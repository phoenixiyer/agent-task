def array_products(nums):
    """
    Given an array of integers nums, return an array where the value at each index is the product of all the other elements in the original array.
    
    This solution calculates the product of all other elements in the input list for each element, without using division. It uses a two-pass approach to achieve O(n) time complexity.
    """
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    
    for i in range(1, n):
        left_products[i] = left_products[i-1] * nums[i-1]
    
    for i in range(n-2, -1, -1):
        right_products[i] = right_products[i+1] * nums[i+1]
    
    return [left * right for left, right in zip(left_products, right_products)]