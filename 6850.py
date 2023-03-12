import sys

def Input_Data():
    readl = sys.stdin.readline
    num = int(readl())
    return num


ans = 0
# 입력 받는 부분
num = Input_Data()

# 여기서부터 작성
a = False
while a is not True:
    print('num = ', num)
    str_num = str(num)
    num_list = sorted(str_num)
    max_num = int(''.join(map(str, reversed(num_list))))
    min_num = int(''.join(map(str, num_list)))
    diff = max_num - min_num
    print('max_num = %d, min_num = %d, diff = %d'%(max_num, min_num, diff))
    ans += 1
    if diff == 6174:
        a = True
    else:
        num = diff

# 출력하는 부분
print(ans)

#1789
#3