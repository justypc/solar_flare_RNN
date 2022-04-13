import sys
import os

p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(p)

from config.Config import File2022Config
from main.train_common.M.NN_train_M import NN_M_train

file_config = File2022Config(p)
NN_M_train(p, file_config, '2022')
