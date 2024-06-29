import numpy as np

def calculate_stats(numbers):
    count = len(numbers)
    mean = np.mean(numbers)
    median = np.median(numbers)
    std_dev = np.std(numbers)
    
    return {
        "count": count,
        "mean": mean,
        "median": median,
        "standard_deviation": std_dev
    }
