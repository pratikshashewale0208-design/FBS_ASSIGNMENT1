#Assignment20
# Simple Calculator with Exception Handling

try:
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operator = input("Enter operator (+, -, *, /): ")

    
    if operator not in ['+', '-', '*', '/']:
        raise ValueError("Invalid Operator! Please use +, -, *, or /.")

    # Performing operation
    if operator == '+':
        result = num1 + num2

    elif operator == '-':
        result = num1 - num2

    elif operator == '*':
        result = num1 * num2

    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        result = num1 / num2

    print("Result:", result)

except ValueError as e:
    print("Error:", e)

except ZeroDivisionError as e:
    print("Error:", e)

except Exception:
    print("Invalid Number! Please enter valid numbers.")

print("2nd")
class Television:

    def __init__(self):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0

    def get_data(self):

        try:
            
            self.model_number = int(input("Enter Model Number: "))
            self.screen_size = float(input("Enter Screen Size (in inches): "))
            self.price = float(input("Enter Price: "))


            if self.model_number > 9999:
                raise ValueError("Model number should not contain more than 4 digits.")

            
            if self.screen_size < 12 or self.screen_size > 70:
                raise ValueError(
                    "Screen size must be between 12 and 70 inches."
                )

            # Checking price
            if self.price < 0 or self.price > 5000:
                raise ValueError(
                    "Price must be between Rs. 0 and Rs. 5000."
                )

        except Exception as e:
            print("Error:", e)

            # Replace all data members with zero
            self.model_number = 0
            self.screen_size = 0
            self.price = 0

    def display_data(self):
        print("\nTelevision Details")
        print("Model Number:", self.model_number)
        print("Screen Size:", self.screen_size, "inches")
        print("Price: Rs.", self.price)

def main():


    tv = Television()

    
    tv.get_data()

    # Displaying data
    tv.display_data()


# Calling main function
main()