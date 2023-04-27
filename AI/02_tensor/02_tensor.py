import tensorflow as tf

# dtype = tf.float32 == dtype=np.float32 (tensorflow 내부적으로 numpy 사용중!)
node1 = tf.constant(10,dtype=tf.float32)
node2 = tf.constant(20,dtype=tf.float32)

node3 = node1 + node2

sess = tf.Session()  # 그래프 실행 환경
print(sess.run(node3))

print(sess.run([node1,node2]))