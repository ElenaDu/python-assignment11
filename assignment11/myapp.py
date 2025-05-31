#Task 4: A Dashboard with Dash
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

#Load the gapminder dataset
df = pldata.gapminder(return_type='pandas')

# Remove duplicates from the countries names
countries = sorted(df['country'].unique())

# Initialize Dash app
app = Dash(__name__)
server = app.server

# Layout
app.layout = html.Div([
    html.H1('GDP Per Capita Over Time', style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in countries],
        value='Canada'
    ),
    dcc.Graph(id='gdp-growth')
])

# Callback for dynamic updates
@app.callback(
    Output('gdp-growth', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_graph(country_name):
    # Filter data for the selected country
    filtered_df = df[df['country'] == country_name]
    fig = px.line(
        filtered_df,
        x='year',
        y='gdpPercap',
        title=f'GDP Per Capita Trends in {country_name}',
        labels={'gdpPercap': 'GDP Per Capita', 'year': 'Year'},
        markers=True
        )
    return fig

# Run the app
if __name__ == "__main__": 
    app.run(debug=True) 