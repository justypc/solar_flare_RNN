import os
import sys

p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(p)

from config.Config import TVTFileConfig
from common.train_common.M.NN_train_M import NN_M_train

file_config = TVTFileConfig(p)
NN_M_train(p, file_config, 'TVT')
