import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category

class TestSearch(unittest.TestCase):
    def test_search_by_category(self):
        dvd1 = DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 89, 19.95)
        dvd2 = DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 87, 24.95)
        results = search_by_category([dvd1, dvd2], "Animation")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "The Lion King")

if __name__ == '__main__':
    unittest.main()