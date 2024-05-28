from langchain_google_genai import GoogleGenerativeAIEmbeddings

api_key = "AIzaSyDMDsDDs5aHpJ69pBKedgzK3_EpAIcmyfQ"

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
vector = embeddings.embed_query("hello, world!")
print(vector[:5])
print(len(vector))