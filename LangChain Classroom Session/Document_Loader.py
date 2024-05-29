#pip install langchain


# from langchain_community.document_loaders import TextLoader

# loader = TextLoader(r"C:\Users\sahil\OneDrive\Naresh IT Class\LangChain\mbox-short.txt")
# data = loader.load()
# print(type(data))
# # print(data[0])
# # print(data[0].page_content)
# # print(data[0].metadata)



from langchain_community.document_loaders.csv_loader import CSVLoader


loader = CSVLoader(file_path=r"C:\Users\sahil\Downloads\diabetes.csv")
data = loader.load()
# print(type(data))
# print(data[0])
# print(data[0].page_content)
print(data[0].metadata)