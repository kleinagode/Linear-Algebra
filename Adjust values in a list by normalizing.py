
num_values = int(input())
values = []

for i in range(num_values):
    values.append(float(input()))

maximum_value = max(values)

devided_values = [item /maximum_value for item in values]

for item in devided_values:
    print(f"{item:.2f}")