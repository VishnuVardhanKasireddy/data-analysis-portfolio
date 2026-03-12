#data audit utility - audit table
import pandas as pd
import numpy as np

def data_audit(df):
    audit=pd.DataFrame()
    audit['Data Type']=df.dtypes
    audit['Missing Values']=df.isnull().sum()
    audit['Unique Values']=df.nunique()
    audit['Percentage Missing']=df.isnull().sum()/len(df)*100
    return audit.sort_values(by='Percentage Missing', ascending=False)