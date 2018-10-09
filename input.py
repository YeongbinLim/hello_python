#num=int(input())
#board=[[int(x)for x in input().split()]for y in range(num)]
#print(board)


# 4
# 1 3 4 4
# 2 2 3 4
# 4 4 4 1
# 1 2 3




#num=int(input())
#board=[[0]*num for y in range(num)]
#num에 따라 x축 크기 변경 가능
#board[0][1]=3
#print(board)

# [[0, 3, 0], [0, 0, 0], [0, 0, 0]]


num=input()
num=num.split()
print(num[0])
board=[[0]*int(num[0]) for y in range(len(num))]
print(board)

# 1 2 하면 됨

Ni=input()
Ni=Ni.split()
Ni = [int (i) for i in Ni]

# 1 2 3 4 를 int 로 받아옴거
