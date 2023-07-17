def generate_series(x):
    series = []
    for i in range(1, x+1):
        series.append(2*i - 1)
    return series

# Example usage
input_num = int(input("Enter the value of x: "))
output_series = generate_series(input_num)
print(output_series)
