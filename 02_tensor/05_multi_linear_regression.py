import tensorflow as tf



# 1. 데이터 준비
# x_data : 3번의 쪽지시험 결과 / y_data : 실제 평가 결과
x_data = [
    [73,80,75],
    [93,88,93],
    [89,91,90],
    [96,89,100],
    [73,66,70],
]
y_data = [
    [80],
    [91],
    [88],
    [94],
    [61],
]
# shape=[None,3] -> 몇개가 나오든 리스트 안에는 3개의 값이 있어야함
# shape 이 None : 갯수 상관 없음
x = tf.placeholder(shape=[None,3],dtype=tf.float32)
y = tf.placeholder(shape=[None,1],dtype=tf.float32)
# 2. 가설 설정
# [3,1] -> x와 행렬연산 해야 하기 때문!
W = tf.Variable(tf.random_normal([3,1]),name='weight') # x랑 곱해줘야함 x형태는? 행렬곱 n,3 * 3,1
b = tf.Variable(tf.random_normal([1]),name='bias')  # 상수니까 숫자 1개

# H = W * x + b
H = tf.matmul(x,W) + b

# 3. 준비
# loss function
loss = tf.reduce_mean(tf.square(H - y))
# optimizier
learning_rate = 0.00004   # nan 이 계속 나온다면 발산중
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train = optimizer.minimize(loss)
# session
sess = tf.Session()
sess.run(tf.global_variables_initializer()) # 변수 초기화? W,b 초기화임


# 4. 학습
epochs = 10000
for step in range(epochs):
    _,loss_val,W_val,b_val = sess.run([train,loss,W,b],feed_dict={x:x_data,y:y_data})
    if step % 100 == 0:
        print(f'W: {W_val} \t b: {b_val} \t loss: {loss_val}')
# 5. 예측 및 평가
print(sess.run(H,feed_dict={x:[[100,80,87]]}))