n = int(input())
numbers = list(map(int, input().split()))

expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)

missing = expected_sum - actual_sum
print(missing)
