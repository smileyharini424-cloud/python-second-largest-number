numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_numbers = sorted(set(numbers), reverse=True)

if len(unique_numbers) < 2:
    print("A second largest number does not exist.")
else:
    print("Second largest number:", unique_numbers[1])
