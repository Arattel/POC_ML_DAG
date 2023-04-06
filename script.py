import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import time
import pickle as pkl

iris = load_iris()
data = pd.DataFrame(iris.data)
data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
target = pd.DataFrame(iris.target)
target = target.rename(columns = {0: 'target'})
df = pd.concat([data, target], axis = 1)

X = df.copy()
y = X.pop('target')

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1, stratify = y)

model = LogisticRegression()

model.fit(X_train, y_train)

print(model.score(X_test, y_test))

predictions = model.predict(X_test)

res = pd.DataFrame(predictions)
X_test = X_test.reset_index().drop('index', axis=1)
results = pd.concat([X_test, res], axis=1)
timestr = time.strftime("%Y%m%d-%H%M%S")

with open('model.pkl', 'wb') as f:
    pkl.dump(model, f)
results.to_csv(f'results_{timestr}.csv')