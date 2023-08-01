import pandas as pd


class BookLover:
    
    def __init__(self, name, email, fav_genre, book_name, book_rating):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.book_list = pd.DataFrame({'Book_Name':[book_name],'Book_Rating':[book_rating]})
        self.num_books = 0 if self.book_list is None else len(list([book_name]))
        
    def add_book(self, book_name, book_rating):
        new_book = pd.DataFrame({'Book_Name': [book_name],
                                 'Book_Rating': [book_rating]
                                })
        if book_name in list(self.book_list['Book_Name']):
            print('Book is already included in data.')
        else:
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            print('Book has been added to list.')
    
    def has_read(self, book_name):
        if book_name in list(self.book_list['Book_Name']):
            return True
        else:
            return False
    
    def num_books_read():
        return self.num_books
        
    def fav_books(self):
        self.book_list.loc[self.book_list['Book_Ratings']>3].sort_values(by = ['Book_Ratings'], ascending = False)