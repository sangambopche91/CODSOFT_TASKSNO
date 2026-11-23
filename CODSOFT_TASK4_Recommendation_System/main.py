import math

MOVIES = [
    {"title": "Interstellar", "genres": ["Sci-Fi", "Adventure", "Drama"],
     "tags": ["space", "exploration", "family", "future"]},

    {"title": "Inception", "genres": ["Sci-Fi", "Action", "Thriller"],
     "tags": ["dreams", "mind-bending", "heist", "psychology"]},

    {"title": "The Matrix", "genres": ["Sci-Fi", "Action"],
     "tags": ["artificial intelligence", "virtual reality", "technology"]},

    {"title": "The Dark Knight", "genres": ["Action", "Crime", "Drama"],
     "tags": ["superhero", "justice", "crime", "batman"]},

    {"title": "Titanic", "genres": ["Romance", "Drama"],
     "tags": ["love", "ship", "history", "tragedy"]},

    {"title": "The Notebook", "genres": ["Romance", "Drama"],
     "tags": ["love", "relationship", "emotional"]},

    {"title": "Finding Nemo", "genres": ["Animation", "Adventure", "Comedy"],
     "tags": ["ocean", "family", "friendship", "underwater"]},

    {"title": "Toy Story", "genres": ["Animation", "Comedy", "Adventure"],
     "tags": ["toys", "friendship", "family", "fun"]},

    {"title": "The Conjuring", "genres": ["Horror", "Mystery"],
     "tags": ["ghost", "supernatural", "paranormal", "fear"]},

    {"title": "A Quiet Place", "genres": ["Horror", "Thriller"],
     "tags": ["survival", "monsters", "silence", "fear"]},

    {"title": "The Martian", "genres": ["Sci-Fi", "Adventure"],
     "tags": ["space", "survival", "science", "mars"]},

    {"title": "Jumanji", "genres": ["Adventure", "Comedy", "Fantasy"],
     "tags": ["game", "jungle", "adventure", "fun"]}
]


def normalize_preferences(preferences):
    """Convert user preferences into normalized keywords."""
    if isinstance(preferences, str):
        preferences = preferences.split(",")

    return {
        str(item).strip().lower()
        for item in preferences
        if str(item).strip()
    }


def get_movie_features(movie):
    """Combine movie genres and tags into one feature set."""
    return {
        item.strip().lower()
        for item in movie["genres"] + movie["tags"]
    }


def cosine_similarity(user_features, movie_features):
    """Calculate cosine similarity between user and movie features."""
    if not user_features or not movie_features:
        return 0.0

    common_features = user_features.intersection(movie_features)

    return len(common_features) / math.sqrt(
        len(user_features) * len(movie_features)
    )


def recommend_movies(preferences, limit=5, watched=None):
    """Return movies ranked by similarity to user preferences."""
    user_features = normalize_preferences(preferences)

    if not user_features or limit <= 0:
        return []

    watched = {
        title.strip().lower()
        for title in (watched or [])
    }

    recommendations = []

    for movie in MOVIES:
        if movie["title"].lower() in watched:
            continue

        features = get_movie_features(movie)

        score = cosine_similarity(user_features, features)

        if score > 0:
            recommendations.append({
                "title": movie["title"],
                "genres": movie["genres"],
                "score": score
            })

    recommendations.sort(
        key=lambda item: (-item["score"], item["title"])
    )

    return recommendations[:limit]


def display_recommendations(recommendations):
    """Display recommended movies in a readable format."""
    if not recommendations:
        print("\nNo matching movies found.")
        return

    print("\n========== RECOMMENDED MOVIES ==========")

    for index, movie in enumerate(recommendations, start=1):
        print(f"\n{index}. {movie['title']}")
        print(f"   Genres: {', '.join(movie['genres'])}")
        print(f"   Match Score: {movie['score']:.2%}")

    print("\n========================================")


def main():
    print("========================================")
    print("       MOVIE RECOMMENDATION SYSTEM")
    print("========================================")

    print("\nAvailable genres:")
    print("Sci-Fi, Action, Adventure, Drama, Romance")
    print("Animation, Comedy, Horror, Thriller, Mystery")
    print("\nYou can also enter keywords such as space, love,")
    print("friendship, survival, science, or technology.")

    preferences = input(
        "\nEnter your preferred genres/keywords (comma separated): "
    )

    try:
        limit_input = input("Number of recommendations (default 5): ").strip()
        limit = int(limit_input) if limit_input else 5

        if limit <= 0:
            print("Please enter a positive number.")
            return

    except ValueError:
        print("Invalid number. Please enter a whole number.")
        return

    recommendations = recommend_movies(preferences, limit)

    display_recommendations(recommendations)


if __name__ == "__main__":
    main()
