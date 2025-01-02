import argparse
from os import getenv
from langchain_community.llms import VLLMOpenAI
from dotenv import load_dotenv
load_dotenv(".env", verbose=True)



parser = argparse.ArgumentParser(description="Prompt an LLM")   
parser.add_argument("prompt", help="The prompt to send to the LLM, use quotes for longer prompts")
args = parser.parse_args()


print("Prompt against MAAS URI: " + getenv("MAAS_API_URL"))
llm = VLLMOpenAI(
    openai_api_key=getenv("MAAS_API_KEY"),
    openai_api_base=getenv("MAAS_API_URL") + "/v1",
    model_name="granite-3-8b-instruct",
    model_kwargs={"stop": ["."]},
)

print(llm.invoke(args.prompt))