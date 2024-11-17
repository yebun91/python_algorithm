def count_to_turn_out(s):
    all_make_zero = 0
    all_make_one = 0

    if s[0] == '0':
        all_make_one += 1
    else:
        all_make_zero += 1

    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            if s[i] == "0":
                all_make_one += 1
            else:
                all_make_zero += 1

    print(min( all_make_zero, all_make_one))


s = input()
count_to_turn_out(s)