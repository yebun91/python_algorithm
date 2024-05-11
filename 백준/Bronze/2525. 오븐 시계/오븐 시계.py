time, minute = map(int, input().split())
plusMinute = int(input())
minute += plusMinute

time += minute // 60
minute = minute % 60
time = time % 24

print(time, minute)