"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    # user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    user_prefs = {
    "favorite_genres": ["lofi", "jazz"],   # list instead of single value
    "favorite_moods":  ["chill", "relaxed"],
    "target_energy":       0.40,
    "target_acousticness": 0.80,
    "target_tempo":        78,             # add this
    # drop valence & danceability, or add weights:
    "weights": {
        "energy": 0.35,
        "acousticness": 0.35,
        "tempo": 0.20,
        "genre": 0.05,
        "mood": 0.05,
    }
}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
