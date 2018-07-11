import os
from urllib.request import urlretrieve

import pandas as pd

#from here: https://data.seattle.gov/Transportation/Fremont-Bridge-Hourly-Bicycle-Counts-by-Month-Octo/65db-xm6k/data
FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL, 
                        force_download=False):
    """Download and cache the fremont data
    
    Parameters
    ----------
    filename : string (optional)
        location to save the data
    url : string (optional)
        web location of the data
    force_download : bool (optional)
        if True, force redownload of data
    
    Returns
    -------
    data : pandas.DataFrame
        The fremont bridge data
    """

    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)

    #Before:
    #data = pd.read_csv('Fremont.csv', index_col='Date', parse_dates=True)
    #make parse string of Date and make it an index

    #After: x20 faster
    # look at http://strftime.org/
    data = pd.read_csv('Fremont.csv', index_col='Date')
    try:
        data.index = pd.to_datetime(data.index, format='%m/%d/%Y %H:%M:%S %p')
    except TypeError:
        data.index = pd.to_datetime(data.index) #infer it automatically takes alot of time x10 at least

    
    data.columns = ['East', 'West']
    data['Total'] = data['West'] + data['East']
    return data