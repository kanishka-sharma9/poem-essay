from fastapi import FastAPI
from langserve import add_routes
from langchain.prompts import ChatPromptTemplate
import google.generativeai as genai
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import uvicorn
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app=FastAPI(
    title="Langserve Demo",
    version="1.0",
    description="a simple api server"
)

model=ChatGoogleGenerativeAI(model="gemini-pro")
add_routes(
    app,
    ChatGoogleGenerativeAI(model='gemini-pro'),
    path="/gemini-chat"

)


prompt=ChatPromptTemplate.from_template("write a 200 word essay about {topic}")
prompt1=ChatPromptTemplate.from_template("write a poem about {topic}")

add_routes(
    app,
    prompt|model,
    path="/essay"
)

add_routes(
    app,
    prompt1|model,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)