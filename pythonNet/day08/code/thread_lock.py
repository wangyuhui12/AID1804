
import threading

a = b = 0
lock = threading.Lock()

def value():
    lock.acquire()
    while True:
        if a != b:
            print("a = %d, b = %d" %(a, b))
    lock.release()

t = threading.Thread(target = value)
t.start()

while True:
    lock.acquire()
    a += 1
    b += 1
    lock.release()

t.join()