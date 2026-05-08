# Ask the user for a positive integer
# We use int() to convert the input string into a number
user_num = int(input("Enter a positive integer: "))

# Initialize our counter (multiplier) at 10
multiplier = 10

# The while loop runs as long as the multiplier is 20 or less
while multiplier <= 20:
    # Calculate the product
    result = user_num * multiplier
    
    # Print the formatted result
    print(f"{user_num} x {multiplier} = {result}")
    
    # Important: Increment the multiplier so the loop eventually ends
    multiplier += 1
