from dash import Dash, html, Input, Output, dash_table
import pandas as pd


df = pd.read_csv("Occupations.csv") # replace with your own data source
print(df.head())
print(df.columns)

app = Dash(__name__)


app.layout = html.Div([
    html.H4('Occupations in NZ'),
    html.P(id='table_out'),
    
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i}
                 for i in df.columns],
        data=df.to_dict('records'),
        style_cell={
                "textAlign": "left",
            },
        style_header={
                "backgroundColor": "#1D4ED8",
                "color": "white",
                "fontWeight": "bold",
                "padding": "14px",
                "border": "1px solid #1D4ED8",
            },
        style_data={
                "backgroundColor": "#DBEAFE",
            },
    ),
])

@app.callback(
    Output('table_out', 'children'),
    Input('table', 'active_cell'))
def update_graphs(active_cell):
    if active_cell:
        cell_data = df.iloc[active_cell['row']][active_cell['column_id']]
        return f"Data: \"{cell_data}\" from table cell: {active_cell}"
    return "Click the table"
app.run(debug=True)