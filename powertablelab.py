def display_table(n):
    print(f"{'Number':<10}{'Square':<10}{'Cube':<10}")
    print("-" * 30)
    for i in range(1, n + 1):
        square = i ** 2
        cube = i ** 3
        print(f"{i:<10}{square:<10}{cube:<10}")


def main():
    while True:
        try:
            # Prompt the user to enter an integer
            num = int(input("Enter an integer: "))

            # Display the table of squares and cubes
            display_table(num)

            # Ask if the user wants to continue
            continue_prompt = input("Do you want to continue? (yes/no): ").strip().lower()
            if continue_prompt != 'yes':
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
