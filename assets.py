from dash import Dash, dcc, html, dash_table, Input, Output
from vars import BIZ_CATEGORY, SORT_COLUMNS
from utils import searchData

# Dashboard Layout
# ├-Header
# | └-Title
# | └-Dropdown (Category)
# | └-Dropdown (DataIndex)
# | └-Dropdown (ColumnSort)
# └-Table (by Category)

class HtmlMaster():

    def __init__(self):
        pass

    @property
    def HeaderTitle(self):
        return html.Div(children=[
            html.P(children="🎮🎲", className="header-emoji"),
            html.H1(
                children="Lazada Flash Sale Data", className="header-title"
            ),
            html.P(
                id='header-description',
                # children=f"@ {name}",
                className="header-description",
            ),
        ], className="header")

    @property
    def HeaderDropdownCategory(self):
        return html.Div(children=[
            html.Div(children="Category", className="menu-title"),
            dcc.Dropdown(
                id="category-filter",
                options=[
                    {"label": category, "value": category}
                    for category in BIZ_CATEGORY.values()
                ],
                value="Electronics & Appliances",
                clearable=False,
                className="dropdown",
            ),
        ])

    @property
    def HeaderDropdownIndex(self):
        return html.Div(children=[
            html.Div(children="Index", className="menu-title"),
            dcc.Dropdown(
                id="index-filter",
                options=[
                    {"label": index, "value": index}
                    for index in range(len(searchData()))
                ],
                value="0",
                clearable=False,
                searchable=False,
                # className="dropdown",
            ),
        ])

    @property
    def HeaderDropdownColumn(self):
        return html.Div(children=[
            html.Div(children="Sort By", className="menu-title"),
            dcc.Dropdown(
                id="select-column",
                options=[
                    {"label": column, "value": column}
                    for column in SORT_COLUMNS
                ],
                value="itemTitle",
                clearable=False,
                searchable=False,
                className="dropdown-1",
            ),
        ])

    @property
    def HeaderDropdownAscending(self):
        return html.Div(children=[
            html.Div(children="Order By", className="menu-title"),
            dcc.Dropdown(
                id="select-sort",
                options=[
                    {"label": val, "value": val}
                    for val in ['Ascending', 'Descending']
                ],
                value='True',
                searchable=False,
                className="dropdown-1",
            ),
        ])

    @property
    def HeaderDropdowns(self):
        return html.Div(children=[
            html.Div(children="Category", className="menu-title"),
            dcc.Dropdown(
                id="category-filter",
                options=[
                    {"label": category, "value": category}
                    for category in BIZ_CATEGORY.values()
                ],
                value="Electronics & Appliances",
                clearable=False,
                className="dropdown",
            ),
            html.Div(children="Index", className="menu-title"),
            dcc.Dropdown(
                id="index-filter",
                options=[
                    {"label": index, "value": index}
                    for index in range(len(searchData()))
                ],
                value="0",
                clearable=False,
                searchable=False,
                className="dropdown",
            )
        ], className="menu")

class CallbackMaster():
    
    def __init__(self, app):
        self.app = app
        pass
