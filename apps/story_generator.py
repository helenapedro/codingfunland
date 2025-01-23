import random
from dash import html, dcc, Input, Output

# Story data
STORY_ELEMENTS = {
    "Character": [
        "A brave knight 🏰",
        "A mischievous wizard 🧙‍♂️",
        "A curious cat 🐱",
        "A smart alien 👽",
        "A magical fairy 🧚‍♀️"
    ],
    "Setting": [
        "in a magical forest 🌲",
        "on a distant planet 🌌",
        "in a haunted castle 🏰",
        "in a cozy little village 🏡",
        "under the sea 🌊"
    ],
    "Plot": [
        "looking for treasure 💰",
        "trying to save the kingdom 👑",
        "going on a fun adventure 🏃‍♀️",
        "discovering new friends 👫",
        "fighting a dragon 🐉"
    ]
}

def get_story_data(character, setting, plot):
    random_character = random.choice(STORY_ELEMENTS[character])
    random_setting = random.choice(STORY_ELEMENTS[setting])
    random_plot = random.choice(STORY_ELEMENTS[plot])
    return f"Once upon a time, {random_character} was {random_plot} {random_setting}. The adventure was about to begin! 🎉"

def story_generator_layout():
    return html.Div(
        style={"padding": "20px", "textAlign": "center"},
        children=[
            html.H1("📚 Story Generator 📚", style={"color": "#ff33e0", "fontSize": "48px"}),
            html.P(
                "Let's create a magical story together! Choose your character, setting, and plot, then hit the button to generate a fun story. 🚀",
                style={"color": "#333", "fontSize": "20px", "marginBottom": "30px"},
            ),
            # Dropdown for character selection
            dcc.Dropdown(
                id="character-picker",
                options=[{"label": character, "value": character} for character in STORY_ELEMENTS.keys()],
                value="Character",
                style={"width": "50%", "margin": "0 auto", "padding": "10px"},
            ),
            # Dropdown for setting selection
            dcc.Dropdown(
                id="setting-picker",
                options=[{"label": setting, "value": setting} for setting in STORY_ELEMENTS.keys()],
                value="Setting",
                style={"width": "50%", "margin": "20px auto", "padding": "10px"},
            ),
            # Dropdown for plot selection
            dcc.Dropdown(
                id="plot-picker",
                options=[{"label": plot, "value": plot} for plot in STORY_ELEMENTS.keys()],
                value="Plot",
                style={"width": "50%", "margin": "20px auto", "padding": "10px"},
            ),
            # Button to generate story
            html.Button(
                "Generate Story 🎉",
                id="generate-story-btn",
                n_clicks=0,
                style={
                    "backgroundColor": "#FFD700",
                    "border": "none",
                    "color": "white",
                    "padding": "15px 30px",
                    "fontSize": "20px",
                    "borderRadius": "10px",
                    "cursor": "pointer",
                },
            ),
            # Display the generated story
            html.Div(id="story-display", 
                     style={"marginTop": "50px", "fontSize": "24px", "fontStyle": "italic", "color": "#333"}),
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
        Output("story-display", "children"),
        [Input("generate-story-btn", "n_clicks")],
        [Input("character-picker", "value"), Input("setting-picker", "value"), Input("plot-picker", "value")]
    )
    def update_story(n_clicks, character, setting, plot):
        if n_clicks > 0:
            story = get_story_data(character, setting, plot)
            return story
        return "Select your story elements and click 'Generate Story' to create a fun tale!"
