import json
import random
import time

from pymilvus import MilvusClient

client = MilvusClient("http://127.0.0.1:19530")

# create_collection
if client.has_collection(collection_name="demo_collection"):
    client.drop_collection(collection_name="demo_collection")
client.create_collection(
    collection_name="demo_collection",
    dimension=768,  # The vectors we will use in this demo has 768 dimensions
)

with open("/tmp/data.json", "r") as f:
    vector = json.loads(f.read())

# insert
N = 1000000
M = 10000
start_time = time.time()
for i in range(N):
    data = {"id": i, "vector": vector}
    client.insert(collection_name="demo_collection", data=data)
end_time = time.time()
print("insert time:", end_time - start_time)

# query
start_time = time.time()
for i in range(M):
    id_ = random.randint(0, N - 1)
    res = client.query(
        collection_name="demo_collection",
        ids=[id_],
        output_fields=["id", "vector"],
    )
end_time = time.time()
print("query time:", end_time - start_time)

# query
start_time = time.time()
for i in range(M):
    ids = []
    for j in range(10):
        id_ = random.randint(0, N - 1)
        ids.append(id_)
    res = client.query(
        collection_name="demo_collection",
        ids=ids,
        output_fields=["id", "vector"],
    )
end_time = time.time()
print("query time:", end_time - start_time)
