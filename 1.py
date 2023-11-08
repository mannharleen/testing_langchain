from dotenv import load_dotenv

from langchain.chat_models.cohere import ChatCohere
from langchain.prompts import ChatPromptTemplate
from langchain.schema import BaseOutputParser


load_dotenv()


model = ChatCohere()

prompt = ChatPromptTemplate.from_messages([
    ("system", "you are a helpful assistance who returns a comma separated list of words. only return a comma separated list, nothing more."),
    ("human", "{text}")
])

class CommaSeparatedListOutputParser(BaseOutputParser):
    def parse(self, text: str):
        return text.strip().split(sep=",")
    
    
chain = prompt | model | CommaSeparatedListOutputParser()

print (chain.invoke({
    "text": "states of australia"
}))
