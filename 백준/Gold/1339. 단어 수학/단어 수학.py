n = int(input())
words = [input() for _ in range(n)]
weights = {}

for word in words:
  wordLen = len(word)
  for i in range(wordLen):
    char = word[i]
    power = 10 ** (wordLen - i - 1) 
    if char in weights:
        weights[char] += power
    else:
        weights[char] = power

sorted_weights = sorted(weights.items(), key=lambda item: item[1], reverse=True)
char_to_number = {}
number = 9
for i in range(len(sorted_weights)):
  char_to_number[sorted_weights[i][0]] = number
  number -= 1

result = 0
for word in words:
  change = ""
  for char in word:
    change += str(char_to_number[char])
  result += int(change)

print(result)