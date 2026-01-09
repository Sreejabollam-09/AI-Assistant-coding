# Fibonacci Sequence Generator - Modular Implementation

def generate_fibonacci(n):
    """
    This function contains the logic to generate 
    a Fibonacci sequence up to n terms.
    """
    sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        sequence.append(a)
        # Update logic: a becomes b, b becomes the sum
        a, b = b, a + b
    
    return sequence

# --- Main Execution Block ---
user_input = input("Enter the number of terms: ")

if user_input.isdigit():
    num_terms = int(user_input)
    
    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        # Calling the user-defined function
        result = generate_fibonacci(num_terms)
        
        print(f"Fibonacci sequence with {num_terms} terms:")
        print(*result) # Unpacks the list for clean printing
else:
    print("Invalid input. Please enter a numeric value.")
