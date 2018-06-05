def fn():
    for i in range(100):
        yield i

if __name__ == '__main__':
    for x in fn():
        print(x)