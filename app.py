import dash
from dash import dcc, html, Input, Output
from mood_generator.mood import MOODS, get_mood_data  # Import the mood logic
from color_picker.colors import get_color_data  # Import the color logic

# Initialize the app
app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server  # Required for deployment

# Home Page Layout
def homepage_layout():
    return html.Div(
        style={"textAlign": "center", "padding": "50px"},
        children=[
            html.H1("🌟 Welcome to the Coding Fun Land! 🖥", style={"color": "#FF6347", "fontSize": "48px"}),
            html.P(
                "Hi there! My name is Helena, and I’ll be your guide into the magical world of coding. "
                "We’ll create fun apps, learn cool things, and play with technology like never before. 🚀",
                style={"color": "#333", "fontSize": "20px", "marginBottom": "30px"},
            ),
            html.H2("🕹 Explore Our Fun Apps!", style={"color": "#4682B4", "marginBottom": "20px"}),
            html.Div(
                style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "20px", "marginBottom": "50px"},
                children=[
                    dcc.Link(
                        html.Button(
                            "Mood Generator 🎭",
                            style={
                                "width": "100%",
                                "padding": "20px",
                                "fontSize": "18px",
                                "backgroundColor": "#87CEEB",
                                "border": "none",
                                "borderRadius": "10px",
                                "cursor": "pointer",
                            },
                        ),
                        href="/mood-generator",
                    ),
                    dcc.Link(
                        html.Button(
                            "Color Picker 🎨",
                            style={
                                "width": "100%",
                                "padding": "20px",
                                "fontSize": "18px",
                                "backgroundColor": "#FFD700",
                                "border": "none",
                                "borderRadius": "10px",
                                "cursor": "pointer",
                            },
                        ),
                        href="/color-picker",
                    ),
                ],
            ),
        ],
    )

# Mood Generator Layout
def mood_generator_layout():
    return html.Div(
        style={"padding": "20px"},
        children=[
            html.H1("🎭 Mood Generator", style={"color": "#4682B4"}),
            dcc.Dropdown(
                id="mood-picker",
                options=[{"label": mood, "value": mood} for mood in MOODS.keys()],
                value="Happy",
                style={"width": "50%", "margin": "0 auto", "padding": "10px"},
            ),
            html.Div(id="mood-emoji", style={"fontSize": "80px", "marginTop": "20px"}),
            html.Div(id="mood-quote", style={"marginTop": "30px", "fontSize": "24px", "fontStyle": "italic"}),
            html.Div(
                id="mood-display",
                style={
                    "marginTop": "50px",
                    "height": "200px",
                    "borderRadius": "10px",
                    "display": "flex",
                    "justifyContent": "center",
                    "alignItems": "center",
                    "color": "white",
                    "fontSize": "20px",
                    "fontWeight": "bold",
                    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)",
                    "transition": "background-color 1s ease",
                },
            ),
            dcc.Link(
                html.Button(
                    "Back to Home 🏠",
                    style={
                        "marginTop": "30px",
                        "padding": "10px 20px",
                        "fontSize": "18px",
                        "backgroundColor": "#FF6347",
                        "color": "white",
                        "border": "none",
                        "borderRadius": "10px",
                        "cursor": "pointer",
                    },
                ),
                href="/",
            ),
        ],
    )

# Color Picker Layout
def color_picker_layout():
    return html.Div(
        style={'textAlign': 'center', 'fontFamily': 'Arial', 'padding': '50px'},
        children=[
            html.H1("Selecione uma Cor 🎨", style={'marginBottom': '30px'}),
            dcc.Dropdown(
                id='color-picker',
                options=[
                    {'label': 'Vermelho', 'value': 'red'},
                    {'label': 'Verde', 'value': 'green'},
                    {'label': 'Azul', 'value': 'blue'},
                    {'label': 'Roxo', 'value': 'purple'},
                    {'label': 'Laranja', 'value': 'orange'},
                    {'label': 'Amarelo', 'value': 'yellow'},
                ],
                value='red',
                style={'width': '50%', 'margin': '0 auto', 'padding': '10px'}
            ),
            html.Div(
                id='color-display',
                style={
                    'marginTop': '50px',
                    'height': '200px',
                    'borderRadius': '10px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'color': 'white',
                    'fontSize': '20px',
                    'fontWeight': 'bold',
                    'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)',
                },
            ),
            dcc.Link(
                html.Button(
                    "Back to Home 🏠",
                    style={
                        "marginTop": "30px",
                        "padding": "10px 20px",
                        "fontSize": "18px",
                        "backgroundColor": "#FF6347",
                        "color": "white",
                        "border": "none",
                        "borderRadius": "10px",
                        "cursor": "pointer",
                    },
                ),
                href="/",
            ),
        ],
    )

# Main App Layout
app.layout = html.Div(
    children=[
        dcc.Location(id="url", refresh=False),
        html.Div(id="page-content"),
    ]
)

# Update page-content based on URL
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/mood-generator":
        return mood_generator_layout()
    elif pathname == "/color-picker":
        return color_picker_layout()
    return homepage_layout()

# Mood Generator Callbacks
@app.callback(
    [Output("mood-display", "style"), Output("mood-emoji", "children"), Output("mood-quote", "children")],
    [Input("mood-picker", "value")],
)
def update_mood(mood):
    color, emoji, quote = get_mood_data(mood)
    return (
        {
            "backgroundColor": color,
            "marginTop": "50px",
            "height": "200px",
            "borderRadius": "10px",
            "display": "flex",
            "justifyContent": "center",
            "alignItems": "center",
            "color": "white",
            "fontSize": "20px",
            "fontWeight": "bold",
            "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)",
            "transition": "background-color 1s ease",
        },
        emoji,
        quote,
    )

# Color Picker Callbacks
@app.callback(
    Output('color-display', 'style'),
    [Input('color-picker', 'value')]
)
def update_background(selected_color):
    return get_color_data(selected_color)

if __name__ == '__main__':
    app.run_server(debug=True)
