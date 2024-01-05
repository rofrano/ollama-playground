"""
Basic example of using Ollama
"""
# cspell: disable
import time
import argparse
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def query_model(topic):
    """
    Query the model with a given topic.

    Args:
        topic (str): The topic to query the model with.

    Returns:
        str: The response from the model.
    """
    llm = Ollama(model="llama2",
                callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]),
                temperature=0.9)

    # Create a prompt with substitution variables
    prompt = PromptTemplate(
        input_variables=["topic"],
        template="Give me 5 interesting facts about {topic}?",
    )

    # Create the chain
    chain = LLMChain(llm=llm, prompt=prompt)

    # Run the chain and return the results
    return chain.run(topic)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=str, default="the moon")
    args = parser.parse_args()
    print(f"Running with topic: {args.topic}")

    start = time.perf_counter()  # Save the current time before calling the functions

    #  Call the model and print the results
    print(query_model(args.topic))

    end = time.perf_counter()     # Save the current time after calling the functions
    execution_time = end - start  # Calculate the elapsed time
    print(f"\n---\nTotal execution time took {execution_time:.6f} seconds to execute.")
