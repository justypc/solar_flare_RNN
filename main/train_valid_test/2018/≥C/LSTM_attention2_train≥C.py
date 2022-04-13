import sys
import os

p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(p)

from config.Config import File2018Config
from main.train_common.C.LSTM_attention2_train_C import LSTM_attention2_C_train

file_config = File2018Config(p)
LSTM_attention2_C_train(p, file_config, '2018')
