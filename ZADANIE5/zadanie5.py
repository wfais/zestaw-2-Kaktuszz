import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify

# Funkcja rysująca wykres na podstawie eval()
def rysuj_wielomian(wejscie):
    # Generowanie wartości x i y przy użyciu eval()
    # Rysowanie wykresu ale bez show()
    func_str, interval = wejscie.split(",")
    start, stop = map(float, interval.split())
    x = np.linspace(start, stop, 200)
    y_val = eval(func_str, {"np": np, "x": x})

    if np.isscalar(y_val):
        y_val = np.full_like(x, y_val, dtype=float)

    plt.plot(x, y_val, label=f"Eval: {func_str}")
    plt.xlabel("x")
    plt.ylabel("f(x)")

    # Zwracanie wartości na granicach przedziału
    return y_val[0], y_val[-1]

# Funkcja rysująca wykres na podstawie SymPy i lambdify()
def rysuj_wielomian_sympy(wejscie):
    # Definicja symbolu i konwersja do funkcji numerycznej za pomocą SymPy
    # Generowanie wartości x i y przy użyciu funkcji numerycznej
    # Rysowanie wykresu ale bez show()

    func_str, interval = wejscie.split(",")
    start, stop = map(float, interval.split())

    x = symbols('x')
    func_sympy = sympify(func_str)
    func_num = lambdify(x, func_sympy, modules=["numpy"])

    x_vals = np.linspace(start, stop, 200)
    y_val_sympy = func_num(x_vals)

    plt.plot(x_vals, y_val_sympy, label=f"SymPy: {func_str}", linestyle='--')
    plt.xlabel("x")
    plt.ylabel("f(x)")

    # Zwracanie wartości na granicach przedziału
    return y_val_sympy[0], y_val_sympy[-1]

if __name__ == '__main__':
    # Przykładowe wywołanie pierwszej funkcji
    wejscie1 = "x**3 + 3*x + 1, -10 10"
    
    # Pierwszy wykres z eval
    wynik_eval = rysuj_wielomian(wejscie1)
    print("Wynik (eval):", wynik_eval)
    
    # Drugie wejście dla funkcji SymPy - bardziej złożona funkcja 
    wejscie2 = "x**4 - 5*x**2 + 3*sin(x), -10 10"  
    
    # Drugi wykres z SymPy
    wynik_sympy = rysuj_wielomian_sympy(wejscie2)
    print("Wynik (SymPy):", wynik_sympy)
    
    # Wyświetlanie obu wykresów
    plt.show()
