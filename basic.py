"""
Basic example of using Ollama
"""
# cspell: disable
import time
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

start = time.perf_counter()  # Save the current time before calling the functions

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

# Run the chain and output the results
print(chain.run("the moon"))

end = time.perf_counter()     # Save the current time after calling the functions
execution_time = end - start  # Calculate the elapsed time

print("\n---\nTotal execution time took {:.6f} seconds to execute.".format(execution_time))
