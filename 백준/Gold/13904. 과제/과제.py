import sys
input=sys.stdin.readline

n = int(input())
w = [] #[[과제 마감일, 과제의 점수]]

for _ in range(n):
  t, s = map(int, input().split())
  w.append([t, s])

w.sort(key= lambda x: (-x[1]))
zero_list = [0] * max(w)[0] # [0, 0, 0, 0, 0, 0]

for i in w :
  index = i[0] -1 # 날짜를 인덱스처럼 사용하려면 -1 해줘야 함
  while index >= 0: # 0번째 인덱스도 있기 때문에 0을 포함해야 함
    if zero_list[index] < i[1]: # 해당 인덱스의 숫자가 점수보다 작은 경우
      zero_list[index] = i[1]
      break
    else:
      # 해당 인덱스에 이미 점수가 있고 그 점수가 i의 점수보다 큰 경우에 인덱스를 1 낮춤
      index -= 1

print(sum(zero_list))