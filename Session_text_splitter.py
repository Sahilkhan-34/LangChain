# pip install -qU langchain-text-splitters

# this is long document we can split up

with open(r"C:\Users\sahil\OneDrive\Naresh IT Class\LangChain\mbox-short.txt") as f:
    mbox_short = f.read()
    # print(mbox_short)

from langchain_text_splitters import CharacterTextSplitter

text_splitter=CharacterTextSplitter(
    separator="\n\n",
    chunk_size=1000
)

text = text_splitter.create_documents([mbox_short])
text
# print(text[0])
print(text[0].page_content)
print(len(text[1].page_content))

chunks=[len(i.page_content) for i in text]
print(sum(chunks))