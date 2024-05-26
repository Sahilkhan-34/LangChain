# pip inatall langchain

from langchain_community.document_loaders.csv_loader import CSVLoader


loader = CSVLoader(file_path=r"C:\Users\sahil\OneDrive\Naresh IT Class\Data Files\bank.csv")
data = loader.load()

# print(data)
print(len(data))
print(data[0])
# print(data[1].page_content)
print(data[1].metadata)
