import os
import sys

p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(p)

from common.detect_common.NN_run import NN
from config.Config import TTFileConfig

file_config = TTFileConfig(p)
NN(p, file_config, 'TVT', 'M')
