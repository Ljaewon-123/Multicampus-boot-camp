class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

memory = []
root = None
nameAry = ['블','레','마마','에이','걸스','트와이스']

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
            # print(name,current.data)
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
findData = '마마'

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