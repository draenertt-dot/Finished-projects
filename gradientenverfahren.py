import matplotlib.pyplot as plt, random

def f(x): 
    return x ** 2

def df(x):
    return 2 * x

def g(x):
    return 0.1 * x**6 - 1.5 * x**4 + 4 * x**2 + x

def dg(x):
    return 0.6 * x**5 - 6 * x**3 + 8 * x + 1

X = [x/250 for x in range (-1000,1001)]
y = [g(x) for x in X]


max_iterationen = 1000

     
for x in range(1, 1000):

    x_start = random.choice(X)

    x_verlauf = [x_start]
    for iteration in range(max_iterationen):
        x_iteration = x_verlauf[iteration]

        steigung_x_iteration = dg(x_iteration)

        x_neu = x_iteration - 0.01 * steigung_x_iteration

    
    y_neu = g(x_neu)
    if y_neu < min_y:
        min_y = y_neu
        x_bei_min_y = x_neu
        
    x_verlauf.append(x_neu)

    def minimum(x_verlauf: list) -> float:
        
        return min(x_verlauf, key=lambda x: g(x))

plt.plot(X,y)
plt.scatter(x_verlauf, [g(x) for x in x_verlauf])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Funktionsgraph")
plt.show()