import random

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
