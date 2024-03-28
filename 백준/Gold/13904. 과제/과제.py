n = int(input())
w = [] #[[과제 마감일, 과제의 점수]]

for _ in range(n):
  t, s = map(int, input().split())
  w.append([t, s])

w.sort(key= lambda x: (-x[1]))
zero_list = [0] * max(w)[0] 

for i in w :
  index = i[0] -1
  while index >= 0:
    if zero_list[index] < i[1]:
      zero_list[index] = i[1]
      break
    else:
      index -= 1

print(sum(zero_list))
