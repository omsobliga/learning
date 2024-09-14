# benchmark

测试环境

```
系统 MacOS
CPU 16 核
内存 18G
磁盘 SSD
```

## Mongodb

```
10000 rows
0.60ms per insert 1 row
0.25ms per query 1 row
0.77ms per query 10 rows

100000 rows
0.58ms per insert 1 row
0.27ms per query 1 row
0.79ms per query 10 rows

1000000 rows
0.59ms per insert 1 row
0.79ms per query 1 row
2.03ms per query 10 rows
```

## Cassandra

```
10000 rows
1.68ms per insert 1 row
1.41ms per query 1 row
11.15ms per query 10 rows

100000 rows
1.79ms per insert 1 row
1.96ms per query 1 row
11.38ms batch query 10 rows

1000000 rows
3.13ms per insert 1 row
3.74ms per query 1 row
13.34ms batch query 10 rows
```

## MySQL

```
10000 rows
0.42ms per insert 1 row
0.11ms per query 1 row
0.11ms per query 10 rows

100000 rows
0.28ms per insert 1 row
0.16ms per query 1 row
0.23ms per query 10 rows

1000000 rows
0.28ms per insert 1 row
0.38ms per query 1 row
0.38ms per query 10 rows

5000000 rows
0.38ms per insert 1 row
0.39ms per query 1 row
0.40ms per query 10 rows
```
