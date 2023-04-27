import tensorflow as tf

# 1. 데이터준비
# 4번의 쪽지시험 -> 상,중,하
x_data = [
    [10,7,8,3],
    [8,8,9,4],
    [7,8,2,3],
    [6,3,9,3],
    [7,6,7,5],
    [3,5,6,2],
    [2,4,3,1],
]
y_data = [
    [1,0,0],
    [1,0,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,0,1],
    [0,0,1],
]
x = tf.placeholder(shape=[None,4],dtype=tf.float32)
y = tf.placeholder(shape=[None,3],dtype=tf.float32)

# 로지스틱 회귀를 통해 2개의 선택지 중에서 1개를 고르는 이진 분류(Binary Classification)를
#   3개 이상의 선택지 중에서 1개를 고르는 다중 클래스 분류 문제를 위한 소프트맥스 회귀(Softmax Regression)에 대해서 배웁니다.

# 2. 가설 설정
W = tf.Variable(tf.random_normal([4,3]),name='weight') # 결과가 상,중,하 라서
b = tf.Variable(tf.random_normal([3]),name = 'bias')

logit = tf.matmul(x,W) + b
H = tf.nn.softmax(logit)  # 개수마다 확률 구할때 
# 3. 준비
# loss function
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logit,labels=y))
# optimizier
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)


# session
sess = tf.Session()
sess.run(tf.global_variables_initializer())
# 4. 학습
for step in range(3000):
    _,cost_val = sess.run([train,loss],feed_dict={x:x_data,y:y_data})
    if step % 300 == 0:
        print(f'cost:{cost_val}')


# 5. 예측 평가
print(sess.run(H,feed_dict={x:[[4,9,8,5]]})) # 0.9 확률로 하