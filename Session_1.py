# pip install langchain-google-genai

from langchain_google_genai import GoogleGenerativeAI

api_key = 'AIzaSyC_L3-d181ibSultwSEuGm6P4XwE8HIsEQ'

llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)

print(
    llm.invoke('List top 5 indian cricketer')
    )

