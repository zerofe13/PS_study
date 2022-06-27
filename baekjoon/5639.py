#이진 탐색 트리
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

pre_order_list = []

while True:
    try:
        pre_order_list.append(int(input()))
    except:
        break;


def post_order(start,end):
    if start > end:
        return
    mid = end +1; #오른쪽 서브트리로 못가는경우
    for i in range(start+1,end+1):
        if pre_order_list[start]<pre_order_list[i]:
            mid = i
            break
    post_order(start+1,mid-1) # 왼쪽 서브트리
    post_order(mid,end) # 오른쪽 서브트리
    print(pre_order_list[start])

post_order(0,len(pre_order_list)-1)