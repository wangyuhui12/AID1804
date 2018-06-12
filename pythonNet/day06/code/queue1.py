
from multiprocessing import Queue

#　创建队列 最多存放3条消息
q = Queue(3)
#　向队列中存放一条消息
q.put(1)

print(q.full())
q.put(2)
q.put(3)
print(q.full())
# q.put(4, True, 5)
print(q.get())
print(q.qsize())  # 查看消息数量
print(q.empty())
q.close()