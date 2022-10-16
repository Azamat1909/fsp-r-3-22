

operators = ['+', '-', '^', '/']
nums = [2, 4, 5, 6, 7]

temp = operators[len(operators) - 1]
nums.append(temp)
operators.pop()
print(nums, operators)
