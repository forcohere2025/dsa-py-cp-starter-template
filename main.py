# Read numbers from input until EOF or non-number input
numbers = []
while True:
    try:
        line = input()
        numbers.append(float(line))
    except EOFError:
        break
    except ValueError:
        break

# Calculate sum
total = sum(numbers)

# Output result
print(f"Sum: {total}")