from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

iris = load_iris()
X = iris.data
y = iris.target

# the default test_size is 0.2
(X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.4)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print(metrics.accuracy_score(y_test, y_pred))
