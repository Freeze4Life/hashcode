#import operator

class Library:
    def __init__(self,id,n_books,time,rate,books):
        self.id = id
        self.n_books = n_books
        self.time = time
        self.rate = rate
        self.books = books
        self.value = 0
        self.scanned = []
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
time = D
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

comp_books = set()
comp_lib = list()
while time>0 and len(libraries)>0:
    ## DONE: only consider libs whose sign up time less than days left
    for lib in libraries:
        if lib.time>time:
            continue
        lib.arrange_books()
        quant = (time-lib.time)*lib.rate
        lib.value = sum([temp.score for temp in lib.books[:quant]])/lib.time
    libraries = sorted(libraries,reverse=True,key=(lambda x: x.value))
    used_lib = libraries.pop(0)
    quant = (time-used_lib.time)*used_lib.rate
    time = D-used_lib.time
    used_lib.scanned = used_lib.books[:quant]
    comp_books.add(frozenset(used_lib.scanned))
    comp_lib.append((used_lib.id,used_lib.scanned))

print(len(comp_lib))
for (lib,books) in comp_lib:
    print(lib,len(books))
    for book in books:
        print(book.id,end=" ")
    print()
