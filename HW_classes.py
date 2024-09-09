class Book:
    def __init__(self, title: str, author: str, year: int, genre: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.review_list = []  # List of reviews, initialized as an empty list

    # Adding __repr__ for detailed representation
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year}, genre='{self.genre}')"

    # Adding __str__ for a more readable representation
    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.year} (Genre: {self.genre})"

  
# Creating several different books
book1 = Book("1984", "George Orwell", 1949, "Dystopian")
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
book3 = Book("Pride and Prejudice", "Jane Austen", 1813, "Romance")

# __repr__
print("repr method is : ", repr(book1))  
# __str__
print("str method is : ", str(book1))  


class BookReview:
    def write_review(self, book: Book, review: str):
        # Append review to the book's review list without assigning it to a variable
        book.review_list.append(review)


# adding reviews
review1.write_review(book1, "A timeless classic that delves into the dangers of totalitarianism.")
review1.write_review(book2, "An inspiring and thought-provoking book about racism and justice.")
review1.write_review(book3, "A beautiful romance novel with social commentary.")

# Show reviews for a specific book
print(f"Reviews for {book1.title}: {book1.review_list}")
