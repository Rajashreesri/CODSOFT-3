items = {
    'Movie1': {'Action': 1, 'Comedy': 0, 'Drama': 1},
    'Movie2': {'Action': 0, 'Comedy': 1, 'Drama': 1},
    'Movie3': {'Action': 1, 'Comedy': 0, 'Drama': 0},
    'Movie4': {'Action': 0, 'Comedy': 1, 'Drama': 1},
    'Movie5': {'Action': 0, 'Comedy': 0, 'Drama': 0}
}

# Function to get item recommendations based on user preferences
def get_recommendations(user_preferences):
    # Calculate a simple weighted sum of preferences for each item
    scores = {item: sum(user_preferences[genre] * items[item][genre] for genre in user_preferences) for item in items}

    # Sort items by score in descending order
    sorted_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # Extract recommended items
    recommendations = [item[0] for item in sorted_items]

    return recommendations

# Example: Get recommendations for user preferences
user_preferences = {'Action': 1, 'Comedy': 1, 'Drama': 0}
recommendations = get_recommendations(user_preferences)
print(recommendations)


