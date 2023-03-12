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

for i in range(1,N+1):
    print('i = ', i)
    for j in range(0,i+1):
        print('j =', j)
        print(Fraction(j,i))
        ans.append(j/i)

# 출력하는 부분
print(*ans, sep='\n')

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