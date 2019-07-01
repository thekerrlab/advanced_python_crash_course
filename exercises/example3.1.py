torun = [
'matplotlib',
'bokeh',
'altair',
'plotnine',
'plotly'
]

if 'matplotlib' in torun:
    import pylab as pl
    pl.plot([1,4,3,2,5,8])
    pl.title('Simple example')
    pl.xlabel('x')
    pl.ylabel('y')

if 'bokeh' in torun:
    import bokeh.plotting as bop
    p = bop.figure(title="Simple example", x_axis_label='x', y_axis_label='y')
    p.line(x=range(6), y=[1,4,3,2,5,8])
    bop.show(p)

if 'altair' in torun:
    import altair as alt
    import pandas as pd
    data = pd.DataFrame({'x': range(6), 'y': [1,4,3,2,5,8]})
    alt.Chart(data).mark_line().encode(x='x', y='y').interactive()

if 'plotnine' in torun:
    import plotnine as pn
    import pandas as pd
    data = pd.DataFrame({'x': range(6), 'y': [1,4,3,2,5,8]})
    pn.ggplot(data) + pn.geoms.geom_line()

if 'plotly' in torun:
    import plotly as ply
    data = ply.graph_objs.Scatter(x=list(range(6)), y=[1,4,3,2,5,8])
    ply.offline.plot({'data':[data]}, auto_open=True)