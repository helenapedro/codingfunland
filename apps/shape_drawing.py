import dash
from dash import dcc, html, Input, Output
import dash_daq as daq

# Shape Drawing Layout
def shape_drawing_layout():
    return html.Div(
        style={"textAlign": "center", "fontFamily": "Arial, sans-serif", "padding": "50px"},
        children=[
            html.H1("🎨 Shape Drawing App", style={"color": "#FF6347", "marginBottom": "20px"}),
            html.P("Select a shape, size, and color, and watch it come to life!", 
                   style={"fontSize": "18px", "color": "#555", "marginBottom": "30px"}),

            # Shape selection dropdown
            html.Div([
                html.Label("Select a Shape:", style={"fontSize": "16px", "marginRight": "10px"}),
                dcc.Dropdown(
                    id="shape-selector",
                    options=[
                        {"label": "Circle", "value": "circle"},
                        {"label": "Square", "value": "square"},
                        {"label": "Triangle", "value": "triangle"},
                    ],
                    value="circle",
                    style={"width": "200px", "display": "inline-block"}
                ),
            ], style={"marginBottom": "20px"}),

            # Size slider
            html.Div([
                html.Label("Adjust Size:", style={"fontSize": "16px", "marginRight": "10px"}),
                daq.Slider(
                    id="size-slider",
                    min=50,
                    max=300,
                    value=100,
                    step=10,
                    handleLabel={"showCurrentValue": True, "label": "px"},
                    marks={
                        50: "50px",
                        150: "150px",
                        300: "300px"
                    },
                ),
            ], style={"marginBottom": "20px", "textAlign": "center"}),

            # Color picker
            html.Div([
                html.Label("Pick a Color:", style={"fontSize": "16px", "marginRight": "10px"}),
                dcc.Input(id="color-picker", type="color", value="#FF6347", 
                          style={"width": "50px", "height": "30px", "border": "none"}),
            ], style={"marginBottom": "30px"}),

            # Shape preview area
            html.Div(id="shape-preview", 
                     style={"margin": "0 auto", "height": "350px", "border": "1px solid #ddd", "borderRadius": "10px", 
                            "display": "flex", "alignItems": "center", "justifyContent": "center", "backgroundColor": "#f9f9f9"}),

            # Back to Home button
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

# Shape Drawing Callbacks
def register_shape_callbacks(app):
    @app.callback(
        Output("shape-preview", "children"),
        [Input("shape-selector", "value"), Input("size-slider", "value"), Input("color-picker", "value")],
    )
    def update_shape_preview(shape, size, color):
        # Create the shape based on the selection
        if shape == "circle":
            return html.Div(
                style={
                    "width": f"{size}px",
                    "height": f"{size}px",
                    "borderRadius": "50%",
                    "backgroundColor": color,
                }
            )
        elif shape == "square":
            return html.Div(
                style={
                    "width": f"{size}px",
                    "height": f"{size}px",
                    "backgroundColor": color,
                }
            )
        elif shape == "triangle":
            return html.Div(
                style={
                    "width": "0",
                    "height": "0",
                    "borderLeft": f"{size / 2}px solid transparent",
                    "borderRight": f"{size / 2}px solid transparent",
                    "borderBottom": f"{size}px solid {color}",
                }
            )
        return html.Div("Select a shape to preview.", style={"color": "#888"})
