import dash
from dash import dcc, html, Input, Output
from apps.mood_generator.mood import get_mood_data, mood_generator_layout
from apps.color_picker.colors import get_color_data, color_data_layout
from apps.shape_drawing import shape_drawing_layout, register_shape_callbacks
from apps.simple_calculator import calculator_layout, register_calculator_callbacks

# Initialize the app
app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

register_calculator_callbacks(app)
register_shape_callbacks(app)

# Home Page Layout
def homepage_layout():
    return html.Div(
        style={"textAlign": "center", "padding": "50px"},
        children=[
            html.H1("🌟 Welcome to the Coding Fun Land! 🖥", style={"color": "#FF6347", "fontSize": "48px"}),
            html.P(
                "Hi there! My name is Helena, and I guide many kids into the magical world of coding. "
                "We create fun apps, learn cool things, and play with technology like never before. 🚀",
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
                    
                    dcc.Link(
                        html.Button(
                            "Simple Calculator 🧮",
                            style={
                                "width": "100%",
                                "padding": "20px",
                                "fontSize": "18px",
                                "backgroundColor": "#FF4500",
                                "border": "none",
                                "borderRadius": "10px",
                                "cursor": "pointer",
                            },
                        ),
                        href="/simple-calculator",
                    ),
                    
                    dcc.Link(
                        html.Button(
                            "Shape Drawing 🎨",
                            style={
                                "width": "100%",
                                "padding": "20px",
                                "fontSize": "18px",
                                "backgroundColor": "#32CD32",
                                "border": "none",
                                "borderRadius": "10px",
                                "cursor": "pointer",
                            },
                        ),
                        href="/shape-drawing",
                    ),
                ],
            ),
            html.Footer(
                children=[
                    html.P("Connect with me on LinkedIn:"),
                    html.A("Helena Mbeua Pedro", href="https://www.linkedin.com/in/helena-mbeua-pedro/", target="_blank"),
                    html.P("Remember, coding is like a superpower. Use it wisely and have fun! 🦸‍♀️🦸‍♂️"),
                    html.P("P.S. Don't forget to take breaks and eat your veggies! 🥦🥕")
                ],
                style={"marginTop": "50px", "fontSize": "16px", "color": "#333"}
            )
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
        return color_data_layout(app)
    elif pathname == "/simple-calculator":
        return calculator_layout()
    elif pathname == "/shape-drawing":
        return shape_drawing_layout()
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
