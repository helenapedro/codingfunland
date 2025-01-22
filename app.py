import dash
from dash import dcc, html

# Initialize the app
app = dash.Dash(__name__)
server = app.server  # Required for deployment

# App layout
app.layout = html.Div(
    style={
        'textAlign': 'center',
        'fontFamily': 'Arial, sans-serif',
        'padding': '50px',
        'backgroundColor': '#F5F5F5',
    },
    children=[
        # Title Section
        html.H1(
            "🌟 Welcome to the Coding Fun Land! 🖥",
            style={
                'color': '#FF6347',
                'fontSize': '48px',
                'marginBottom': '20px',
            },
        ),
        html.P(
            "Hi there! My name is Helena, and I’ll be your guide into the magical world of coding. "
            "We’ll create fun apps, learn cool things, and play with technology like never before. 🚀",
            style={'color': '#333', 'fontSize': '20px', 'marginBottom': '30px'},
        ),
        # Interactive Section for Displaying Apps
        html.Div(
            children=[
                html.H2("🕹 Explore Our Fun Apps!", style={'color': '#4682B4', 'marginBottom': '20px'}),
                html.Div(
                    style={
                        'display': 'grid',
                        'gridTemplateColumns': 'repeat(auto-fit, minmax(200px, 1fr))',
                        'gap': '20px',
                    },
                    children=[
                        html.Div(
                            [
                                html.Button(
                                    "Mood Generator 🎭",
                                    style={
                                        'width': '100%',
                                        'padding': '20px',
                                        'fontSize': '18px',
                                        'backgroundColor': '#87CEEB',
                                        'border': 'none',
                                        'borderRadius': '10px',
                                        'cursor': 'pointer',
                                    },
                                    id='mood-generator-btn',
                                ),
                            ],
                            style={
                                'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)',
                                'borderRadius': '10px',
                                'backgroundColor': '#FFFFFF',
                                'padding': '10px',
                                'textAlign': 'center',
                            },
                        ),
                        html.Div(
                            [
                                html.Button(
                                    "Coming Soon 🚧",
                                    style={
                                        'width': '100%',
                                        'padding': '20px',
                                        'fontSize': '18px',
                                        'backgroundColor': '#FFD700',
                                        'border': 'none',
                                        'borderRadius': '10px',
                                        'cursor': 'not-allowed',
                                    },
                                    disabled=True,
                                ),
                            ],
                            style={
                                'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)',
                                'borderRadius': '10px',
                                'backgroundColor': '#FFFFFF',
                                'padding': '10px',
                                'textAlign': 'center',
                            },
                        ),
                    ],
                ),
            ],
        ),
        # Call-to-Action
        html.Div(
            children=[
                html.Button(
                    "Let's Get Started! 🚀",
                    id='start-btn',
                    style={
                        'marginTop': '40px',
                        'padding': '15px 30px',
                        'fontSize': '20px',
                        'backgroundColor': '#FF4500',
                        'color': 'white',
                        'border': 'none',
                        'borderRadius': '10px',
                        'cursor': 'pointer',
                    },
                ),
            ],
        ),
    ],
)

if __name__ == '__main__':
    app.run_server(debug=True)
