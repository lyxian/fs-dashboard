from dash import Dash, dcc, html, dash_table
from vars import BIZ_CATEGORY
import os

# Dashboard Layout
# ├-Header
# | └-Title
# | └-Dropdown (Category)
# | └-Dropdown (DataIndex)
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
                    for index in range(len(os.listdir('data')))
                ],
                value="0",
                clearable=False,
                searchable=False,
                # className="dropdown",
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
                    for index in range(len(os.listdir('data')))
                ],
                value="0",
                clearable=False,
                searchable=False,
                className="dropdown",
            )
        ], className="menu")