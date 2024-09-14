# json vs protobuf

## storage size

Python
```
python to_json.py
python to_protobuf.py
wc /tmp/vector.json /tmp/vector.bin
0     771   15585 /tmp/data.json
10      78    3077 /tmp/data.bin
```

Go
```
go run to_json.go
go run to_protobuf.go
wc /tmp/data.json /tmp/data.bin
0       1   14814 /tmp/data.json
13     133    6149 /tmp/data.bin
```

## serialize/deserialize time

Python
```
python benchmark.py
json dumps time: 631.1030387878418ms
json loads time: 303.4040927886963ms
protobuf serialize time: 1.0738372802734375ms
protobuf deserialize time: 3.0951499938964844ms
```

Go
```
go run benchmark.go
json marshal time: 120.119371ms
json unmarshal time: 237.314816ms
protobuf marshal time: 1.956725ms
protobuf unmarshal time: 2.235183ms
```