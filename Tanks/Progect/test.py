import multiprocessing

def func():
    for i in range(10000):
        print("World")
thread = multiprocessing.Process(target=func)
thread.start()
for i in range(10000):
    print("Hello")