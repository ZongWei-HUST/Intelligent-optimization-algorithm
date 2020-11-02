import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [0.2067, 0.9440, 0.9961, 0.9972, 0.9958, 0.9987, 0.9981, 0.9987, 0.9972,]

plt.plot(x, y, marker='*', color='r')
plt.xlabel('epoch')
plt.ylabel('Accuracy')

plt.show()