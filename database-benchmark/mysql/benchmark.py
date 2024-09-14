import random
import time

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='root',
                             database='mysql_benchmark',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        sql = "DROP TABLE IF EXISTS `test_table`"
        cursor.execute(sql)
        sql = """
            CREATE TABLE `test_table` (
                `id` int(11) NOT NULL AUTO_INCREMENT,
                `pid` int(11) NOT NULL,
                `vector` TEXT,
                PRIMARY KEY (`id`),
                UNIQUE KEY (`pid`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """
        cursor.execute(sql)
        connection.commit()

    with open("/tmp/data.json", "r") as f:
        vector = f.read()

    N = 5000000
    M = 100000

    with connection.cursor() as cursor:
        start_time = time.time()
        for i in range(N):
            sql = "INSERT INTO `test_table` (`pid`, `vector`) VALUES (%s, %s)"
            cursor.execute(sql, (i, vector))
            connection.commit()
        end_time = time.time()
        print("insert time:", end_time - start_time)

    with connection.cursor() as cursor:
        start_time = time.time()
        for i in range(M):
            id_ = random.randint(0, N - 1)
            sql = "SELECT `pid`, `vector` FROM `test_table` WHERE `pid`=%s"
            cursor.execute(sql, (id_,))
            cursor.fetchone()
            connection.commit()
        end_time = time.time()
        print("query time:", end_time - start_time)

    with connection.cursor() as cursor:
        start_time = time.time()
        for i in range(M):
            ids = []
            for j in range(10):
                id_ = random.randint(0, N - 1)
                ids.append(id_)
            sql = "SELECT `pid`, `vector` FROM `test_table` WHERE `pid` IN (%s)"
            cursor.execute(sql, (','.join(map(str, ids)),))
            cursor.fetchall()
            connection.commit()
        end_time = time.time()
        print("batch query time:", end_time - start_time)
