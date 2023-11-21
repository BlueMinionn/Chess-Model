!pip install kaggle -q
mport pandas as pd
import numpy as np
import random
import re
import chess
import torch
import gc
from torch import nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, IterableDataset, random_split
import pandas as pd
import torch
from sklearn.model_selection import train_test_split