import plotly.graph_objects as go


fig = go.figure(go.indicator(
    mode="guage+number",
    value=65,
    title={'text':"speed"},
    guage{'axis' :{'range' : [0, 100]},
          'bar': {'color': "darlblue"},
          'steps' :[]}
))