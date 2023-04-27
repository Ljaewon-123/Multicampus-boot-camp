import tensorflow.compat.v1 as tf

# placeholder : 그래프를 실행하는 시점에 데이터를 입력받을수 있도록 해주는놈
node1 = tf.placeholder(dtype=tf.float32)
node2 = tf.placeholder(dtype=tf.float32)

node3 = node1 + node2

sess = tf.Session()

# data 입력해주면서 실행
x = [10,20,30]
y = [40,50,60]

print(sess.run(node3,feed_dict={node1:x,node2:y})) # feed_dict run 하는 시점의 값 딕셔너리 타입
# constant 해당노드에 바로 [상수]값
# 그때그때 다른값 placeholder 메모리(공간) 미리 만듬
