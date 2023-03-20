import sys

def Input_Data():
    readl = sys.stdin.readline
    R = int(readl())
    return R


ans = -1
# 입력 받은 부분
R = Input_Data()

# 여기서부터 작성
if 2*((R-1)**2) < R**2 :
    ans = 4*((R-1)**2)
else:
    ans = 4*((R-1)**2-1)

# 출력하는 부분
print(ans)
