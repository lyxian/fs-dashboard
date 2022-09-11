from dash import Dash, dcc, html, dash_table, Output, Input
from assets import HtmlMaster

from utils import filterItemsByCategory, formatFilename, sortItemsByColumn
import json
import os

app = Dash(__name__)
server = app.server
htmlObj = HtmlMaster()

app.layout = html.Div(children = [
    html.Div(children = [
        htmlObj.HeaderTitle,
    ]),
    html.Div(children = [
        htmlObj.HeaderDropdownCategory,
        htmlObj.HeaderDropdownIndex,
        htmlObj.HeaderDropdownColumn,
        htmlObj.HeaderDropdownAscending,
        # htmlObj.HeaderDropdowns
    ], className="menu"),
    html.Div(children = [
        html.Div(children = [
            dash_table.DataTable(
                id='table',
                style_cell={'textAlign': 'center'},
                # style_cell={'overflow': 'hidden', 'textOverflow': 'ellipsis', 'maxWidth': '50px'},
                style_data={'whiteSpace': 'normal', 'height': 'auto', 'lineHeight': '15px'},
                # columns=[{"name": i, "id": i} for i in df.columns],
                # data=df.to_dict('records'),
                page_size=100 # default = 250
            )
        ], className="card")
    ], className="wrapper")
])

@app.callback(
    Output('header-description', 'children'), [Input("index-filter", "value")]
)
def update_description(index):
    folderDir = 'data'
    filename = os.path.join(folderDir, sorted(os.listdir(folderDir))[int(index)])
    
    return formatFilename(filename)

@app.callback(
    [
        Output("table", "data"),
        Output("table", "columns"),
    ],
    [
        Input("category-filter", "value"),
        Input("index-filter", "value"),
        Input("select-column", "value"),
        Input("select-sort", "value")
    ],
)
def update_table(category, index, column, orderBy):
    folderDir = 'data'
    filename = os.path.join(folderDir, sorted(os.listdir(folderDir))[int(index)])
    
    with open(filename, 'r') as file:
        items = json.load(file)

    if not orderBy:
        df = filterItemsByCategory(category, items)
    else:
        df = sortItemsByColumn(category, column, items, orderBy)

    return df.to_dict('records'), [{"name": i, "id": i} for i in df.columns]

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=os.getenv('PORT', 8008))
