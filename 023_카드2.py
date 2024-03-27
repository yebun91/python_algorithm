from collections import deque

n = int(input())
my_list = deque(range(1, n+1))

while len(my_list) > 1 :
  my_list.popleft()
  my_list.rotate(-1)

print(my_list[0])
