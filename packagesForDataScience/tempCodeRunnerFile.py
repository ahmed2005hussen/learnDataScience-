# use it when u work on ordered data / time series 
import pandas as pd

stock_a = pd.DataFrame({
    'date': ['2023-01-01', '2023-01-03', '2023-01-04'],
    'price_a': [100, 102, 103]
})

stock_b = pd.DataFrame({
    'date': ['2023-01-02', '2023-01-03', '2023-01-05'],
    'price_b': [200, 202, 205]
})

merged = pd.merge_ordered(stock_a, stock_b, on='date')

print(merged)
