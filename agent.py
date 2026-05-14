import torch 
import numpy as np
import random 
from game import SnakeGameAI, Direction, Point
from collections import deque

MAX_MEMORY=100_000
BATCH_SIZE=1000
LR=0.001


