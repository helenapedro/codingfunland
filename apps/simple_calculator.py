import dash
from dash import dcc, html, Input, Output, ctx

# Calculator Layout
def calculator_layout():
    return html.Div(
        style={"textAlign": "center", "fontFamily": "Arial, sans-serif", "padding": "50px"},
        children=[
            html.H1("🧮 Simple Calculator", style={"color": "#FF6347", "marginBottom": "20px"}),
            html.Div(
                style={"display": "inline-block", "padding": "20px", "border": "2px solid #FFD700", "borderRadius": "10px"},
                children=[
                    dcc.Input(id="num1", type="number", placeholder="Enter first number",
                              style={"width": "200px", "padding": "10px", "marginRight": "10px", "borderRadius": "5px"}),
                    dcc.Input(id="num2", type="number", placeholder="Enter second number",
                              style={"width": "200px", "padding": "10px", "borderRadius": "5px"}),
                ],
            ),
            html.Div(
                style={"marginTop": "20px"},
                children=[
                    html.Button("➕ Add", id="add-btn", n_clicks=0, style=button_style("#FFD700")),
                    html.Button("➖ Subtract", id="sub-btn", n_clicks=0, style=button_style("#87CEEB")),
                    html.Button("✖️ Multiply", id="mul-btn", n_clicks=0, style=button_style("#FF4500")),
                    html.Button("➗ Divide", id="div-btn", n_clicks=0, style=button_style("#32CD32")),
                ],
            ),
            html.Div(id="result-display", 
                     style={"marginTop": "30px", "fontSize": "24px", "fontWeight": "bold", "color": "#333"}),
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

# Button styling helper function
def button_style(color):
    return {
        "backgroundColor": color,
        "border": "none",
        "color": "white",
        "padding": "10px 20px",
        "margin": "10px",
        "borderRadius": "10px",
        "cursor": "pointer",
        "fontSize": "18px",
    }

# Callback for calculator functionality
def register_calculator_callbacks(app):
    @app.callback(
        Output("result-display", "children"),
        Input("add-btn", "n_clicks"),
        Input("sub-btn", "n_clicks"),
        Input("mul-btn", "n_clicks"),
        Input("div-btn", "n_clicks"),
        [Input("num1", "value"), Input("num2", "value")]
    )
    def update_result(add_clicks, sub_clicks, mul_clicks, div_clicks, num1, num2):
        if num1 is None or num2 is None:
            return "Please enter both numbers!"

        # Determine which button triggered the callback
        triggered_id = ctx.triggered_id

        try:
            if triggered_id == "add-btn":
                return f"Result: {num1} + {num2} = {num1 + num2} 🎉"
            elif triggered_id == "sub-btn":
                return f"Result: {num1} - {num2} = {num1 - num2} 🤔"
            elif triggered_id == "mul-btn":
                return f"Result: {num1} × {num2} = {num1 * num2} 🪄"
            elif triggered_id == "div-btn":
                if num2 == 0:
                    return "Cannot divide by zero! 😵"
                return f"Result: {num1} ÷ {num2} = {num1 / num2:.2f} ➗"
        except Exception as e:
            return f"Error: {str(e)}"

        return "Click a button to calculate!"
