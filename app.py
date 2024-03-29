from dash import html
import dash_bootstrap_components as dbc
from menu import menu_row
from create_app import app


# for Heroku deployment
server = app.server

app.title = "Wildlife Image Classifier"
app.layout = dbc.Container([
    html.Br(),
    # ---- Header and description ----
    dbc.Row([
        html.Div(
            style={
                "display":"flex", 
                "alignItems":"center"
            },
            children=[
                html.Button(
                    "WILDLIFE IMAGE CLASSIFIER",
                    id="btn_home",
                    className="btn_home"
                )
            ]
        ),
        html.Hr(),
        html.H3("Discover the wildlife of Africa")
    ]),
    dbc.Row(
        className="g-0",
        justify="center",
        children=[
            html.Div(
                className="section_div",
                children=[
                    # ---- Menu ----
                    menu_row,
                    # ---- Contents ----
                    html.Div(
                        id="div_contents",
                        className="contents_div",
                        children=[]
                    )
                ]
            )
        ]
    ),
    html.Br()
])


if __name__ == "__main__":
    app.run_server(debug=True, port=3838)