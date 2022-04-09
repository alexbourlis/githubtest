import matplotlib.pyplot as plt

def sort(X,Y,Z):
    sorting = True
    iterations = len(X)-1
    while(sorting):
        sorting = False
        for i in range(iterations):
            if Y[i]>Y[i+1]:
                buffer = Y[i]
                Y[i] = Y[i+1]
                Y[i+1] = buffer
                buffer = X[i]
                X[i] = X[i + 1]
                X[i + 1] = buffer
                buffer = Z[i]
                Z[i] = Z[i + 1]
                Z[i + 1] = buffer
                sorting = True
        iterations -= 1
    return X,Y,Z

data = [[1985, 21580, 14.06], [1986, 21440, 14.13], [1987, 21340, 14.27], [1988, 21281, 14.31], [1989, 21262, 14.19],
        [1990, 21283, 14.38], [1991, 21344, 14.35], [1992, 21445, 14.13], [1993, 21588, 14.14], [1994, 21772, 14.24],
        [1995, 21999, 14.38], [1996, 22270, 14.30], [1997, 22587, 14.40], [1998, 22952, 14.57], [1999, 23366, 14.33],
        [2000, 23833, 14.33], [2001, 24355, 14.48], [2002, 24934, 14.56], [2003, 25576, 14.55], [2004, 26283, 14.49],
        [2005, 27061, 14.63]]

rows = len(data)
col = len(data[0])
X = []
Y = []
Z = []
for i in range(rows):
    X.append(data[i][0])
    Y.append(data[i][1])
    Z.append(data[i][2])

fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(X,Z, 'o-')
X,Y,Z = sort(X,Y,Z)
axs[1].plot(Y,Z, 'o-')
plt.show()
