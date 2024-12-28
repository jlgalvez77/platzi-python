# Hallar la sumatoria de un número n usando funciones recursivas.

def sumatoria(n):
    if n == 0:
        return 0
    else:
        return n + sumatoria(n - 1)
    
print(sumatoria(5))  # 15