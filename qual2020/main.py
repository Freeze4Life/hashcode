# Classes

class Library:

    book_scores = list()

    def __init__(self, id, n_books, time, rate, books_id_arr):
        self.id = id
        self.n_books = n_books
        self.time = time
        self.rate = rate
        self.books_id_arr = books_id_arr
    


    def worth(self, days_rem):
        # sum of scores of books for (rem days - signup time) indices / signup time
        return sum(list(map(lambda book_id: Library.book_scores[book_id], self.books_id_arr[ : ((days_rem-self.time)*self.rate) ]))) / self.time




# Functions

def sort_book_indices(book_ids):
        books_dict = dict()

        for id in book_ids:
            books_dict[id] = Library.book_scores[id]
        
        #sort based on scores
        sorted_books_dict = dict(sorted(books_dict.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_books_dict.keys())



def main():
    # INPUT

    B, L, D = tuple(map(int, input().split()))

    Library.book_scores = list(map(int, input().split()))

    libraries = list()

    for i in range(L):
        no_of_books, signup_time, max_books_per_day = tuple(map(int, input().split()))

        book_ids = list(map(int, input().split()))
        sorted_book_ids = sort_book_indices(book_ids)

        libraries.append(Library(i, no_of_books, signup_time,max_books_per_day, sorted_book_ids))

    print(libraries[0].books_id_arr)
    print(libraries[0].worth(4))




# main exec
if __name__ == "__main__":
    main()

# LOGIC
# give each lib a rank decided by total score of that library divided by no of days it takes to sign up -> worth
# k = (rate * no of days left)
# score = (score of top k books without repetitions)
