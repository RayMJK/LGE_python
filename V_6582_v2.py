import sys

def Input_Data():
    readl = sys.stdin.readline
    R = int(readl())
    return R


ans = -1
# 입력 받은 부분
R = Input_Data()


def solve():
    R2 = R**2
    cnt = 0
    for h in range(1,R+1):
        h2 = h**2
        cnt += int((R2-h2)**0.5)

    return 4 * cnt
# 여기서부터 작성

ans = solve()

# 출력하는 부분
print(ans)
