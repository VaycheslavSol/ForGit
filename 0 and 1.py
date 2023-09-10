N = int(input())
if N % 100 != 0 and N % 4 == 0 or N // 400 > 0 and N % 400 == 0:
    print('YES')
else:
    print('NO')
