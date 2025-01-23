import random
from dash import html, dcc, Input, Output

# Mood data
MOODS = {
    "Happy": {
        "color": "#FFD700",
        "emoji": "😄",
        "quotes": [
            "Happiness is not something ready-made. It comes from your actions.",
            "Be so happy that when others look at you, they become happy too.",
            "Happiness is a warm puppy.",
        ],
    },
    "Sad": {
        "color": "#708090",
        "emoji": "😢",
        "quotes": [
            "Tears come from the heart and not from the brain.",
            "Sadness flies away on the wings of time.",
            "Sometimes, it's okay not to be okay.",
        ],
    },
    "Excited": {
        "color": "#FF4500",
        "emoji": "🤩",
        "quotes": [
            "Excitement is the spark that ignites greatness.",
            "Do more of what makes you excited!",
            "The best way to predict the future is to create it.",
        ],
    },
    "Relaxed": {
        "color": "#87CEEB",
        "emoji": "😌",
        "quotes": [
            "Relax. Breathe. Let go.",
            "Almost everything will work again if you unplug it for a few minutes, including you.",
            "Take time to do what makes your soul happy.",
        ],
    },
}

def get_mood_data(mood):
    mood_data = MOODS[mood]
    random_quote = random.choice(mood_data["quotes"])
    return mood_data["color"], mood_data["emoji"], f'"{random_quote}"'

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

def register_callbacks(app):
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
