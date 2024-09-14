import json
import random

vector = [random.uniform(0, 1) for i in range(768)]
data = {"id": 1, "vector": vector}

with open("/tmp/data.json", "w") as f:
    json.dump(data, f)
