import tensorflow as tf

x = tf.Variable(2, name='x', dtype=tf.float32)
log_x = tf.log(x)
y = tf.square(log_x) + 1

optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(y)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for step in range(10):
        x_val, y_val = sess.run([x, y])
        print('x: {}, y: {}'.format(x_val, y_val))
        sess.run(train)
