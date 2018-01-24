import numpy as np
import random
import matplotlib.pyplot as plt

N = 100
np.random.seed(1000)

def scatter(x, y, c):
	colors = []
	for i in range(len(c)):
		if c[i] == 0:
			colors.append('r')
		else:
			colors.append('b')
	plt.scatter(x, y, c = colors, s = 3)
	plt.show()

def createData(kind):
	x = []
	y = []
	c = []
	if kind == 0: 
		# linear seperable
		# Setting: class 0: (-5, 5)
		#          class 1: (5, -5)
		#          variance: 3
		for i in range(N):
			x.append(np.random.normal(-5, 2))
			y.append(np.random.normal(5, 2))
			c.append(0)
			x.append(np.random.normal(5, 2))
			y.append(np.random.normal(-5, 2))
			c.append(1)
	if kind == 1:
		# not linear seperable
		for i in range(N):
			while True:
				temX = np.random.normal(0, 10)
				temY = np.random.normal(0, 10)
				if temX > 3 and temY > 3:
					x.append(temX)
					y.append(temY)
					c.append(0)
					break
			while True:
				temX = np.random.normal(0, 10)
				temY = np.random.normal(0, 10)
				if temX < -3 or temY < -3:
					x.append(temX)
					y.append(temY)
					c.append(1)
					break
	# shuffle
	for i in range(10000):
		id1 = random.randint(0, 2 * N - 1)
		id2 = random.randint(0, 2 * N - 1)
		x[id1], x[id2] = x[id2], x[id1]
		y[id1], y[id2] = y[id2], y[id1]
		c[id1], c[id2] = c[id2], c[id1]

	return x, y, c

if __name__ == "__main__":
	x, y, c = createData(1)
	scatter(x, y, c)