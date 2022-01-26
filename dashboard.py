import dash
from pandas import read_csv
from numpy import nan
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

app = dash.Dash()
df = read_csv('C:/Users/bhara/Environments/boss/overall.csv')

df = df.sample(random_state = 259, n = 100)


del df["Unnamed: 0"]

df['year'] = df['term'].apply(lambda x: x[0:7])
df['term'] = df['term'].apply(lambda x: x[8:])
df["before_process_vacancy"].replace(0, nan, inplace = True)
df.dropna(inplace = True)



def bid_prices():
    # Function for creating line chart showing bid prices over time
    fig = make_subplots(rows = 2, cols = 1) 
    
    fig.add_trace(
        go.Scatter(x = df['year'], y = df['median_bid'], marker = dict(color = 'firebrick'), name = 'Median Bid'),
        row = 1, col = 1
    )

    fig.add_scatter(x = df['year'], y = df['min_bid'], marker = dict(color = 'MediumPurple'), name = 'Min Bid', row = 1, col = 1)

    fig.add_bar(x = df['year'], y = df['before_process_vacancy'], name = 'Before Process Vacancy', row = 2, col = 1)

    fig.add_bar(x = df['year'], y = df['after_process_vacancy'], name = 'After Process Vacancy', row = 2, col =1)
    
    fig.update_layout(title = 'Bid Prices over Time',
                      xaxis_title = 'Years',
                      yaxis_title = 'Bids'
                      )
    return fig


app.layout = dash.html.Div(id = 'parent', children = [
    dash.html.H1(id = 'H1', children = 'Boss Bids Analysis', style =  {'textAlign': 'center', 'marginTop': 40, 'marginBottom':40}),

    dash.dcc.Graph(id = 'line_plot', figure = bid_prices())

])

if __name__ == '__main__': 
    app.run_server()

go.Figure()