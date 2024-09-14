import json
import random
import message_pb2

vector = [random.uniform(0, 1) for i in range(768)]
data = {"id": 1, "vector": vector}
msg = message_pb2.ProductVector(**data)

with open("/tmp/data.bin", "wb") as f:
    f.write(msg.SerializeToString())

data = {"vector": vector}
print(data)
vector = message_pb2.Vector(**data)
with open("/tmp/vector.bin", "wb") as f:
    f.write(vector.SerializeToString())
