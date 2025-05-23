from llama_index.core import VectorStoreIndex
from llama_index.core import Document

from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext

import chromadb

from traceloop.sdk import Traceloop
from traceloop.sdk.decorators import workflow, task

Traceloop.init()

remote_db = chromadb.HttpClient(port=8001)
chroma_collection = remote_db.get_or_create_collection("my_documents")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
index = VectorStoreIndex.from_vector_store(vector_store)

@task(name="index_documents")
def index_documents(documents: list[Document]):
    for document in documents:
        index.insert(document)

@task(name="query_documents")
def query_documents(query: str) -> str:
    query_engine = index.as_query_engine()
    return query_engine.query(query)


@workflow(name="quick-rag")
def run_quick_rag():
    documents = [
        Document(text="Anton has 3 cats and 2 dogs"),
        Document(text="Anton has 1 giraffes"),
        Document(text="Anton has 5 squirrels living in the tree in his backyard"),
        Document(text="Anton has 16 ants living in his ant farm"),
    ]    

    index_documents(documents)
    response = query_documents("How many dogs Anton has?")

    print(response)


if __name__ == "__main__":
    run_quick_rag()