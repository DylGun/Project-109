import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff
data1=pd.read_csv("StudentsPerformance.csv")
data2=data1["reading score"].tolist()
mean=statistics.mean(data2)
median=statistics.median(data2)
mode=statistics.mode(data2)
stdev=statistics.stdev(data2)