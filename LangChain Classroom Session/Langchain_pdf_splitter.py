from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader = PyPDFLoader(r"C:\Users\sahil\Downloads\CNN-Sahil.pdf")
pages = loader.load()
pages2 = loader.load_and_split()


# Extract 

text_splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=0
)

# texts = text_splitter.create_documents(pages)
texts = text_splitter.split_documents(pages)

print(texts)
print('============================')
print(texts[0])
print('================ len ================')
print(len(texts[0].page_content))
print('============== type ==================')
print(type(texts))
print('============= chunks ===================')
chunks = [len(i.page_content) for i in texts ]
print(sum(chunks))
print('================================')
