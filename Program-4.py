def count_multiples(numbers):
    counts = {}
    for i in range(1, 10):
        counts[i] = sum(1 for num in numbers if num % i == 0)
    return counts

user_input = input("Enter a list of numbers, separated by commas: ")
numbers = [int(num) for num in user_input.split(",")]

result = count_multiples(numbers)
print(result)
