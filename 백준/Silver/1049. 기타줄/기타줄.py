사야하는줄수, n = map(int, input().split())
# [[6개 패키지가격, 낱개가격]]
브랜드 = [list(map(int, input().split())) for _ in range(n)]
가장낮은패키지가격 = min(브랜드, key=lambda x: x[0])[0]
가장낮은낱개가격 = min(브랜드, key=lambda x: x[1])[1]

답 = 0

if 가장낮은패키지가격 <= 가장낮은낱개가격 * 6 :
  답 += (사야하는줄수 // 6) * 가장낮은패키지가격
  남은줄수 = 사야하는줄수 % 6
  if 남은줄수 * 가장낮은낱개가격 < 가장낮은패키지가격:
    답 += 남은줄수 * 가장낮은낱개가격
  else: 
    답 += 가장낮은패키지가격
else:
  답 = 사야하는줄수 * 가장낮은낱개가격
    
print(답)