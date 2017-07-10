import tensorflow as tf

a=tf.constant(1)
with tf.Session() as sess:
    sess.run(a)
