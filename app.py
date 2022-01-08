from dash import Dash, dcc, html, dash_table, Output, Input
from assets import HtmlMaster
from utils import df

# ..

app = Dash(__name__)
htmlObj = HtmlMaster()

app.layout = html.Div(children = [
    html.Div(children = [
        htmlObj.HeaderTitle,
    ]),
    html.Div(children = [
        htmlObj.HeaderDropdownCategory,
        htmlObj.HeaderDropdownIndex,
        # htmlObj.HeaderDropdowns
    ], className="menu"),
    html.Div(children = [
        html.Div(children = [
            dash_table.DataTable(
                id='table',
                style_cell={'textAlign': 'center'},
                # style_cell={'overflow': 'hidden', 'textOverflow': 'ellipsis', 'maxWidth': '50px'},
                style_data={'whiteSpace': 'normal', 'height': 'auto', 'lineHeight': '15px'},
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
                page_size=100 # default = 250
            )
        ], className="card")
    ], className="wrapper")
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8008)

# dcc - graphs, sliders, dropdowns
# dcc.Graph (args) - dict or plotly

# html.Div (args) - children, style, className, id


# dash_table :
# style_cell updates the styling for the data cells & the header cells. 
# To specify header styles, use style_header. 
# To specify data cell styles, use style_data.