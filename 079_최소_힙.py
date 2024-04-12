import heapq
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
data = [ int(input()) for _ in range(n)]

min_heap = []
result = []

for x in data:
  if x == 0:
    print("min_heap", min_heap)
    if min_heap:
      print("if min_heap", min_heap)
      result.append(heapq.heappop(min_heap))
    else:
      result.append(0)
  else:
    heapq.heappush(min_heap, x)

print(*result)

# heapq 모듈은 리스트를 힙처럼 다룰 수 있도록 도와주는 함수를 제공함.
# 힙은 데이터를 특정한 순서대로 자동으로 정렬해주는 자료구조임.
# 이 경우에는 최소 힙을 사용하고 있어서 가장 작은 값이 항상 힙의 첫번째 요소가 되도록 유지됨.
# heapq.heappush(min_heap, x) x를 heap 리스트에 추가해주는 함수임.
# 이 함수를 사용하면 x는 리스트 heap의 적절한 위치에 삽입돼서 힙의 성질이 유지됨.
# 예를 들어 heap리스트에 [1,3,2]가 있고 4를 추가하고 싶으면 
# heapq.heappush(heap, 4)를 호출하면 heap은 [1,3,2,4]로 유지됨.
# 여기서 가장 작은 값 1이 가장 앞에 있어서 힙의 조건을 만족함.
# heapq.heappop(heap) 함수는 힙인 heap 리스트에서 가장 작은 요소를 제거하고 그 값을 반환함.
# 여기서 가장 작은 값 1이 가장 앞에 있어서 힙의 조건을 만족함.
# 이 함수를 호출하면 힙의 첫 번째 요소를 제거하고 힙의 나머지 요소들은 다시 힙의 성질을 만족하도록 재정렬됨.
# 만약 heap 리스트가 [1,3,2,4]였다면 heapq.heappop(heap)을 호출하면 1이 반환되고, 남은 리스트는 2,3,4 처럼 재 정렬됨.
# 여기에서도 가장 작은 2가 앞에 오게 됨.




