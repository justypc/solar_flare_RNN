import os
import sys

p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(p)

from config.Config import File202240Config
from common.train_common.C.GRU_attention_train_C import GRU_attention_C_train

file_config = File202240Config(p)
GRU_attention_C_train(p, file_config, '202240')
