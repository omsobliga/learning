# GIL 是什么

GIL 全称 global interpreter lock（全局解释器锁）。

GIL 不是 Python 的特性，而是 CPython 的特性。GIL 是一个互斥锁，用于保护对 Python 对象的访问，防止多个线程同时执行 Python 字节码。GIL 可防止竞争条件并确保线程安全。[1]

Python 多线程的执行方式：

- step1 获取 GIL
- step2 执行代码，直到遇见 IO 操作或者 ticks 计数达到 100
- step3 释放 GIL

在 python3 环境，将切换颗粒度从基于 opcode 计数改成基于时间片计数。[2]

# 引用

1. [GlobalInterpreterLock](https://wiki.python.org/moin/GlobalInterpreterLock)
2. https://mail.python.org/pipermail/python-dev/2009-October/093321.html
