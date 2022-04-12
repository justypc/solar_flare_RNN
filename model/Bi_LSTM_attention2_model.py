from tensorflow import keras
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer, Bidirectional, LSTM, Dense, Dropout, BatchNormalization, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.initializers import glorot_normal
from layer.attention2 import Attention
from common import common_NN


def get_Bi_LSTM_attention_model(time_steps,
                                learning_rate: float,
                                dropout_rate: float,
                                seed: int,
                                score_metrics: list):
    """
    获得编译好的 双向lstm 多对一注意力机制 模型
    :param time_steps: 时间步
    :param learning_rate: 学习率
    :param dropout_rate: 神经元失活率
    :param seed: 随机数种子  Glorot正态分布初始化方法和Dropout
    :param score_metrics: 评价指标
    :return: 编译好的 双向lstm 多对一注意力机制 模型
    """
    keras.initializers.he_normal(521)
    model = Sequential(
        [
            InputLayer(input_shape=(time_steps, 10)),
            # 第一层Bi-LSTM
            Bidirectional(
                LSTM(
                    units=256,
                    kernel_initializer=glorot_normal(seed),
                    activation='tanh',
                    return_sequences=True,
                    bias_initializer=tf.zeros_initializer()
                ),
            ),
            Dropout(dropout_rate, seed=seed),
            BatchNormalization(),
            # 第二层Attention
            Attention(),
        ].append(common_NN(dropout_rate, seed)))
    adam = Adam(learning_rate)
    model.compile(
        optimizer=adam,
        loss='binary_crossentropy',  # 'categorical_crossentropy',  # 交叉熵
        metrics=score_metrics  # 准确率,
    )
    return model
