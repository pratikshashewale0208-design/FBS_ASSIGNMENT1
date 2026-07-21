###Assignment15###############################
class Book:
    def __init__(self,bid=0,bname="waiting",price=700,author="pratiksha"):
        self.bd=bid
        self.bn=bname
        self.pr=price
        self.au=author
    def showBook(self):
        print(f"{self.bd},{self.bn},{self.pr},{self.au}")
    def __del__(self):
        print("Book Object destroy")
#parametrised
b1=Book(101,"Python",500,"Guido")
b1.showBook()
#parameterless
b2=Book()
b2.showBook()

print("#############################################################################")
class Product:
    def __init__(self,pid=0,pname="",price=700,quantity=0):
        self.pd=pid
        self.pn=pname
        self.pr=price
        self.pq=quantity
    def showProduct(self):
        print(f"{self.pd},{self.pn},{self.pr},{self.pq}")
    def __del__(self):
        print("Product Object destroy")
#parametrised
p1=Product(1,"Tv",20500,2)
p1.showProduct()
#parameterless
p2=Product()
p2.showProduct()

print("#######################################################################")
class Shirt:
    def __init__(self,sid=0,sname="",price=700,stype="",size="XL"):
        self.sd=sid
        self.sn=sname
        self.pr=price
        self.st=stype
        self.sz=size
    def showShirt(self):
        print(f"{self.sd},{self.sn},{self.pr},{self.st},{self.sz}")
    def __del__(self):
        print("Shirt Object destroy")
#parametrised
s1=Shirt(1,"Cotton",800,"Formal","M")
s1.showShirt()
#parameterless
s2=Shirt()
s2.showShirt()