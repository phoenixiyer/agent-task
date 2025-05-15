# Array Products Calculator

## Task Description

Create a Python function `calculate_products` that takes a list of integers and returns a new list where each element is the product of all other elements in the original list except the one at the corresponding position.

## Requirements:

1. The function should be named `calculate_products`
2. It should take a single parameter: a list of integers
3. It should return a list of integers where each element is the product of all other numbers in the input list
4. Do not use division in your solution
5. Include proper type hints
6. Add comprehensive docstrings with examples
7. Implement the solution with O(n) time complexity

## Example:

```python
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]
```

Explanation:
- For position 0: 2 * 3 * 4 = 24
- For position 1: 1 * 3 * 4 = 12
- For position 2: 1 * 2 * 4 = 8
- For position 3: 1 * 2 * 3 = 6

## Testing:

Your solution will be tested with the following inputs:
1. [1, 2, 3, 4] → Expected output: [24, 12, 8, 6]
2. [0, 1, 2] → Expected output: [2, 0, 0]
3. [-1, -2, -3, -4] → Expected output: [-24, -12, -8, -6]
