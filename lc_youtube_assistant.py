import requests

session = requests.Session()
session.verify = False
session.trust_env = False

from langchain.llms.cohere import Cohere
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
#
from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.cohere import CohereEmbeddings
from langchain.vectorstores.faiss import FAISS
from dotenv import load_dotenv
load_dotenv()

def create_db(url:str) -> FAISS:
    docs = YoutubeLoader.from_youtube_url(url).load()
    spliter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_docs = spliter.split_documents(docs)
    embeddings = CohereEmbeddings() # type: ignore
    db = FAISS.from_documents(split_docs, embeddings)
    return db

if __name__ == "__main__":
    print(create_db("https://www.youtube.com/watch?v=lG7Uxts9SXs&t=2325s"))