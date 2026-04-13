"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs, score_song


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded {len(songs)} songs.\n")

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

    print("\n" + "=" * 50)
    print(" TOP RECOMMENDATIONS")
    print("=" * 50)
    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{i}  {song['title']}  —  {song['artist']}")
        print(f"    Score : {score:.2f}")
        print(f"    Genre : {song['genre']}  |  Mood: {song['mood']}")
        for reason in explanation.split(" | "):
            print(f"    • {reason}")
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
