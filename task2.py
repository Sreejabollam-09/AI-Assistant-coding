def get_fibonacci_sequence(n: int) -> list:
    """
    Generates a list containing the Fibonacci sequence up to n terms.
    
    Args:
        n (int): The number of terms to generate.
        
    Returns:
        list: A list of Fibonacci numbers.
    """
    # Initialize the sequence with the first two numbers
    sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        sequence.append(a)
        # Simultaneous assignment to calculate the next term efficiently
        a, b = b, a + b
        
    return sequence

def main():
    """
    Handles user interaction and displays the sequence.
    """
    try:
        user_input = input("Enter the number of terms for the Fibonacci sequence: ")
        n_terms = int(user_input)

        if n_terms <= 0:
            print("Please enter a positive integer greater than zero.")
        else:
            # Calling the modular function
            fib_list = get_fibonacci_sequence(n_terms)
            
            print(f"\nGenerated Sequence ({n_terms} terms):")
            print(fib_list)
            
    except ValueError:
        print("Invalid input! Please enter a numeric whole number.")

if __name__ == "__main__":
    main()