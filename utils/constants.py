TAGS_LIST = [
    'Breakfast',
    'Lunch',
    'Dinner',
    'Dessert',
    'Quick and Easy',
    'Low Calorie',
    'Healthy',
    'Vegetarian',
    'Vegan',
    'Low Carb',
    'Gluten Free',
    'On a Budget',
    'Prep Ahead'
    ]
# Idea for better code consistency and less error-prone tags provided by Reuben Ferrante (CI Mentor)
TAGS = [(tag, "-".join(tag.lower().split(" "))) for tag in TAGS_LIST]
