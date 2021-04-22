import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_profiling import ProfileReport
import sweetviz as sw

df = pd.read_csv("G:/data source/201601-citibike-tripdata/201601-citibike-tripdata.csv",
                 parse_dates=["starttime", "stoptime"], infer_datetime_format=True, index_col=["starttime", "stoptime"])
raw_nrow = len(df)

df = df.drop(df[df.tripduration > 3600].index)
less_than_1_hour_nrow = len(df)

# Configure Output to display all columns
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',17)

# Take a look at df
print(df)
print(df.columns)

print(df.describe())
print(df.info())

# EDA using Sweetviz
#report_general = sw.analyze(df)
#report_general.show_html('report_general.html')

# EDA take-away
# column "usertype", "gender", "birth year"
# are for marketing purpose analysis, for this cost-reduction analysis we will not use them
# "bikeid" can provide a metric of analysis
# "start station id" and "end station id" have almost identical distribution, this means bikes are mainly used
# for round-trip, this is valuable info to cost-reduction, should dig down in this direction
# "end station lon/lag" distribution does make sense, check with data source manager.
# "tripduration" there are outliers, need to manipulate data
# focus analysis on the relation between "starttime" and  "start station id", at the same time,
# "stoptime" and "end station id"

# check "tripduration" outliers
#print(df.sort_values(["tripduration"], ascending=False).head(100))
#df = df.apply(lambda x: True if x["tripduration"] > 86400 else False, axis=1)
#print(len(df[df == True].index)/len(df))

#outliers are less than 0.05% of number of records, delete them and EDA again

#finaly decide to use only less than 1 hour data, percentage to raw data
print('less than 1 hour trips: ',less_than_1_hour_nrow)
print('total trip: ',raw_nrow)
print('ratio (less than 1 hour trips to total): ', less_than_1_hour_nrow/raw_nrow)
#this also improve "end station lon/lag" distribution grap, which makes sense

#find out unique combinations of start station id and end station id and count it
df_1 = df.groupby(['start station id','end station id']).size().reset_index().rename(columns={0:'count'})

print(df_1.sort_values(by=['count'], ascending=False))
print(df_1.columns)

print(df_1.describe())
print(df_1.info())