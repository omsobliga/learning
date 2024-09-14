import random
import time

from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

database = client["test_database"]
database.drop_collection("test_collection")
database.create_collection("test_collection")
collection = database["test_collection"]
collection.create_index("id", unique=True)

with open("/tmp/data.json", "r") as f:
    vector = f.read()

N = 5000000
M = 100000
start_time = time.time()
for i in range(N):
    data = {
        "id": i,
        "vector": vector,
    }
    collection.insert_one(data)
end_time = time.time()
print("insert time:", end_time - start_time)

start_time = time.time()
for i in range(M):
    id_ = random.randint(0, N - 1)
    collection.find_one({"id": id_})
end_time = time.time()
print("find time:", end_time - start_time)

start_time = time.time()
for i in range(M):
    ids = []
    for j in range(10):
        id_ = random.randint(0, N - 1)
        ids.append(id_)
    res = collection.find({"id": {"$in": ids}})
    list(res)
end_time = time.time()
print("batch find time:", end_time - start_time)
