import json
import random
import time

import message_pb2

vector = [random.uniform(0, 1) for i in range(768)]
data = {"id": 1, "vector": vector}

N = 1000

start = time.time()
for i in range(N):
    json.dumps(data)
end = time.time()
print(f"json dumps time: {(end - start) * 1000}ms")

dump_data = json.dumps(data)
start = time.time()
for i in range(N):
    json.loads(dump_data)
end = time.time()
print(f"json loads time: {(end - start) * 1000}ms")

msg = message_pb2.ProductVector(**data)
start = time.time()
for i in range(N):
    msg.SerializeToString()
end = time.time()
print(f"protobuf serialize time: {(end - start) * 1000}ms")

serialize_data = msg.SerializeToString()
product_vector = message_pb2.ProductVector()
start = time.time()
for i in range(N):
    product_vector.ParseFromString(serialize_data)
end = time.time()
print(f"protobuf deserialize time: {(end - start) * 1000}ms")
