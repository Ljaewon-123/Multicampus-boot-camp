import tensorflow as tf



# 1. 데이터 준비
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

# 2. 가설 설정
# H (hypothesis) = W (weight) * x + b (bias)
# tf.random_normal : random 으로 표준분포값 설정
W = tf.Variable(tf.random_normal([1]),name = 'weight')
b = tf.Variable(tf.random_normal([1]),name = 'bias')

H = W * x + b
# 3. 준비
# loss function
# Mean Square Error
loss = tf.reduce_mean(tf.square(H - y))  # 예측값과 실제값의 차이를 제곱해서 평균
# optimizer
# 경사 하강법 (gradient descent) : loss 기울기가 최소화되는 값을 찾기
# 0.01 = learning rate
optimizer = tf.train.GradientDescentOptimizer(0.01)
# loss가 최소화 되도록
train = optimizer.minimize(loss)
# session
sess = tf.Session()

# 그래프에있는 변수초기화
sess.run(tf.global_variables_initializer())

# 4. 학습
# epoch == 학습 횟수
epoch = 5000
for step in range(epoch):
    tmp,loss_val,W_val,b_val = sess.run([train,loss,W,b],feed_dict={x:[1,2,3,4,5],y:[3,5,7,9,11]})
    # train 값은 잘안나옴 -> 잘 안씀 train loss 최소화 값 ==> 결과로 볼거라 괜춘
    if step % 100 == 0:
        print(f'W: {W_val} \t b: {b_val} \t loss: {loss_val}')
# 5. 예측 및 평가
print(sess.run(H,feed_dict={x:[10,11,12,13,14]}))
