def generate_fibonacci(n: int) -> list:
    """
    Generates a list containing the Fibonacci sequence up to n terms.
    Optimized using list appending and tuple unpacking.
    """
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    try:
        n_terms = int(input("Enter the number of terms: "))
        if n_terms <= 0:
            print("Please enter a positive integer.")
            return
            
        # Calling the modular function
        result = generate_fibonacci(n_terms)
        print(f"Sequence: {result}")
        
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()