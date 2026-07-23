import dash
from dash import dcc, html, Input, Output
from apps.mood_generator.mood import get_mood_data, mood_generator_layout
from apps.color_picker.colors import get_color_data, color_data_layout
from apps.shape_drawing import shape_drawing_layout, register_shape_callbacks
from apps.simple_calculator import calculator_layout, register_calculator_callbacks
from apps.story_generator import  story_generator_layout, register_callbacks

# Initialize the app
SOCIAL_META_TAGS = [
    {"name": "description", "content": "Playful, hands-on coding activities that help young minds explore, create, and learn with confidence."},
    {"property": "og:type", "content": "website"},
    {"property": "og:site_name", "content": "Coding Fun Land"},
    {"property": "og:title", "content": "Coding Fun Land | Learn by Creating"},
    {"property": "og:description", "content": "Explore playful coding activities designed to spark curiosity, creativity, and confidence."},
    {"property": "og:url", "content": "https://codingfunland.hmpedro.com/"},
    {"property": "og:image", "content": "https://codingfunland.hmpedro.com/assets/helena-pedro-codingfunland.png"},
    {"property": "og:image:secure_url", "content": "https://codingfunland.hmpedro.com/assets/helena-pedro-codingfunland.png"},
    {"property": "og:image:type", "content": "image/png"},
    {"property": "og:image:width", "content": "1672"},
    {"property": "og:image:height", "content": "941"},
    {"property": "og:image:alt", "content": "Helena Pedro, creator of Coding Fun Land"},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:title", "content": "Coding Fun Land | Learn by Creating"},
    {"name": "twitter:description", "content": "Explore playful coding activities designed to spark curiosity, creativity, and confidence."},
    {"name": "twitter:image", "content": "https://codingfunland.hmpedro.com/assets/helena-pedro-codingfunland.png"},
    {"name": "twitter:image:alt", "content": "Helena Pedro, creator of Coding Fun Land"},
]

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    title="Coding Fun Land | Helena Pedro",
    meta_tags=SOCIAL_META_TAGS,
)
server = app.server

register_calculator_callbacks(app)
register_shape_callbacks(app)
register_callbacks(app)

# Home Page Layout
def homepage_layout():
    projects = [
        ("Mood Generator", "Explore emotions, colors, and encouraging words.", "/mood-generator", "🎭", "Wellbeing", "mood"),
        ("Color Picker", "Experiment with color and bring creative choices to life.", "/color-picker", "🎨", "Creativity", "color"),
        ("Simple Calculator", "Build confidence with numbers through playful practice.", "/simple-calculator", "🧮", "Problem solving", "calculator"),
        ("Shape Drawing", "Turn ideas into shapes and discover digital art.", "/shape-drawing", "✦", "Design", "shape"),
        ("Story Generator", "Mix imagination and technology to create a unique story.", "/story-generator", "📖", "Imagination", "story"),
    ]

    def card(title, description, href, icon, tag, theme):
        return dcc.Link(html.Article([
            html.Div([html.Span(tag, className="project-tag"), html.Span(icon, className="project-icon")], className="project-card-top"),
            html.H3(title), html.P(description),
            html.Span(["Open activity ", html.Span("→", className="arrow")], className="card-cta"),
        ], className=f"project-card card-{theme}"), href=href, className="project-link")

    return html.Div(className="site-shell", children=[
        html.Header(className="site-header", children=[
            dcc.Link([html.Span("HF", className="brand-mark"), html.Span("Coding Fun Land", className="brand-name")], href="/", className="brand"),
            html.Nav([html.A("Activities", href="#activities"), html.A("Visit hmpedro.com ↗", href="https://hmpedro.com/", target="_blank", className="nav-cta")], className="nav-links"),
        ]),
        html.Main([
            html.Section(className="hero section-wrap", children=[
                html.Div(className="hero-copy", children=[
                    html.P("✦ Playful technology projects for curious minds", className="eyebrow"),
                    html.H1(["Where young minds ", html.Span("learn by creating.")]),
                    html.P("I am Helena Pedro. This collection of hands-on activities invites children to explore technology, create freely, and build confidence through play.", className="hero-intro"),
                    html.Div([html.A("Explore the activities", href="#activities", className="button button-primary"), html.A("Visit my website", href="https://hmpedro.com/", target="_blank", className="button button-secondary")], className="hero-actions"),
                ]),
                html.Div(className="hero-visual", children=[
                    html.Div("💡", className="floating-icon icon-one"), html.Div("🚀", className="floating-icon icon-two"),
                    html.Img(src="/assets/helena-pedro-codingfunland.png", alt="Portrait of Helena Pedro", className="hero-photo"),
                    html.Div([html.Strong("5"), html.Span("interactive activities")], className="activity-badge"),
                ]),
            ]),
            html.Section(id="activities", className="activities-section section-wrap", children=[
                html.Div([html.Div([html.P("LEARN • PLAY • CREATE", className="eyebrow"), html.H2("Choose your next adventure")]), html.P("Each activity turns an everyday idea into a small, satisfying creative win.", className="section-intro")], className="section-heading"),
                html.Div([card(*project) for project in projects], className="project-grid"),
            ]),
        ]),
        html.Footer(className="site-footer section-wrap", children=[html.Div([html.Span("HF", className="brand-mark small"), html.Span("Coding Fun Land")], className="footer-brand"), html.P("© 2026 Helena Pedro. Built with curiosity.")]),
    ])

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
    elif pathname == "/story-generator":
        return story_generator_layout()
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
