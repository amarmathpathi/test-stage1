def generate_series(a):
    output = []
    for i in range(a):
        output.append(2*i + 1)
    return output
input_value = int(input("Enter the value of 'a': "))

series = generate_series(input_value)
output_str = ", ".join(map(str, series))
print(output_str)
