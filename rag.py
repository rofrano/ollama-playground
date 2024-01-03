"""
Basic example of using Ollama
"""
# cspell: disable
import time

# Load web page
import argparse
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Embed and store 
from langchain.vectorstores import Chroma
from langchain.embeddings import GPT4AllEmbeddings
from langchain.embeddings import OllamaEmbeddings # We can also try Ollama embeddings

from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from langchain import hub  # for RAG prompt
from langchain.chains import RetrievalQA  # for QA chain


def main():
    parser = argparse.ArgumentParser(description='Filter out URL argument. ')
    parser. add_argument('--url', type=str, default='http://example.com', required=True, help='The URL to filter out')

    args = parser.parse_args()
    url = args.url
    print (f"using URL: {url}")

    loader = WebBaseLoader(url)
    data = loader.load()

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=100)
    all_splits = text_splitter.split_documents(data)
    print(f"Split into {len(all_splits)} chunks")

    vectorstore = Chroma.from_documents (documents=all_splits,
                                         embedding=OllamaEmbeddings()
                                         )
    # Retrieve
    question = "What are the latest headlines on TechCrunch?"
    docs = vectorstore.similarity_search(question)
    
    print (f"Loaded {len(data)} documents")
    print (f"Retrieved {len(docs)} documents")

    # RAG prompt
    QA_CHAIN_PROMPT = hub.pull("rlm/rag-prompt-llama")
    
    # LLM
    llm = Ollama(model="llama2",
                verbose=True,
                callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
                )
    print(f"Loaded LLM model {llm.model}")
    
    # QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
    )

    # Ask a question
    question = f"What are the latest headlines on {url}?"
    result = qa_chain({"query": question})

    print(result)

# python rag.py --url https://techcrunch.com/
if __name__ == "__main__":
    start = time.perf_counter()  # Save the current time before calling the functions
    main()
    end = time.perf_counter()     # Save the current time after calling the functions
    execution_time = end - start  # Calculate the elapsed time

    print("\n---\nTotal execution time took {:.6f} seconds to execute.".format(execution_time))
