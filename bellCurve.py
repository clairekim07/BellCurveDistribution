import pandas as panda
import csv
import plotly.figure_factory as ff

df = panda.read_csv("rating.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Rating"], show_hist=False)
fig.show()