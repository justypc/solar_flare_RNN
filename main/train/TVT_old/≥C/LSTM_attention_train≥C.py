import sys
import os

p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(p)

from config.Config import TTFileConfig
from common.train_common.C.LSTM_attention_train_C import LSTM_attention_C_train

file_config = TTFileConfig(p)
LSTM_attention_C_train(p, file_config, 'TT')
