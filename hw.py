import csv
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import random
import plotly.graph_objects as go
import statistics

df = pd.read_csv("data1.csv") 
data = df["average"].tolist()
mean = sum(data)/len(data)
median = statistics.median(data)
mode = statistics.mode(data)
std = statistics.stdev(data)
first_std_start,first_std_end = mean-std,mean+std
second_std_start,second_std_end = mean-(std*2),mean+(std*2)
third_std_start,third_std_end = mean-(std*3),mean+(std*3)
#fig = px.bar(x = df["Weight(Pounds)"].tolist(),y = df["Index"].tolist())
fig1 = ff.create_distplot([df["average"].tolist()],["average"],show_hist = False) 
fig1.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean"))
fig1.add_trace(go.Scatter(x = [first_std_start,first_std_start],y = [0,0.17],mode = "lines",name = "first standard deviation"))
fig1.add_trace(go.Scatter(x = [first_std_end,first_std_end],y = [0,0.17],mode = "lines",name = "first standard deviation end"))
fig1.add_trace(go.Scatter(x = [second_std_start,second_std_start],y = [0,0.17],mode = "lines",name = "second standard deviation"))
fig1.add_trace(go.Scatter(x = [second_std_end,second_std_end],y = [0,0.17],mode = "lines",name = "second standard deviation end"))
fig1.add_trace(go.Scatter(x = [third_std_start,third_std_start],y = [0,0.17],mode = "lines",name = "third standard deviation"))
fig1.add_trace(go.Scatter(x = [third_std_end,third_std_end],y = [0,0.17],mode = "lines",name = "third standard deviation end"))
#fig.show()
fig1.show()
datawithinfirststandarddeviation = [result for result in data if result >first_std_start and result<first_std_end]
print("f{}% of data lies within first standard deviation",format(len(datawithinfirststandarddeviation)*100.0/len(data)))
datawithinsecondstandarddeviation = [result for result in data if result >second_std_start and result<second_std_end]
print("f{}% of data lies within second standard deviation",format(len(datawithinsecondstandarddeviation)*100.0/len(data)))
datawithinthirdstandarddeviation = [result for result in data if result >third_std_start and result<third_std_end]
print("f{}% of data lies within third standard deviation",format(len(datawithinthirdstandarddeviation)*100.0/len(data)))