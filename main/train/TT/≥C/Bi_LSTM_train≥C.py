import os
import sys

p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(p)

from config.Config import TTFileConfig
from common.train_common.C.Bi_LSTM_train_C import Bi_LSTM_C_train

file_config = TTFileConfig(p)
Bi_LSTM_C_train(p, file_config, 'TT')
