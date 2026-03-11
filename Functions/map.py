# Program: Using map() with user input.

def to_int(value):
    """Convert string to integer with error handling."""
    try:
        return int(value)
    except ValueError:
        print(f"Warning: '{value}' is not a valid integer. Using 0 instead.")
        return 0

def main():
    # Prompt user for space-separated numbers.
    user_input = input("Enter numbers separated by spaces: ").strip()

    if not user_input:
        print("No input provided.")
        return

    # Split input into list of strings.
    str_numbers = user_input.split()

    # Use map() to convert each string to an integer.
    numbers = list(map(to_int, str_numbers))

    print(f"Converted numbers: {numbers}")
    print(f"Sum of numbers: {sum(numbers)}")

if __name__ == "__main__":
    main()
