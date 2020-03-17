#!/user/bin/python3
# -*- coding:utf-8 -*-
# Created by Super He on 2019/3/7

import os
import sys
import json
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import decimal

# Type your code here
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file = pd.read_excel(os.path.join(BASE_DIR, 'circlip\\Latin_TABLE.xlsx'), header=0)
input_x = file[
    ['circlip_thickness', 'delta_outer_radius', 'delta_tooling_diameters', 'inner_diameters', 'tip_type']]
output_y_stress = file[['max_stress']]
output_y_diameters = file[['deformed_diameters']]

def restore_data(data, input_x, output_y, flag):

    input_x = np.asarray(input_x)
    output_y = np.asarray(output_y)

    x_train, x_test, y_train, y_test = train_test_split(input_x, output_y, test_size=1, random_state=65)
    x_test = data
    min_max_scaler_x = preprocessing.MinMaxScaler()
    min_max_scaler_y = preprocessing.MinMaxScaler()
    x_train_norm = min_max_scaler_x.fit_transform(x_train)
    x_test_norm = min_max_scaler_x.transform(x_test)
    y_train_norm = min_max_scaler_y.fit_transform(y_train)
    y_test_norm = min_max_scaler_y.transform(y_test)

    graph = tf.Graph()

    with graph.as_default():
        inputs_ = tf.placeholder(tf.float32, [None, 5], name='inputs')
        outputs_ = tf.placeholder(tf.float32, [None, 1], name='outputs')
        learning_rate_ = tf.placeholder(tf.float32, name='learning_rate')
        dense1 = tf.contrib.layers.fully_connected(inputs_, 256)
        dense_norm1 = tf.layers.batch_normalization(dense1)
        dense2 = tf.contrib.layers.fully_connected(dense_norm1, 256)
        dense_norm2 = tf.layers.batch_normalization(dense2)
        #     dense3 = tf.contrib.layers.fully_connected(dense_norm2,4)
        #     dense_norm3 = tf.layers.batch_normalization(dense3)
        outputs = tf.contrib.layers.fully_connected(dense_norm2, 1, activation_fn=tf.nn.sigmoid)
        saver = tf.train.Saver()

    with tf.Session(graph=graph) as sess:
        # Restore
        restore_path = os.path.join(BASE_DIR, 'circlip/checkpoints_0%s_circlip' %flag)
        saver.restore(sess, tf.train.latest_checkpoint(restore_path))

        feed = {inputs_: x_test_norm}

        pred = sess.run(outputs, feed_dict=feed)
        pred = min_max_scaler_y.inverse_transform(pred)

    # return "{:.2f}".format(float(pred[0]))
    return decimal.Decimal(float(pred[0])).quantize(decimal.Decimal('.01'))

if __name__ == '__main__':
    # x_test = [[3.48, 1.96, 3.85, 29.8, 2]]
    path = r'D:\DjangoWeb\SealingAuto\media'
    file = os.path.join(path, 'parameters.json')
    with open(file) as fp:
        para = json.load(fp)
    fp.close()
    circlip_thichness = para['circlip_thickness']
    inner_diameters = para['circlip_diameters']
    delta_outer_radius = para['circlip_width']
    delta_tooling_diameters = para['tooling_diameters'] - inner_diameters
    tip_type = para['tip_type']
    data = [[circlip_thichness, delta_outer_radius, delta_tooling_diameters, inner_diameters, tip_type]]
    print(data)
    def_diameters = restore_data(data, input_x, output_y_diameters, 7)
    mises = restore_data(data, input_x, output_y_stress, 8)
    print(mises, def_diameters)
    r_para = {'mises': float(mises), 'deformed_diameters': float(def_diameters)}
    json_encoding = json.dumps(r_para, indent=4)
    json_file = open(os.path.join(path, 'results.json'), 'w')
    json_file.write(json_encoding)
    json_file.close()

