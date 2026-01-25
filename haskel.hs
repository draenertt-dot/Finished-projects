mal2 :: Int -> Int
mal2 x = 2*x

quadrat :: Int -> Int
quadrat x = x*x

fibo :: Int -> Int
fibo 0 = 0
fibo 1 = 1
fibo x = fibo( x - 1) + fibo(x - 2)

-- Wie viele Möglichkeiten gibt es, x Elemente unter Berücksichtigung ihrer Reihenfolger anzuordnen?
faku :: Int -> Int
faku 0 = 1
faku x = faku(x - 1) * x

hoch :: Int -> Int
hoch 0 = 1
hoch x = hoch(x - 1) * 2

summe :: Int -> Int
summe 0 = 0
summe x = summe( x - 1) + x

xHochY :: Int -> Int -> Int
xHochY 0 x = 1
xHochY x 0 = 1
xHochY x y = xHochY(x) (y - 1) * x

-- Wie viele Möglichkeiten gibt es, n Elemente unter Berücksichtigung ihrer Reihenfolger anzuordnen?
-- Antwort: n! (n Fakultät, n * (n-1) * (n-2) * ... * 2 * 1). Für das erste Element gibt es n Möglichkeiten,
-- für das zweite noch (n-1) Möglichkeiten, für das dritte noch (n-2) Möglichkeiten, ..., für das vorletzte
-- zwei, für das letzte eine.
-- Wie viele Möglichkeiten gibt es, k Elemente aus n Elementen unter Berücksichtigung ihrer Reihenfolge
-- anzuordnen? (Zum Beispiel: Wir möchten 3 Elemente aus [1,2,3,4,5] unter Berücksichtigung ihrer
-- Reihenfolge anordnen. Wie viele gibt es für die erste Zahl? 5. Wie viele
-- gibt es für die zweite Zahl? 4. Wie viele gibt es für die dritte Zahl? 3. Also: 5 * 4 * 3 = 60. Wir multiplizieren,
-- da wir die einzelnen Möglichkeiten unabhängig voneinander miteinander kombinieren können. So wie es auch
-- 6 * 6 = 36 mögliche Ergebnisse dabei gibt, zwei Würfel zu werfen. Jede Augenzahl des ersten Würfels kann mit
-- jeder Augenzahl des zweiten Würfels kombiniert werden.) Die allgemeine Formel lautet: TODOTODOTODOTODO vom 17.07.25. Bis nächste Woche!

-- TODO vom 26.06.2025
-- Hinweis: div 9 2 ist 9 geteilt durch 2 ohne Nachkommastellen, also 4
-- Nachschauen, was der Binomialkoeffizient ist (aber nicht gleich eine Haskellfunktion dafür)
binomialkoeffizient :: Int -> Int -> Int
binomialkoeffizient n 0 = 1
binomialkoeffizient n k
    | n == k = 1
    | otherwise = binomialkoeffizient (n - 1) k + binomialkoeffizient (n - 1) (k - 1)

-- das sieht nicht lauffähig aus
-- n = 5
-- k = 3

-- man sollte eine der zuvor geschriebenen funktionen verwenden
-- man gibt ihr zwei zahlen (n und k) und sie soll den binomialkoeffizienten von n und k zurückgebenx
-- Todo liste nach ferien:
    -- Github account machen udn alles bisherige dokumentieren
    -- neues projekt beginnen. Am besten etwas neues bei dem ich auch lernen kann.

erstesElement :: [Int] -> Int
erstesElement [] = error "Leere Liste!"
erstesElement (x:xs) = x

zweitesElement :: [Int] -> Int
zweitesElement [] = error "Leere Liste!"
zweitesElement [x] = error "Liste besitzt nur ein Element!"
zweitesElement (x:y:ys) = y

zweitesElementAlt :: [Int] -> Int
zweitesElementAlt (x:y:ys) = y
zweitesElementAlt _ = error "Liste zu kurz!"

letztesElement :: [Int] -> Int