import pytest
import sys
import os
sys.path.append(os.path.abspath('..'))
from src import plot_hist
import matplotlib
import pandas as pd

def test_plot_hist():
    df = pd.DataFrame({'a': [1,2,4], 'b': [3, 4, 5]})
    assert type(plot_hist(df, 'a')) == matplotlib.axes.Axes