#######Assignment16
class Book:
    count=0
    def __init__(self,bid=0,bname="",price=0,auther=""):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.auther=auther
        Book.count+=1
    
    def showBook(self):
        print("Book id=",self.bid)
        print("Book Name=",self.bname)
        print("price=",self.price)
        print("author name=",self.auther)
    @classmethod
    def showCount(cls):
        print("Total Objects created:",cls.count)
    def __del__(Self):
        print("Book Object Destoryed")
b1=Book()
b2=Book(1,"Python",1000,"Hener Charley")
b1.showBook()
b2.showBook()
Book.showCount()
print("******************2nd question***************************")
class Product:
    discount = 10  # Static Discount %

    def __init__(self, pid=0, pname="", price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        print("Product Created")

    def applyDiscount(self):
        discount_amount = self.price * Product.discount / 100
        final_price = self.price - discount_amount
        return final_price

    def showBook(self):
        print("\nProduct Details")
        print("Product ID :", self.pid)
        print("Product Name :", self.pname)
        print("Price :", self.price)
        print("Quantity :", self.quantity)
        print("Discount :", Product.discount, "%")
        print("Final Price :", self.applyDiscount())

    def __del__(self):
        print("Product Destroyed")


p1 = Product()
p2 = Product(1, "Laptop", 50000, 2)

p1.showBook()
p2.showBook()
print("******************3rd question***************************")
class Shirt:
    increase = 10  

    def __init__(self, sid=0, sname="", stype="", price=0, size="Small"):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size
        print("Shirt Object Created")

    def calculatePrice(self):
        if self.size.lower() == "small":
            return self.price
        elif self.size.lower() == "medium":
            return self.price * 1.10
        elif self.size.lower() == "large":
            return self.price * 1.20
        elif self.size.lower() == "xlarge":
            return self.price * 1.30
        else:
            return self.price

    def showBook(self):
        print("\nShirt Details")
        print("Shirt ID :", self.sid)
        print("Shirt Name :", self.sname)
        print("Type :", self.stype)
        print("Size :", self.size)
        print("Base Price :", self.price)
        print("Final Price :", self.calculatePrice())

    def __del__(self):
        print("Shirt Object Destroyed")



s1 = Shirt()
s2 = Shirt(201, "Peter England", "Formal", 1000, "Small")
s3 = Shirt(202, "Allen Solly", "Formal", 1000, "Medium")
s4 = Shirt(203, "Levis", "Casual", 1000, "Large")
s5 = Shirt(204, "Nike", "Sports", 1000, "XLarge")

s1.showBook()
s2.showBook()
s3.showBook()
s4.showBook()
s5.showBook()