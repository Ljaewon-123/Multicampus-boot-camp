import tensorflow as tf
from tensorflow_core.examples.tutorials.mnist import input_data

# 잊어버리랭

# 1.
mnist = input_data.read_data_sets('data/mnist/',one_hot = True)

# print(mnist)
# 2. 가설 설정
# mnist 가로세로 곱? 784
x = tf.placeholder(shape = [None,784],dtype=tf.float32)
y = tf.placeholder(shape=[None,10],dtype=tf.float32)
# 10 숫자종류가 총 10개라
W1 = tf.Variable(tf.random_normal([784,256]),name='weight1')
b1 = tf.Variable(tf.random_normal([256]),name = 'bias1')
layer1 = tf.nn.relu(tf.matmul(x,W1)+b1)

W2 = tf.Variable(tf.random_normal([256,256]),name= 'weigh2')
b2 = tf.Variable(tf.random_normal([256]),name = 'bias2')
layer2 = tf.nn.relu(tf.matmul(layer1,W2)+b2)

W3 = tf.Variable(tf.random_normal([256,10]),name= 'weigh3')
b3 = tf.Variable(tf.random_normal([10]),name = 'bias3')
layer3 = tf.nn.relu(tf.matmul(layer2,W3)+b3)

logit = tf.matmul(layer2,W3)+b3
H = tf.nn.relu(logit)
# 준비
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logit,labels=y))

train = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
# 학습
num_of_epoch = 30 # 학습한번당 100개로 쪼개서 100번 학습이 1번임
batch_size = 100
for step in range(num_of_epoch):
    total_iter = int(mnist.train.num_examples / batch_size)
    for i in range(total_iter):
        batch_x,batch_y = mnist.train.next_batch(batch_size)
        _,loss_val = sess.run([train,loss],feed_dict={x:batch_x,y:batch_y})
        if step % 3 == 0:
            print(f'loss: {loss_val}')
# 5 예
predict = tf.argmax(H,1)
correct = tf.equal(predict,tf.argmax(y,1))
accracy = tf.reduce_mean(tf.cast(correct,dtype=tf.float32))
print(f'acc: {sess.run(accracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})}')
