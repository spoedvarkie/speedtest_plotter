import plotly.express as px
import pandas as pd

df = pd.read_csv('results.csv')

fig = px.line(df, x='time', y=['curr_ping', 'curr_upload', 'curr_download', 'avg_ping', 'avg_upload_speed',
                               'avg_download_speed'], title='Speedtest Stats', markers=True)
# fig.add_scatter(x=df['time'], y=df['curr_upload'], name='Upload')
# fig.add_scatter(x=df['time'], y=df['curr_download'], name='Download')
# fig.add_scatter(x=df['time'], y=df['avg_ping'], name='Avg Ping')
# fig.add_scatter(x=df['time'], y=df['avg_upload_speed']/1000000, name='Avg Upload')
# fig.add_scatter(x=df['time'], y=df['avg_download_speed']/1000000, name='Avg Download')

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1y <", step="year", stepmode="backward"),
            dict(count=6, label="6m <", step="month", stepmode="backward"),
            dict(count=1, label="1m <", step="month", stepmode="backward"),
            dict(count=1, label="Now", step="day", stepmode="todate"),
            dict(count=1, label="Now Month", step="month", stepmode="todate"),
            dict(count=1, label="Now Year", step="year", stepmode="todate"),
            dict(step="all")
        ])
    )
)
fig.show()
