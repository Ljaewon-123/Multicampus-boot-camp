import tensorflow as tf

# print(tf.__version__)
# 상수 노드
node = tf.constant(100)
# tf.constant()는 변수 선언할 때 사용합니다.
# 괄호 안에는 value, dtype, shape, name이 들어갑니다.
#
# tf.Variable과 차이점은 변경이 되지 않는다는 것입니다.
#
# value는 상수나 배열 형태가 들어갈 수 있습니다.

# session : 그래프를 실행시켜주는 역할(runner)
sess = tf.Session()

print(sess.run(node))


'''
tensorflow
-Tensor     : 데이터 저장 객체(placeholder)
-Variable   : Weight, bias 
-Operation  : H = W * X + b (node, 식) -> 그래프 (tensor -> operation -> tensor -> operation -> ...)
-Session    : 그래프 실행 환경 
'''