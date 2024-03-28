import sys
input=sys.stdin.readline

n, inputNum = map(int, input().split())
dix = {}

for _ in range(n):
  email, pw = input().split()
  dix[email] = pw

for _ in range(inputNum):
  inputPw = input()
  print(dix[inputPw])
