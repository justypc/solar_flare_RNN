import os
import sys

p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(p)

from common.detect_common.GRU_run import GRU
from config.Config import File202240Config

file_config = File202240Config(p)
GRU(p, file_config, '202240', 'C')