import numpy as np
import pandas as pd

def f(x):
    return 9.36 - 21.963*x + 16.2965*np.pow(x, 2) - 3.70377*np.pow(x, 3)

def tabulasi(a, b, n):
    results = []
    count = 1
    
    x_values = np.arange(a+n, b + n, n)     
    for i in x_values:
        results.append((count, i, f(i)))
        count += 1
    
    df = pd.DataFrame(results, columns=['Iterasi', 'x', 'f(x)'])
    return df

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
n = float(input("Masukkan jumlah step: "))  
  
if a >= b:
    print("Error: Nilai a harus lebih kecil dari b")
elif n <= 0:
    print("Error: Step size harus positif")
else:
    result = tabulasi(a, b, n)
    print("\nHasil Tabulasi:")
    print(result.to_string(index=False))
