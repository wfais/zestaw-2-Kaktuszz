import os
import time
import threading
import sys

# Stałe konfiguracyjne
LICZBA_KROKOW = 80_000_000
LICZBA_WATKOW = sorted({1, 2, 4, os.cpu_count() or 4})


def policz_fragment_pi(pocz: int, kon: int, krok: float, wyniki: list[float], indeks: int) -> None:
    # Funkcja oblicza częściową sumę przybliżenia liczby pi metodą prostokątów.
    # Argumenty:
    #     pocz, kon - zakres iteracji (indeksy kroków całkowania),
    #     krok      - szerokość pojedynczego prostokąta (1.0 / LICZBA_KROKOW),
    #     wyniki    - lista, do której należy wpisać wynik dla danego wątku na pozycji indeks,
    #     indeks    - numer pozycji w liście 'wyniki' do zapisania rezultatu.

    # Każdy wątek powinien:
    #   - obliczyć lokalną sumę dla przydzielonego przedziału,
    #   - wpisać wynik do wyniki[indeks].

    lokalna_suma = 0.0
    for i in range(pocz, kon):
        x_i = (i + 0.5) * krok
        
        lokalna_suma += 4.0 / (1.0 + x_i * x_i)
    
    wyniki[indeks] = lokalna_suma  # zaimplementuj obliczanie fragmentu całki dla danego wątku


def main():
    print(f"Python: {sys.version.split()[0]}  (tryb bez GIL? {getattr(sys, '_is_gil_enabled', lambda: None)() is False})")
    print(f"Liczba rdzeni logicznych CPU: {os.cpu_count()}")
    print(f"LICZBA_KROKOW: {LICZBA_KROKOW:,}\n")

    # Wstępne uruchomienie w celu stabilizacji środowiska wykonawczego
    krok = 1.0 / LICZBA_KROKOW
    wyniki = [0.0]
    w = threading.Thread(target=policz_fragment_pi, args=(0, LICZBA_KROKOW, krok, wyniki, 0))
    w.start()
    w.join()

    czas_1_watek = 0.0

    # ---------------------------------------------------------------
    # Tu zaimplementować:
    #   - utworzenie wielu wątków (zgodnie z LICZBY_WATKOW),
    #   - podział pracy na zakresy [pocz, kon) dla każdego wątku,
    #   - uruchomienie i dołączenie wątków (start/join),
    #   - obliczenie przybliżenia π jako sumy wyników z poszczególnych wątków,
    #   - pomiar czasu i wypisanie przyspieszenia.
    # ---------------------------------------------------------------

    for n_watkow in LICZBA_WATKOW:
        print(f"\n--- Obliczenia dla {n_watkow} wątku/ów ---")
        wyniki = [0.0] * n_watkow
        watki = []
        krokow_na_watek = LICZBA_KROKOW // n_watkow
        pocz = 0
        start_time = time.perf_counter()

        for i in range(n_watkow):
            kon = pocz + krokow_na_watek
            if i == n_watkow - 1:
                kon = LICZBA_KROKOW
            
            watek = threading.Thread(
                target=policz_fragment_pi,
                args=(pocz, kon, krok, wyniki, i)
            )
            watki.append(watek)
            watek.start()

            pocz = kon

        for watek in watki:
            watek.join()

        end_time = time.perf_counter()
        czas_wykonania = end_time - start_time   

        calka_suma = sum(wyniki)

        pi = krok * calka_suma

        print(f"Obliczone Pi: {pi:.12f}")
        print(f"Czas:         {czas_wykonania:.4f} s")

        if n_watkow == 1:
            czas_1_watek = czas_wykonania
            print("Przyspieszenie: 1.00x (baza)")
        else:
            if czas_1_watek > 0:
                przyspieszenie = czas_1_watek / czas_wykonania
                print(f"Przyspieszenie: {przyspieszenie:.2f}x")
            else:
                print("Przyspieszenie: B/D (brak czasu bazowego)")

if __name__ == "__main__":
    main()
