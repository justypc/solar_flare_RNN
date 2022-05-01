import os
import sys

from common.detect_common.run import *

p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(p)

from config.Config import File202240Config

file_config = File202240Config(p)
# NN(p, file_config, '202240', 'M', 'same')

LSTM(p, file_config, '202240', 'M', 'same')
LSTM_Att(p, file_config, '202240', 'M', 'same')
# LSTM_Att2(p, file_config, '202240', 'M', 'same')

BLSTM(p, file_config, '202240', 'M', 'same')
BLSTM_Att(p, file_config, '202240', 'M', 'same')
# BLSTM_Att2(p, file_config, '202240', 'M', 'same')

GRU(p, file_config, '202240', 'M', 'same')
GRU_Att(p, file_config, '202240', 'M', 'same')
# GRU_Att2(p, file_config, '202240', 'M', 'same')

BGRU(p, file_config, '202240', 'M', 'same')
BGRU_Att(p, file_config, '202240', 'M', 'same')
# BGRU_Att2(p, file_config, '202240', 'M', 'same')
