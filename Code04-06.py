## 연결리스트 심화

## 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def insert_node(findDate,insertData):
    global memory, head , current, pre
    # 첫노드 앞에 삽입
    if findDate == head.data:
        node =Node()
        node.data = insertData
        node.link = head
        head = node
        return
    # 중간노드 삽입 (사나 앞에 솔라)
    current = head
    while current.link  != None:
        pre = current
        current = current.link
        if current.data == findDate:  # 삽입처리
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    # 마지막에 추가할때
    node = Node()
    node.data = insertData
    current.link = node
    return

def deleteNode(deleteDate):
    global memory, head, current, pre
    # 첫 노드 삭제
    if deleteDate == head.data:
        current = head
        head = head.link
        del(current)
        return
    # 두번째 이후를 삭제
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteDate:
            pre.link = current.link
            del(current)
            return

def findNode(findDate):
    global memory, head, current, pre
    current = head
    if current.data == findDate:
        return current
    while current.link != None:
        current = current.link
        if current.data == findDate:
            return current
    return Node()

## 전역
memory  = []
head,current ,pre = None,None,None

dataArray = ['다현','정연','쯔위','사나','지효']



## 메인
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:]: # ['정연','쯔위','사나','지효']
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)

# insert_node('다현', '화사')
# printNodes(head)
#
# insert_node('사나', '솔라')
# printNodes(head)
# insert_node('제남', '문별')
# printNodes(head)
#
# deleteNode('화사')
# printNodes(head)
# deleteNode('쯔위')
# printNodes(head)

fNode = findNode('다현')
print(fNode.data)
fNode = findNode('쯔위')
print(fNode.data)
fNode = findNode('재남')
print(fNode.data)