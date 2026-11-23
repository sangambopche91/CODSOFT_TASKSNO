import unittest

from main import (
    MOVIES,
    normalize_preferences,
    cosine_similarity,
    recommend_movies
)


class TestRecommendationSystem(unittest.TestCase):

    def test_preferences_are_normalized(self):
        result = normalize_preferences("SCI-FI, Action")
        self.assertEqual(result, {"sci-fi", "action"})

    def test_recommends_matching_genre(self):
        results = recommend_movies("sci-fi", 5)

        self.assertTrue(len(results) > 0)

        for movie in results:
            self.assertIn("Sci-Fi", movie["genres"])

    def test_recommends_matching_keyword(self):
        results = recommend_movies("space", 5)

        titles = [movie["title"] for movie in results]

        self.assertIn("Interstellar", titles)

    def test_limit_is_respected(self):
        results = recommend_movies("adventure", 3)
        self.assertLessEqual(len(results), 3)

    def test_watched_movies_are_excluded(self):
        results = recommend_movies(
            "sci-fi",
            5,
            watched=["Interstellar"]
        )

        titles = [movie["title"] for movie in results]

        self.assertNotIn("Interstellar", titles)

    def test_empty_preferences(self):
        self.assertEqual(recommend_movies(""), [])

    def test_invalid_limit(self):
        self.assertEqual(recommend_movies("sci-fi", 0), [])

    def test_similarity_score_range(self):
        score = cosine_similarity(
            {"sci-fi", "action"},
            {"sci-fi", "action", "space"}
        )

        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 1)

    def test_all_recommendations_have_scores(self):
        results = recommend_movies("comedy", 5)

        for movie in results:
            self.assertIn("score", movie)
            self.assertGreater(movie["score"], 0)

    def test_movie_catalog_is_available(self):
        self.assertGreaterEqual(len(MOVIES), 10)


if __name__ == "__main__":
    unittest.main()
