### 연결리스트   논리적인 연결
# 오버헤드 없음, 접근속도 느림

# 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None


# 전역

# 메인
node1 = Node()
node1.data = '다현'
node2 = Node()
node2.data = '정연'
node1.link = node2
node3 = Node()
node3.data = '쯔위'
node2.link = node3
node4 = Node()
node4.data = '사나'
node3.link = node4
node5 = Node()
node5.data = '지효'
node4.link = node5

### 삽입
newNode = Node()
newNode.data = '재남'
newNode.link = node2.link
node2.link = newNode

## 삭제
# node2.link = node3.link   # 삽입에 이을려면 newNode가 있어야한다
# del(node3)

node2.link = newNode.link
del(newNode)


current = node1
print(current.data,end = ' ')
while current.link != None:
    current = current.link
    print(current.data, end=' ')



# print(node1.data,end = ' ')
# print(node1.link.data,end = ' ')
# print(node1.link.link.data,end = ' ')
# print(node1.link.link.link.data,end = ' ')
# print(node1.link.link.link.link.data,end = ' ')