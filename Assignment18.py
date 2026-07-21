class Complex:

    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
        print("Constructor Called")

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __del__(self):
        print("Destructor Called")


# Main Program
c1 = Complex(4, 5)
c2 = Complex(2, 3)

print("First Complex Number :", c1)
print("Second Complex Number :", c2)

c3 = c1 + c2
print("Addition :", c3)

c4 = c1 - c2
print("Subtraction :", c4)

print("***************2nd**********************")
class Distance:

    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm
        print("Constructor Called")

    def __add__(self, other):
        cm = self.cm + other.cm
        m = self.m + other.m
        km = self.km + other.km

        # Convert cm to m
        if cm >= 100:
            m += cm // 100
            cm = cm % 100

        # Convert m to km
        if m >= 1000:
            km += m // 1000
            m = m % 1000

        return Distance(km, m, cm)

    def __sub__(self, other):
        total1 = self.km * 100000 + self.m * 100 + self.cm
        total2 = other.km * 100000 + other.m * 100 + other.cm

        diff = abs(total1 - total2)

        km = diff // 100000
        diff %= 100000
        m = diff // 100
        cm = diff % 100

        return Distance(km, m, cm)

    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm"

    def __del__(self):
        print("Destructor Called")


# Main Program
d1 = Distance(2, 500, 50)
d2 = Distance(1, 700, 75)

print("Distance 1 :", d1)
print("Distance 2 :", d2)

d3 = d1 + d2
print("Addition :", d3)

d4 = d1 - d2
print("Subtraction :", d4)