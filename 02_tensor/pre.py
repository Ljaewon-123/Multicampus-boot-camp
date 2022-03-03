import tensorflow as tf

# 1. 데이터 준비
x_data = [
    [0,0],
    [0,1],
    [1,0],
    [1,1],
]
y_data = [
    [0],
    [1],
    [1],
    [0],
]

x = tf.placeholder(shape=[None,2],dtype=tf.float32)
y = tf.placeholder(shape=[None,1],dtype=tf.float32)

W1 = tf.Variable(tf.random_normal([2,10]),name = 'weight1')
b1 = tf.Variable(tf.random_normal([10]),name = 'bias1')
layer1 = tf.sigmoid(tf.matmul(x,W1)+b1)

W2 = tf.Variable(tf.random_normal([10,20]),name = 'weight2')
b2 = tf.Variable(tf.random_normal([20]),name = 'bias2')
layer2 = tf.sigmoid(tf.matmul(layer1,W1)+b1)

W3 = tf.Variable(tf.random_normal([20,10]),name = 'weight3')
b3 = tf.Variable(tf.random_normal([10]),name = 'bias3')
layer3 = tf.sigmoid(tf.matmul(layer2,W1)+b1)

W4 = tf.Variable(tf.random_normal([10,1]),name='weight4')
b4 = tf.Variable(tf.random_normal([1]),name='bias4')

logit = tf.matmul(layer3,W4)+b4
loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logit,labels=y))

train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

epo = 10000
for step in range(epo):
    _,loss_val = sess.run([train,loss],feed_dict={x:x_data,y:y_data})
    if step % 500 == 0:
        print(f'loss: {loss_val}')

# 5.
print(sess.run(H,feed_dict={x:x_data}))