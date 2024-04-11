number = input()

zero = [ x for x in number.split("1") if x ]
one = [ x for x in number.split("0") if x ]

print(min(len(zero), len(one)))
