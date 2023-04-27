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
# 입력층
W1 = tf.Variable(tf.random_normal([2,10]),name='weight1') # 2개 들어와서 10개 나감
b1 = tf.Variable(tf.random_normal([10]),name='bias1')
layer1 = tf.sigmoid(tf.matmul(x,W1)+b1)
# 히든층
W2 = tf.Variable(tf.random_normal([10,20]),name='weight2')
b2 = tf.Variable(tf.random_normal([20]),name='bias2')
layer2 = tf.sigmoid(tf.matmul(layer1,W2)+b2)  # layer1 에 보내준걸 가중치 더해서 다음으로 보냄  layer * W+b

W3 = tf.Variable(tf.random_normal([20,10]),name='weight3')
b3 = tf.Variable(tf.random_normal([10]),name='bias3')
layer3 = tf.sigmoid(tf.matmul(layer2,W3)+b3)  #matmul(layer2 곱(*) W3) (합) + b3

# 출력층
W4 = tf.Variable(tf.random_normal([10,1]),name='weight4')
b4 = tf.Variable(tf.random_normal([1]),name='bias4')

logit = tf.matmul(layer3,W4)+b4
H = tf.sigmoid(logit)
# 활성화함수 sigmoid 로 만듬
# 3.
# loss
loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logit,labels=y))

# optimizer
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(loss)
# session
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# 4.
epo = 10000
for step in range(epo):
    _,loss_val = sess.run([train,loss],feed_dict={x:x_data,y:y_data})
    if step % 500 == 0:
        print(f'loss: {loss_val}')

# 5.
print(sess.run(H,feed_dict={x:x_data}))

# cast T / F -> 1 / 0   (/ 0.5 보다 큰지 아닌지로
# equal 같은지 아닌지
# cast 가함
# accuracy H 와 y의 차이가 정확도
pred = tf.cast(H>0.5,dtype=tf.float32)
# 실제 y값이랑 비교
correct = tf.equal(pred,y)
# 그값으로 같음녀 T/F를 1 / 0 으로 바꿈 그리고 퍼센테이지 % 따짐
accuracy = tf.reduce_mean(tf.cast(correct,dtype=tf.float32))
print(sess.run(accuracy,feed_dict={x:x_data,y:y_data})) # [[0,0]] 정확도임 하나를 넣으면 50밖에 안나올수밖에없음
