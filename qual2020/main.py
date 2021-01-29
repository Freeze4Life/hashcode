import operator

class Library:
    def __init__(self,id,n_books,time,rate,books):
        self.id = id
        self.n_books = n_books
        self.time = time
        self.rate = rate
        self.books = books
        self.value = 0
    def __str__(self):
        return f"ID:{self.id}"
    def arrange_books(self):
        self.books=[ele for ele in self.books if ele not in comp_books]
        self.books=sorted(self.books,reverse=True,key=(lambda x: x.score))

class Book:
    def __init__(self,id,score):
        self.id = id
        self.score = score
    def __str__(self):
        return f"ID:{self.id} SCORE:{self.score}"

TIME = int()

#INPUT
B,L,D = tuple(map(int,input().split()))
TIME = D
scores = list(map(int,input().split()))
books = list()
libraries = list()
for i in range(B):
    books.append(Book(i,scores[i]))

for i in range(L):
    N,T,M = tuple(map(int,input().split()))
    bookids = list(map(int,input().split()))
    lib_books = [books[i] for i in bookids]
    libraries.append(Library(i,N,T,M,lib_books))

#LOGIC
# give each lib a rank decided by total score of that library divided by no of days it takes to sign up
# k = (rate * no of days left)
# score = (score of top k books without repetitions)
comp_books = list()
for time in range(D,0,-1):
    ## TODO: only consider libs whose sign up time less than days left
    for lib in libraries:
        lib.arrange_books()
        quant = (time-lib.time)*lib.rate
        lib.value = sum([temp.score for temp in lib.books[:quant]])/lib.time
    libraries = sorted(libraries,reverse=True,key=(lambda x: x.value))
    time = D-libraries[0].time+1
    comp_books.append(libraries[0].books[:quant])
    comp_lib.append(libraries[0].id)
    libraries.pop(0)
