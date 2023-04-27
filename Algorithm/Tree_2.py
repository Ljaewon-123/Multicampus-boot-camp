### 이진 탐색 트리 일반 구현

## 함수
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None
## 전역
memory = []
root = None
nameAry = ['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']

## 메인
# 첫 노드 생성(루트노드)
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]:
    node = TreeNode()
    node.data = name

    current = root
    while True:
        if name < current.data :
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right

    memory.append(node)

print('이진탐색트리완료')
## 탐색
findData = '바마무'

current = root
while True:
    if current.data == findData:
        print(findData, '찾음')
        break
    elif current.data > findData:
        if current.left == None:
            print(findData,' 이 트리에 없음 ')
            break
        current = current.left
    else:
        if current.right == None:
            print(findData,' 이 트리에 없음 ')
            break
        current = current.right