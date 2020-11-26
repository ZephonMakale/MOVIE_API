import unittest
from app.models import Review



class ReviewTest(unittest.TestCase):
    """
    test class to test the behaviour of the review classs
    """
    def setUp(self):
        """
        set up method that will run before every test
        """
        self.new_review = Review('movie_id','title','imageurl','review')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review, Review))