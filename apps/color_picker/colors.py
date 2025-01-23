from dash import html, dcc, Input, Output

def get_color_data(selected_color):
    return {
        'backgroundColor': selected_color,
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
    }
    
def color_data_layout(app):
    # Color Picker Layout
    layout = html.Div(
        style={'textAlign': 'center', 'fontFamily': 'Arial', 'padding': '50px'},
        children=[
            html.H1("Pick a Color 🎨", style={'marginBottom': '30px'}),
            dcc.Dropdown(
                id='color-picker',
                options=[
                    {'label': 'Red', 'value': 'red'},
                    {'label': 'Green', 'value': 'green'},
                    {'label': 'Blue', 'value': 'blue'},
                    {'label': 'Purple', 'value': 'purple'},
                    {'label': 'Orange', 'value': 'orange'},
                    {'label': 'Yellow', 'value': 'yellow'},
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

    # Color Picker Callbacks
    @app.callback(
        Output('color-display', 'style'),
        [Input('color-picker', 'value')]
    )
    def update_background(selected_color):
        return get_color_data(selected_color)

    return layout
