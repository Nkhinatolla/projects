import pandas as pd, sys
import numpy as np
from settings import *

class LogisticRegression:
    def __init__(self):
        self.train_x = []
        self.train_y = []
        # y = m * x + b
        self.theta = []
        # update times
        self.epoch = 5000
        # learning rate
        self.ETA = 0.01
        self.accuracy = 0
        self.log = []

    def get_datas(self, path=TRAINING_PATH, year=2017):
        datas = pd.read_csv(path)
        datas = datas[datas['Year'] == year]
        week_return = []
        adj_close = datas['Close'].iloc[0]
        data = []
        for i in range(len(datas)):
            week_return.append(datas['Return'].iloc[i])
            if datas['Weekday'].iloc[i] == 'Friday':
                mean = round(np.mean(week_return) * 100, 2)
                sd = round(np.std(week_return) * 100, 2)
                color = datas['Label'].iloc[i][0].lower()
                data.append([mean, sd, int(color == 'g')])
                adj_close = datas['Close'].iloc[i]
                week_return = []
        data = np.array(data)
        self.train_x = data[:, 0:2]
        self.train_y = data[:, 2]
        self.log.append((self.train_x, self.train_y))
        
    def add_data(self, new_x=None,new_y=None):
        self.train_x = list(self.train_x)
        self.train_y = list(self.train_y)
        if new_x[0] != None:
            self.train_x.append(new_x)
            self.train_y.append(new_y)
        self.train_x = np.array(self.train_x)
        self.train_y = np.array(self.train_y)
        self.log.append((self.train_x, self.train_y))

    def delete_data(self, new_x=None, new_y=None):
        self.train_x = list(self.train_x)
        self.train_y = list(self.train_y)
        min_dis = 1000
        pos = -1
        if new_x[0] != None:
            for i in range(len(self.train_x)):
                d = self.distance(self.train_x[i], new_x)
                if min_dis > d:
                    min_dis = d
                    pos = i
            if pos != -1:
                self.train_x.pop(pos)
                self.train_y.pop(pos)
        self.train_x = np.array(self.train_x)
        self.train_y = np.array(self.train_y)
        self.log.append((self.train_x, self.train_y))

    def fit(self):
        # initialize parameter
        self.theta = np.zeros(self.train_x.shape[1]+1)
         # # standardization
        # mu = self.train_x.mean(axis=0)
        # sigma = self.train_x.std(axis=0)
        # std_x = self.standardizer(self.train_x, mu, sigma)
        self.mat_x = self.to_matrix(self.train_x)
        
    def standardizer(self, x, mu, sigma):
        return (x - mu) / sigma

    # get matrix
    def to_matrix(self, std_x):
        return np.array([[1, x1, x2] for x1, x2 in std_x])

    # sigmoid function
    def __sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
        
    def get_line(self, game):
        z = np.dot(self.mat_x, self.theta)
        h = self.__sigmoid(z)

        gradient = np.dot(self.mat_x.T, (h - self.train_y)) / len(self.train_y)
        self.theta -= self.ETA * gradient
        # self.theta = self.theta - self.ETA * np.dot(self.f(self.mat_x) - self.train_y, self.mat_x)
        y_new = []
        y_altered = []
        for x, y in self.train_x:
            new_y = -(self.theta[0] + x * self.theta[1]) / self.theta[2]
            if new_y >= y:
                y_new.append(1)
            else:
                y_new.append(0)
            y_altered.append(1 - y_new[-1])
        self.accuracy = max(self.get_accuracy(y_new, self.train_y), self.get_accuracy(y_altered, self.train_y))
        x1 = np.linspace(-2, 3, 100)
        x2 = - (self.theta[0] + x1 * self.theta[1]) / self.theta[2]
        return (x1, x2)

    def get_accuracy(self, pred, test_y):
        correct = 0
        for i in range(len(test_y)):
            correct += test_y[i] == pred[i]
        return  round((correct / len(test_y)) * 100, 2)

    def distance(self, x, y):
        return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5 