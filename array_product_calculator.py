from typing import List

def calculate_products(nums: List[int]) -> List[int]:
    """
    Calculates the product of all elements in a list except the one at the corresponding position.
    
    Args:
        nums (List[int]): A list of integers.
    
    Returns:
        List[int]: A list where each element is the product of all other elements in the input list.
    
    Examples:
        >>> calculate_products([1, 2, 3, 4])
        [24, 12, 8, 6]
        >>> calculate_products([0, 1, 2])
        [2, 0, 0]
        >>> calculate_products([-1, -2, -3, -4])
        [-24, -12, -8, -6]
    """
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    result = [1] * n
    
    for i in range(1, n):
        left_products[i] = left_products[i-1] * nums[i-1]
    
    for i in range(n-2, -1, -1):
        right_products[i] = right_products[i+1] * nums[i+1]
    
    for i in range(n):
        result[i] = left_products[i] * right_products[i]
    
    return result