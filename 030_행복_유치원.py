n, k = map(int, input().split())
heights = list(map(int, input().split()))

# 각각 키 사이의 차이를 담을 배열
diffHeights = []
for i in range(n-1):
  diff = heights[i + 1] - heights[i]
  diffHeights.append(diff)

diffHeights.sort(reverse=True) # 키 차이가 큰 순으로 정렬

# k개의 조가 필요하다면 나눠지는 부분은 k-1임. 키차이가 가장 큰 순서대로 정렬되어 있으니 
# 가장 큰 부분[k-1: ]을 제외한 나머지를 모두 더함
print(sum(diffHeights[k-1:])) 