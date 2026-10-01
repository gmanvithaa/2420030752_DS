import matplotlib.pyplot as plt

y1 = []
y2 = []

x = range(-100, 100, 10)

for i in x:
    y1.append(i**2)

for i in x:
    y2.append(-i**2)

plt.plot(x, y1,color='red')
plt.plot(x, y2,color='blue')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Simple Graph')
plt.axhline(color='lavender')

plt.axvline(color='blue')

plt.show()