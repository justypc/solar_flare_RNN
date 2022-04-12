import keras
import tensorflow as tf
from keras.models import Sequential
from keras.layers import InputLayer, Bidirectional, GRU, Dense, Dropout, BatchNormalization, Activation
from keras.optimizers import Adam
from keras.initializers import glorot_normal


def get_Bi_GRU_model(time_steps: int,
                     learning_rate: float,
                     dropout_rate: float,
                     seed: int,
                     score_metrics: list):
    """
    获得编译好的双向GRU模型
    :param time_steps: 时间步
    :param learning_rate: 学习率
    :param dropout_rate: 神经元失活率
    :param seed: 随机数种子  Glorot正态分布初始化方法和Dropout
    :param score_metrics: 评价指标
    :return: 编译好的双向GRU模型
    """
    keras.initializers.he_normal(521)
    model = Sequential([
        InputLayer(input_shape=(time_steps, 10)),
        # 第一层Bi-GRU
        Bidirectional(
            GRU(
                units=256,
                kernel_initializer=glorot_normal(seed),
                activation='tanh',
                bias_initializer=tf.zeros_initializer()
            ),
        ),
        Dropout(dropout_rate, seed=seed),
        BatchNormalization(),
        # 第二层
        Dense(
            units=128,
            kernel_initializer=glorot_normal(seed),
            bias_initializer=tf.zeros_initializer()
        ),
        Dropout(dropout_rate, seed=seed),
        BatchNormalization(),
        Activation('relu'),
        # 第三层
        Dense(
            units=64,
            kernel_initializer=glorot_normal(seed),
            bias_initializer=tf.zeros_initializer()
        ),
        Dropout(dropout_rate, seed=seed),
        BatchNormalization(),
        Activation('relu'),
        # 第四层输出层
        Dense(
            units=2,
            activation='softmax',
            kernel_initializer=glorot_normal(seed),
            bias_initializer=tf.zeros_initializer()
        ),
    ])
    adam = Adam(learning_rate)
    model.compile(
        optimizer=adam,
        loss='binary_crossentropy',  # 'categorical_crossentropy',  # 交叉熵
        metrics=score_metrics  # 准确率,
    )
    return model
