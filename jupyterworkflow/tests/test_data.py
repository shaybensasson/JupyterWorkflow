from jupyterworkflow.data import get_fremont_data
import numpy as np
import pandas as pd

def test_fremont_data():
	data = get_fremont_data()
	assert all(data.columns == ["East", "West", "Total"])
	assert isinstance(data.index, pd.DatetimeIndex)
	assert len(np.unique(data.index.time)) == 24