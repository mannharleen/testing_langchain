from langchain.llms.cohere import Cohere
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from dotenv import load_dotenv
load_dotenv()

def lc_pet_names(pet_type: str = 'dog', pet_colors:str = 'red') -> str:
    model = Cohere()

    prompt = PromptTemplate(
        input_variables=[
            "pet_type",
            "pet_colors"
        ],
        template="""Provide uncommon pet names for the pet of type {pet_type} that has the following colors {pet_colors}. Respond in bullet points in alphabetical order"""
    )

    chain = LLMChain(
        llm=model,
        prompt=prompt,
        output_key="pet_names"
    )
    
    response = chain({"pet_type":pet_type, "pet_colors":pet_colors})
    return response['pet_names']

if __name__ == "__main__":
    print(lc_pet_names())