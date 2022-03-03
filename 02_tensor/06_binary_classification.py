import tensorflow as tf

# 1. 데이터 준비
x_data = [
    [1,0],
    [2,0],
    [5,1],
    [2,3],
    [3,3],
    [8,1],
    [10,0],
]
y_data = [
    [0],
    [1],
    [0],
    [0],
    [1],
    [1],
    [1],
]
x = tf.placeholder(shape=[None,2],dtype=tf.float32)
y = tf.placeholder(shape=[None,1],dtype=tf.float32)

# 2. 가설 설정
W = tf.Variable(tf.random_normal([2,1]),name='weight')
b = tf.Variable(tf.random_normal([1]),name='bias')

# sigmoid : 0 ~ 1 사이의 실수 (H>0.5 : True)  => 0 / 1 로 결과 확인하고 싶어서!
logit = tf.matmul(x,W) + b
H = tf.sigmoid(logit) # 이진 분류

# 3. 준비
# loss function
# loss = tf.reduce_mean(tf.square(H -y))
# loss 값을 미분했을때 0이 되는 지점이 1개가 아니다!!!
# 선하나로 분리 어려움 곡선이 왔다리 갔다리 단순하게 차이제곱이 안됨 그래서 sigmoid를 쓰나??
loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits = logit,labels=y))
# optimizer
learning_rate = 0.1
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train = optimizer.minimize(loss)

# session
sess = tf.Session()
sess.run(tf.global_variables_initializer())
# 4. 학습
epochs = 10000
for step in range(epochs):
    _, loss_val, W_val, b_val = sess.run([train, loss, W, b], feed_dict={x:x_data, y:y_data})
    if step % 500 == 0:
        print(f'W: {W_val} \t b:{b_val} \t loss:{loss_val} ')
# 5. 예측 평가
print(sess.run(H,feed_dict={x:[[4,2],[2,4]]}))