import tensorflow as tf

# 1.
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


# 2.
W = tf.Variable(tf.random_normal([2,1]),name= 'weight')
b = tf.Variable(tf.random_normal([1]),name = 'bias')

logit = tf.matmul(x,W) + b
H = tf.sigmoid(logit)

# 3. 준비 -> loss function optimizier session
loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logit,labels=y))

learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())  # 암튼 초기화

# 4.  for
epoch = 30000
for step in range(epoch):
    _,loss_val,W_val,b_val = sess.run([train,loss,W,b],feed_dict={x:x_data,y:y_data})
    if step % 1000 == 0:
        print(f'loss:{loss_val} ')  # loss가 멈추면 다한거?
# 5.
print(sess.run(H,feed_dict={x:x_data}))