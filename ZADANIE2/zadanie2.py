import re

def rzymskie_na_arabskie(rzymskie):
    # twój kod
    if not isinstance(rzymskie, str):
        raise TypeError("Wejście musi być typu str.")
    
    rzymskie = rzymskie.strip().upper()
    if not rzymskie:
        raise ValueError("Pusty łańcuch nie jest poprawną liczbą rzymską.")
    
    if not re.match(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", rzymskie):
        raise ValueError("Niepoprawny format liczby rzymskiej.")
    
    mapa = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    wartosc = 0
    i = 0
    while i < len(rzymskie):
        if i + 1 < len(rzymskie):
            pair = rzymskie[i:i+2]
            if pair in ("CM", "CD", "XC", "XL", "IX", "IV"):
                wartosc += mapa[pair[1]] - mapa[pair[0]]
                i += 2
                continue
        wartosc += mapa[rzymskie[i]]
        i += 1
    return wartosc

def arabskie_na_rzymskie(arabskie):
    # twój kod
    if not isinstance(arabskie, int):
        raise TypeError("Wejście musi być typu int.")
    
    if not (1 <= arabskie <= 3999):
        raise ValueError("Liczba musi być w zakresie 1-3999.")
    
    wartosci = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    rzymskie = ""
    for val, sym in wartosci:
        ile, arabskie = divmod(arabskie, val)
        rzymskie += sym * ile

    return rzymskie

if __name__ == '__main__':
    try:
        # Przykłady konwersji rzymskiej na arabską
        rzymska = "MCMXCIV"
        print(f"Liczba rzymska {rzymska} to {rzymskie_na_arabskie(rzymska)} w arabskich.")
        
        # Przykłady konwersji arabskiej na rzymską
        arabska = 1994
        print(f"Liczba arabska {arabska} to {arabskie_na_rzymskie(arabska)} w rzymskich.")
        
    except ValueError as e:
        print(e)
