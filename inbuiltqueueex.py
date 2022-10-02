import queue

a= queue.Queue()
b= queue.Queue()

for x in range(5):
    b.put(x)

print(a.empty())
print(b.empty())
