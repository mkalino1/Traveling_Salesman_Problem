# Traveling_Salesman_Problem
Program rozwiązujący problem komiwojażera za pomocą kilku różnych algorytmów

## Algorytmy do wyboru:
1) Algorytm A* z heurystyką minimalnego drzewa rozpinającego
2) Algorytm A* z naiwną heurystyką sumującą najkrótsze z pozostałych odcinków
3) Algorymt Pierwszy Najlepszy
4) Algorytm Brute Force

Trzy pierwsze algorytmy są algorytmami przeszukiwania przestrzeni stanów, gdzie stanem jest częściowa droga komiwojażera.

Algorytm pierwszy najlepiej radzi sobie z problemem. Wynika to z tego, że minimalne drzewo rozpinające jest bardzo dobrym dolnym oszacowaniem pozostałej drogi.

## Przewodnik po projekcie:
Pierwszą częścią projektu jest skrypt generate_problem.py wywoływany z pojedyczym argumentem - liczbą będącą rozmiarem problemu. Dla zadanej liczby wygeneruje odpowiednią ilość miast do pliku z danymi.

Drugą, właściwą częscią projektu jest program rozwiązujący wygenerowany problem. Po wywołaniu pliku main.py użytkownik wybiera, którego algorytmu chce użyć, po czym po obliczeniu wyświetlana jest optymalna droga komiwojażera oraz odpowiednie statystyki (w tym czasowe), dzięki czemu użytkownik może porównywać ze sobą różne algorytmy.
