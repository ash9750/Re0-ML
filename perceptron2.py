import numpy as np

def check(index):
	is_correct = False
	if (cal(index) <= 0):
		is_correct = False
		update(index)
	else:
		is_correct = True
	return is_correct

def cal(index):
	global X, Y, Gram, alpha, b
	return Y[index] * (np.dot(alpha * Y.T, Gram[index].T) + b)

def update(index):
	global alpha, b, history, eta
	alpha[:, index] += eta
	b += Y[index] * eta
	history = np.vstack((history, alpha))

def train(dataset, step):
	global W, b
	for _ in range(step):
		for i, _ in enumerate(dataset):
			check(i)
	W = np.dot(alpha * Y.T, X)
	print("history: \n", history)
	print("result: ", W, b)

def gram(target_matrix):
	result = np.zeros((target_matrix.shape[0], target_matrix.shape[0]))
	for i in range(np.shape(train_set)[0]):
		target_matrix[i, :] = train_set[i][0][:-1]
	for i in range(np.shape(target_matrix)[0]):
		for j in range(np.shape(target_matrix)[0]):
			result[i][j] = np.dot(target_matrix[i].T, target_matrix[j])
	return result

def preprocess(dataset):
	X = np.zeros((np.shape(dataset)[0], np.shape([dataset[0][0][:-1]])[1]))
	Y = np.zeros((np.shape(dataset)[0], 1))
	for i in range(np.shape(dataset)[0]):
		Y[i] = dataset[i][1]
	return X, Y

train_set = [[(3,3,1), 1],[(4,3,1), 1],[(1,1,1),-1]]
W = np.array([[0,0]])
b = 0
eta = 1
num_step = 1000
X, Y = preprocess(train_set)
Gram = gram(X)
alpha = np.zeros((1,np.shape(train_set)[0]))
history = np.zeros((alpha.shape))

train(train_set, num_step)
