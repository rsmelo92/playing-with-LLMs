import validators
from prepare import prepare_llm, prepare_retrieval_QA, parse_arguments
from ingest import load_single_document
from langchain.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain

def load_web_document(path):
    loader = WebBaseLoader(path)
    return loader.load()

def main():
    print("summarizing...")
    llm = prepare_llm()

    # doc_path = "/Users/melo/github/private-original-gpt/source_documents/Multiple.txt"
    doc_path = "/Users/melo/github/private-original-gpt/source_documents/USS.txt"
    # doc_path = "https://engineering.atspotify.com/2023/05/multiple-layers-of-abstraction-in-design-systems/"

    if validators.url(doc_path) is True:
        docs = load_web_document(doc_path)
    else:
        docs = load_single_document(doc_path)

    chain = load_summarize_chain(llm, chain_type="stuff")
    chain.run(docs)

if __name__ == "__main__":
    main()
