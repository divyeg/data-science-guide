def calculate_power(a, b):
    """
    Args:
     a(int64)
     b(int64)
    Returns:
     int32
    """
    if b==0:
        return 1
    if a==1:
        return 1
    if a == 0:
        return 0
    
    result = calculate_power(a, b // 2)
    result_power = (result*result) % 1000000007

    if b%2 > 0:
        result_power = (result_power*a) % 1000000007
        return result_power
    else:
        return result_power



print(calculate_power(100,3))