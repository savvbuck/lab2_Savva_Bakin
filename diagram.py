import plotly.graph_objects as go

below_mfive = []
above_mfive = []

with open('sequence.txt') as f:
    for x in f:
        x = float(x)
        if x <= 0:
            if x < -5:
                below_mfive.append(x)
            if x > -5:
                above_mfive.append(x)

labels = ['0 =< x > -5', 'x < -5']
values = [len(above_mfive), len(below_mfive)]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()