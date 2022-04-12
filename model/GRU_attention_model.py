import keras
from keras.models import Sequential
from keras.layers import InputLayer, GRU, Dense, Dropout, BatchNormalization, Activation
from keras.optimizers import Adam
from keras.initializers import glorot_normal
from layer.attention import Attention


def get_GRU_attention_model(time_steps,
                            learning_rate: float,
                            dropout_rate: float,
                            seed: int,
                            score_metrics: list):
    """
    获得编译好的 GRU 前向传播注意力机制 模型
    :param time_steps: 时间步
    :param learning_rate: 学习率
    :param dropout_rate: 神经元失活率
    :param seed: 随机数种子  Glorot正态分布初始化方法和Dropout
    :param score_metrics: 评价指标
    :return: 编译好的 GRU 前向传播注意力机制 模型
    """
    keras.initializers.he_normal(521)
    model = Sequential([
        InputLayer(input_shape=(time_steps, 10)),
        # 第一层LSTM
        GRU(
            units=256,
            kernel_initializer=glorot_normal(seed),
            activation='tanh',
            return_sequences=True
        ),
        Dropout(dropout_rate, seed=seed),
        BatchNormalization(),
        # 第二层Attention
        Attention(step_dim=time_steps),
        # 第三层
        Dense(
            units=128,
            kernel_initializer=glorot_normal(seed),
        ),
        Dropout(dropout_rate, seed=seed),
        BatchNormalization(),
        Activation('relu'),
        # 第四层
        Dense(
            units=64,
            kernel_initializer=glorot_normal(seed)
        ),
        Dropout(dropout_rate, seed=seed),
        BatchNormalization(),
        Activation('relu'),
        # 第五层输出层
        Dense(
            units=2,
            activation='softmax',
            kernel_initializer=glorot_normal(seed)
        ),
    ])
    adam = Adam(learning_rate)
    model.compile(
        optimizer=adam,
        loss='binary_crossentropy',  # 交叉熵
        metrics=score_metrics
    )
    return model
