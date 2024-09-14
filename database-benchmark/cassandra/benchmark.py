import random
import time

from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'], port=9042)

session = cluster.connect()
# session.execute("""
#     CREATE KEYSPACE test_keyspace
#     WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3}
# """)

session.set_keyspace('test_keyspace')
session.execute('USE test_keyspace')

session.execute(""" DROP TABLE IF EXISTS test_table """)
session.execute("""
    CREATE TABLE test_table (
        id int,
        vector text,
        PRIMARY KEY (id)
    )
""")

with open("/tmp/data.json", "r") as f:
    vector = f.read()

N = 10000
M = 10
start_time = time.time()
for i in range(N):
    session.execute(f"INSERT INTO test_table (id, vector) VALUES ({i}, '{vector}')")
end_time = time.time()
print("insert time:", end_time - start_time)

start_time = time.time()
for i in range(M):
    id_ = random.randint(0, N - 1)
    session.execute(f"SELECT id, vector FROM test_table WHERE id = {id_}")
end_time = time.time()
print("query time:", end_time - start_time)

start_time = time.time()
for i in range(M):
    ids = []
    for j in range(10):
        id_ = random.randint(0, N - 1)
        ids.append(id_)
    session.execute(f"SELECT id, vector FROM test_table WHERE id in ({','.join(map(str, ids))})")
end_time = time.time()
print("batch query time:", end_time - start_time)
