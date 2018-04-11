def parse_k_values(k_values):
    """
    Expects a string like "1,2,3". Returns a list of integers: [1, 2, 3].
    """
    return [int(value.strip()) for value in k_values.split(',')]
