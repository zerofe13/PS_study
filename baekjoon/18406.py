n = str(input())

left = 0
right = 0

for i,v in enumerate(n):
    if i <(len(n)//2):
        left += int(v)
    else:
        right += int(v)
if left == right:
    print('LUCKY')
else:
    print('READY')