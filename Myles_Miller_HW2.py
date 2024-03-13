def num_paths(m, n):
    """
    Calculate the number of paths from the top-left to bottom-right in an m x n grid.
    This function uses a simple recursive strategy without memoization.
    
    Parameters:
    m (int): The number of rows in the grid.
    n (int): The number of columns in the grid.
    
    Returns:
    int: The total number of paths.
    """
    # Base case: if either m or n is 1, there's only one way to reach the end
    if m == 1 or n == 1:
        return 1
    # Recursive step: sum of paths from the cell on the left and the cell above
    return num_paths(m - 1, n) + num_paths(m, n - 1)

def num_paths_memo(m, n, memo={}):
    """
    Calculate the number of paths from the top-left to bottom-right in an m x n grid.
    This function uses memoization to optimize the recursive calculations.
    
    Parameters:
    m (int): The number of rows in the grid.
    n (int): The number of columns in the grid.
    memo (dict): A dictionary to store the results of subproblems to avoid recalculating.
    
    Returns:
    int: The total number of paths.
    """
    # Check if the result is in the memo
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 1 or n == 1:
        return 1
    # If not in memo, calculate and store the result in memo
    memo[(m, n)] = num_paths_memo(m - 1, n, memo) + num_paths_memo(m, n - 1, memo)
    return memo[(m, n)]

# Example usage
if __name__ == "__main__":
    m, n = 15, 14
    print("Calculating number of paths without memoization...")
    print(num_paths(m, n))
    print("Calculating number of paths with memoization...")
    print(num_paths_memo(m, n))
