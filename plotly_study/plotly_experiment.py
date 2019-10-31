import plotly as py
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

orders = pd.read_excel('/Users/apple/PycharmProjects/qtm385/plotly_study/sales.xls')

with pd.option_context('display.max_rows', 10, 'display.max_columns', 10):  # more options can be specified also
    print(orders.Sales)

plt.plot(orders.Sales)
plt.show()
# x = np.linspace(0,np.pi,1000)
#
# print(x)
#
# layout = go.Layout(
#     title='example',
#     yaxis=dict(
#         title='volts'
#     ),
#     xaxis=dict(
#         title='nanoseconds'
#     )
# )
#
# trace1 = go.Scatter(
#     x=x,
#     y=np.sin(x),
#     mode='lines',
#     name='sin(x)',
#     line = dict(
#         shape='spline'
#     )
# )
#
# fig = go.Figure(data=[trace1],layout=layout)
# py.offline.plot(fig)
