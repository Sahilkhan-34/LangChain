# pip install -qU langchain-text-splitters
"""
There are multiple ways to split the data 
1) string concept 
2) word tokenzier and sent tokenizer 
3) using langchain also we can do 

"""

# This is long document we can split up
with open(r"C:\Users\sahil\OneDrive\Naresh IT Class\LangChain\mbox-short.txt") as f:
    mbox_short = f.read()

from langchain_text_splitters import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
    separator='\n\n',
    chunk_size=1000 
)

texts = text_splitter.create_documents([mbox_short])
print(texts)
print('============== tests[0] ==================')
print(texts[0])
print('================ len ================')
print(len(texts[0].page_content))
print('============== type ==================')
print(type(texts))
print('============= chunks ===================')
chunks = [len(i.page_content) for i in texts ]
print(sum(chunks))
print('================================')
