ARRAY_LENGTH = 5  # 배열의 행과 열 크기(고정)

class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printData():
    for i in range(0, ARRAY_LENGTH):
        for k in range(0, ARRAY_LENGTH):
            try:
                print("%5d" % dataArray[i][k], end='')
            except:
                pass
        print()
    print('--------------------------------------')

def replaceData():
    current = head
    for i in range(len(current.data)):
        if current.data[i] < 0:
            current.data[i] = 0
        if current.data[i] > 100:
            current.data[i] = current.data[i] % 100
    # print(current.data,)
    while current.link != None:
        current = current.link
        for i in range(len(current.data)):
            if current.data[i] < 0:
                current.data[i] = 0
            if current.data[i] > 100:
                current.data[i] = current.data[i] % 100
        # print(current.data,)
    print()

def MaxSum():
    current = head
    curSum = 0

    while current.link != None:
        pre = current
        current = current.link
        for i in range(ARRAY_LENGTH - 1):
            hap = pre.data[i] + pre.data[i + 1] + current.data[i] + current.data[i + 1]
            if hap > curSum:
                curSum = hap
    print(f'최대 영역의 합 {curSum}')

head,current ,pre = None,None,None
dataArray = \
        [
            [5, 7, -5, 100, 73],
            [35, 23, 4, 190, 33],
            [49, 85, 662, 39, 81],
            [124, -59, 86, 46, 52],
            [27, 7, 8, 33, -56]
        ]
print(' ----- 초기 배열 -----')
printData()

## 메인
node = Node()
node.data = dataArray[0]
head = node


for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node


replaceData()
print(' ----- 치환 후 배열 -----')
printData()

MaxSum()

