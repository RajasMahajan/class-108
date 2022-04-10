import plotly.figure_factory as ff
import pandas as pd
import csv

dataone = pd.read_csv("data.csv")

fig = ff.create_distplot([dataone["Weight(Pounds)"].tolist()],["Weight"], show_hist= False)
fig.show()