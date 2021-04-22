import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_profiling import ProfileReport
import sweetviz as sw

%timeit pd.read_csv("G:/Python R/coop/w51 KNN, Decision Tree/201601-citibike-tripdata/201601-citibike-tripdata.csv",
                 parse_dates=["starttime","stoptime"], infer_datetime_format=True)

# Configure Output to display all columns
# desired_width = 320
# pd.set_option('display.width', desired_width)
# pd.set_option('display.max_columns',17)
#
# # Take a look at df
# print(df)
# print(df.columns)
#
# print(df.describe())
# print(df.info())
#
# print(df["starttime"].dt.hour)