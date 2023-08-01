import unittest
from booklover import BookLover

class BookLoverTestSuit(unittest.TestCase):
    
    def test_1_add_book(self): 
         # add a book and test if it is in `book_list`.
        mybook = BookLover('Brandon','fqd2hj@virginia.edu','Mystery','Scooby Doo',3)
        mybook.add_book('Twilight',2) 
        expected = 'Book has been added to list.'
        
        self.assertEqual(mybook.add_book, expected)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        mybook = BookLover('Brandon','fqd2hj@virginia.edu','Mystery','Twilight',2)
        mybook.add_book('Twilight',2) 
        expected = 'Book is already included in data.'
        
        self.assertEqual(mybook.add_book, expected)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        mybook = BookLover('Brandon','fqd2hj@virginia.edu','Mystery','Twilight',2)
        mybook.has_read('Twilight')
        
        self.assertTrue(mybook.has_read)
        
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        mybook = BookLover('Brandon','fqd2hj@virginia.edu','Mystery','Twilight',2)
        mybook.has_read('Scooby Doo')
        
        self.assertFalse(mybook.has_read)
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        mybook = BookLover('Brandon','fqd2hj@virginia.edu','Mystery','Twilight',2)
        mybook.add_book(['Ditty Bird','Click Clack Moo'],[1,5])
        mybook.num_books_read()
        expected = 3
        
        self.assertEqual(mybook.num_books_read,expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3.
        mybook = BookLover('Brandon','fqd2hj@virginia.edu','Mystery','Twilight',2)
        orginal = len(mybook.fav_books())
        mybook.add_book(['Animals','Baby Baluga'],[3,5])
        mybook.fav_books()
        expected = orginal + 2
        
        self.assertEqual(mybook.fav_books,expected)
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)