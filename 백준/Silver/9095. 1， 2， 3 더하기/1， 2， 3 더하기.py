n = int(input())
caseList = [int(input()) for _ in range(n)]

dp = [0] * 11
dp[0] = 1 # 다이나믹 프로그래밍 문제에서 0을 만드는 방법은 아무것도 선택하지 않는 것
dp[1] = 1 # 1을 만드는 방법은 오직 하나, 1 자체를 선택하는 것 뿐
dp[2] = 2 # 2를 만드는 방법은 두가지가 있다. 1+1과 2 자체를 선택하는 것
dp[3] = 4 # 3을 만드는 방법은 총 4가지가 있다. 1+1+1, 1+2, 2+1, 3

# 이러한 초기 조건을 설정하는 이유는, 이후의 계산에서 이 값을 기반으로 해서,
# 더 큰 수를 구성하는 방법의 수를 재귀적으로 계산하기 위해서다. 
# 예를 들어 dp[4]를 구하려면 dp[3], dp[2], dp[1]의 값을 이용해 4를 만들 수 있는 방법의 수를 계산하게 됨

for i in range(4, 11):
  dp[i] = dp[i-1] + dp[i-2] + dp[i-3] # 천잰가..?


for case in caseList:
  print(dp[case])