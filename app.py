import dash
from dash import dcc, html, Input, Output
from apps.mood_generator.mood import get_mood_data, mood_generator_layout
from apps.color_picker.colors import get_color_data, color_data_layout
from apps.shape_drawing import shape_drawing_layout, register_shape_callbacks
from apps.simple_calculator import calculator_layout, register_calculator_callbacks
from apps.story_generator import  story_generator_layout, register_callbacks

# Initialize the app
app = dash.Dash(__name__, suppress_callback_exceptions=True, title="Coding Fun Land | Helena Mbeua Pedro")
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
            html.Nav([html.A("Activities", href="#activities"), html.A("Meet Helena", href="#about"), html.A("LinkedIn ↗", href="https://www.linkedin.com/in/helena-mbeua-pedro/", target="_blank", className="nav-cta")], className="nav-links"),
        ]),
        html.Main([
            html.Section(className="hero section-wrap", children=[
                html.Div(className="hero-copy", children=[
                    html.P("✦ Technology educator & creative builder", className="eyebrow"),
                    html.H1(["Where young minds ", html.Span("learn by creating.")]),
                    html.P("I’m Helena Mbeua Pedro. I make technology approachable through joyful, hands-on experiences that help children explore, create, and grow with confidence.", className="hero-intro"),
                    html.Div([html.A("Explore the activities", href="#activities", className="button button-primary"), html.A("Connect with Helena", href="https://www.linkedin.com/in/helena-mbeua-pedro/", target="_blank", className="button button-secondary")], className="hero-actions"),
                ]),
                html.Div(className="hero-visual", children=[
                    html.Div("💡", className="floating-icon icon-one"), html.Div("🚀", className="floating-icon icon-two"),
                    html.Div([html.Span("HELLO, CREATOR!", className="code-label"), html.Div("< dream >", className="code-line line-purple"), html.Div("  learn()", className="code-line line-blue"), html.Div("  build()", className="code-line line-coral"), html.Div("</ dream >", className="code-line line-purple"), html.P("Every big idea starts with curiosity.")], className="code-card"),
                    html.Div([html.Strong("5"), html.Span("interactive activities")], className="activity-badge"),
                ]),
            ]),
            html.Section(id="activities", className="activities-section section-wrap", children=[
                html.Div([html.Div([html.P("LEARN • PLAY • CREATE", className="eyebrow"), html.H2("Choose your next adventure")]), html.P("Each activity turns an everyday idea into a small, satisfying creative win.", className="section-intro")], className="section-heading"),
                html.Div([card(*project) for project in projects], className="project-grid"),
            ]),
            html.Section(id="about", className="about-section", children=[html.Div(className="about-inner section-wrap", children=[
                html.Div([html.Span("HP", className="portrait-monogram"), html.Span("✦", className="portrait-spark")], className="portrait-card"),
                html.Div(className="about-copy", children=[html.P("MEET THE CREATOR", className="eyebrow eyebrow-light"), html.H2("Helping the next generation feel at home with technology."), html.P("Helena Mbeua Pedro is a technology educator and creative builder who believes learning works best when curiosity leads the way. Coding Fun Land brings that philosophy to life through approachable digital activities for young learners."), html.P("Her work sits at the intersection of education, technology, and playful experimentation—making complex ideas feel human, useful, and fun."), html.A("Follow Helena’s journey on LinkedIn ↗", href="https://www.linkedin.com/in/helena-mbeua-pedro/", target="_blank", className="text-link")]),
            ])]),
        ]),
        html.Footer(className="site-footer section-wrap", children=[html.Div([html.Span("HF", className="brand-mark small"), html.Span("Coding Fun Land")], className="footer-brand"), html.P("© 2026 Helena Mbeua Pedro. Built with curiosity.")]),
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
