import string

alpha = {ch: 0 for ch in string.ascii_lowercase}
st = input()

for s in st:
  alpha[s] += 1

print(' '.join(str(alpha[ch]) for ch in string.ascii_lowercase))