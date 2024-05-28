#pip install langchain-google-genai

from langchain_google_genai import GoogleGenerativeAI

api_key = "AIzaSyDMDsDDs5aHpJ69pBKedgzK3_EpAIcmyfQ"

llm = GoogleGenerativeAI(model='gemini-1.5-flash-latest', google_api_key=api_key)

print(
    llm.invoke(
        "List of 5 Indian Actors"
    )
)