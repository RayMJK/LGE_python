import sys

def Input_Data():
    readl = sys.stdin.readline
    R = int(readl())
    return R


ans = 0
# 입력 받은 부분
R = Input_Data()

# 여기서부터 작성
if R > (2*((R-1)**2))**(1/2):
    ans = ((R-1)**2)*4
else:
    ans = ( ((R-2)**2) + (R-2)*2 )*4



# 출력하는 부분
print(ans)