import chromadb
chroma_client = chromadb.Client()

collection = client.create_collection(
        name="collection_name",
        metadata={"hnsw:space": "cosine"} # l2 is the default
    
)
collection.add(
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges"

    ],
    ids=["id1", "id2"]


)
results = collection.query(
    query_texts=["This is a query document about hawaii"], # Chroma will embed this for you
    n_results=2 # how many results to return
)
print(results)


client = chromadb.PersistentClient(path="../data")
client.heartbeat() 
client.reset()


# import
import chromadb.utils.embedding_functions as embedding_functions

# use directly
google_ef  = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key="YOUR_API_KEY")
google_ef(["document1","document2"])

# pass documents to query for .add and .query
collection = client.create_collection(name="name", embedding_function=google_ef)
collection = client.get_collection(name="name", embedding_function=google_ef)
