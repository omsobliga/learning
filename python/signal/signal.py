"""
signal.signal() 函数允许定义在接收到信号时执行的自定义处理程序。

注意事项：
- 只有主解释器的主线程才被允许设置新的信号处理程序。
- Python 信号处理程序总是会在主 Python 主解释器的主线程中执行，即使信号是在另一个线程中接收的。这意味着信号不能被用作线程间通信的手段。
"""
import time

import signal, os

def handler(signum, frame):
    signame = signal.Signals(signum).name
    print(f'Signal handler called with signal {signame} ({signum})')
    raise OSError("Couldn't open device!")

# 设置信号处理器及 5 秒警报
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

# open() 可能会无限挂起
fd = os.open('/dev/ttyS0', os.O_RDWR)
time.sleep(10)

signal.alarm(0)          # 禁用警报
