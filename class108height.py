import plotly.figure_factory as ff
import pandas as pd
import csv 

data = pd.read_csv("data.csv")
fig = ff.create_distplot([data["Height(Inches)"].tolist()],["height"],show_hist=False)

fig.show()


