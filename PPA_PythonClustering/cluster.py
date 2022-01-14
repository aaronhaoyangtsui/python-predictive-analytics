import numpy as pd
import pandas as pd
import sklearn
from sklearn.cluster import Birch
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import scale

import sklearn.metrics as sm
from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report

import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\aaron\Desktop\CICS397A\HW3\data.csv")

BirchC = sklearn.cluster.Birch(df, 1, 50, 3, True)

print(BirchC)

