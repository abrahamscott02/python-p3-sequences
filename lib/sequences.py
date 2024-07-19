def print_fibonacci(length):
    if length <= 0:
        print("[]")  # Print empty list for non-positive length
        return

    # Handle the cases for length 1 or 2 separately
    if length == 1:
        print([0])
        return
    elif length == 2:
        print([0, 1])
        return

    # Initialize the list with the first two Fibonacci numbers
    fibonacci_sequence = [0, 1]
    
    # Generate the rest of the Fibonacci sequence up to the requested length
    while len(fibonacci_sequence) < length:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)

    # Print the Fibonacci sequence up to the requested length
    print(fibonacci_sequence)
