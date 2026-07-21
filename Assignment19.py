#Assignment19
numbers = [i for i in range(1, 1001) if i % 8 == 0]
print(numbers)
print("*********************2*****************")
numbers = [i for i in range(1, 1001) if '6' in str(i)]
print(numbers)
print("*********************3*****************")

text = input("Enter a string: ")

spaces = sum(1 for ch in text if ch == ' ')

print("Number of spaces:", spaces)

print("*********************4***********************")
text = input("Enter a string: ")

result = "".join([ch for ch in text if ch.lower() not in "aeiou"])

print("String without vowels:", result)

print("********************5****************************")
text = input("Enter a sentence: ")

words = [word for word in text.split() if len(word) < 5]

print(words)

print("*****************6*****************************")
text = input("Enter a sentence: ")

length = {word: len(word) for word in text.split()}

print(length)

print("****************7***********************************")
numbers = [num for num in range(1, 1001)
           if any(num % i == 0 for i in range(2, 10))]

print(numbers)

print("*********Generator*********************")

def fibonacci(limit):
    a = 0
    b = 1

    while a <= limit:
        yield a
        a, b = b, a + b


for i in fibonacci(100):
    print(i, end=" ")


def palindrome_generator():
    num = 0

    while True:
        if str(num) == str(num)[::-1]:
            yield num
        num += 1


gen = palindrome_generator()

for i in range(20):
    print(next(gen))

def myrange(start, stop, step=1):
    while start < stop:
        yield start
        start += step


for i in myrange(1, 20, 2):
    print(i)

print("**********Decorator*****************")
def memoize(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]

        result = func(n)
        cache[n] = result
        return result

    return wrapper


@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Enter number: "))
print("Fibonacci:", fibonacci(num))
