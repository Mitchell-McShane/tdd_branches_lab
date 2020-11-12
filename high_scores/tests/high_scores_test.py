import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    # Tests
    def setUp(self):
        self.scores = [1,7,3]
    
    # Test latest score (the last thing in the list)
    def tests_lists_latest_score(self):
        last_score = latest(self.scores)
        self.assertEqual(3, last_score)
    
    # Test personal best (the highest score in the list)
    def tests_personal_best_score(self):
        best_score = personal_best(self.scores)
        self.assertEqual(7, best_score)
    

    # Test top three from list of scores

    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    
