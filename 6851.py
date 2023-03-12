import sys
from fractions import Fraction


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    return N


ans = []
# 입력 받는 부분
N = Input_Data()

# 여기서부터 작성
# ans.append('0/1')
# ans.append('1/1')
# ans = [0/1, 1/1]
for i in range(1,N+1):
    # print('i = ', i)
    for j in range(0,i):
        # print('j =', j)
        fraction = Fraction(j,i)
        if fraction != 0 and fraction != 1:
            # print('fration =',Fraction(j,i))
            ans.append(fraction)
            # a = '{}/{}'.format(j,i)
            # print(a)
# print('anssss =', ans)
ans = sorted(list(set(ans)))
new_ans = ['0/1']
for i in ans:
    new_ans.append(str(i))
new_ans.append('1/1')
# print("new jeans ===",new_ans)
# print(ans)
# print('ssibal = ', ans[-1])
# ans[0] = '0/1'
# ans[-1] = '1/1'
# for i in ans:
#     print("sex =", i)

# 출력하는 부분
# print('0/1')
print(*new_ans, sep='\n')
# print('1/1')
# 5
#
# 0/1
# 1/5
# 1/4
# 1/3
# 2/5
# 1/2
# 3/5
# 2/3
# 3/4
# 4/5
# 1/1