import threading
import time


def function(n):
    for i in range(n):
        print(i, " in func")
        time.sleep(0.1)


a = threading.Thread(target=function, args=(50,))
a.start()
for i in range(100):
    print(i, " not in func")
    time.sleep(0.1)