class Library:
    def __init__(self,id,n_books,time,rate,books):
        self.id = id
        self.n_books = n_books
        self.time = time
        self.rate = rate
        self.books = books


class Book:
    def __init__(self,id,score):
        self.id = id
        self.score = score

TIME = int()

#INPUT
B,L,D = tuple(map(int,input().split()))
TIME = D
scores = list(map(int,input().split()))
books = list(B)
libraries = list(L)
for i in range(B):
    books[i] = Book(i,scores[i])

for i in range(L):
    N,T,M = tuple(map(int,input().split()))
    bookids = list(map(int,input().split()))
    libraries[i] = Library(i,N,T,M,bookids)

#LOGIC
# give each lib a rank decided by total score of that library divided by no of days it takes to sign up
# k = (rate * no of days left)
# score = (score of top k books without repetitions)
#Hi there  hi 


