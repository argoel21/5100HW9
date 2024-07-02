import unittest
import pandas as pd
from booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        self.assertTrue("War of the Worlds" in test_object.book_list['book_name'].values)

    def test_2_add_book(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("War of the Worlds", 4)
        self.assertEqual(test_object.book_list['book_name'].value_counts().get("War of the Worlds", 0), 1)

    def test_3_has_read(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        self.assertTrue(test_object.has_read("War of the Worlds"))

    def test_4_has_read(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        self.assertFalse(test_object.has_read("War of the Worlds"))

    def test_5_num_books_read(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Dune", 5)
        self.assertEqual(test_object.num_books_read(), 2)

    def test_6_fav_books(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Dune", 5)
        test_object.add_book("Some Book", 2)
        fav_books = test_object.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))


if __name__ == '__main__':
    unittest.main(verbosity=3)