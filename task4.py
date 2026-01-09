# Fibonacci Sequence Generator - Logic implemented directly in main
n_input = input("Enter the number of terms (n): ")

if n_input.isdigit():
    n = int(n_input)
    
    if n <= 0:
        print("Please enter a number greater than 0.")
    else:
        # Starting values for the sequence
        a, b = 0, 1
        count = 0
        
        print(f"Fibonacci sequence with {n} terms:")
        
        # Iterative logic handled directly in the main execution path
        while count < n:
            print(a, end=" ")
            # Calculate next term and update variables
            next_term = a + b
            a = b
            b = next_term
            count += 1
        print() # Adds a newline at the end
else:
    print("Error: Invalid input. Please enter a positive integer.")