import logging

try:
    from sklearn.model_selection import train_test_split
except ImportError:
    from sklearn.cross_validation import train_test_split

from sklearn.datasets import make_regression
from mla.linear_models import LinearRegression, LogisticRegression
from mla.metrics.metrics import mean_squared_error, accuracy

# Change to DEBUG to see convergence
logging.basicConfig(level=logging.ERROR)


def regression():
    # Generate a random regression problem
    X, y = make_regression(
        n_samples=10000, n_features=100, n_informative=75, n_targets=1, noise=0.05, random_state=1111, bias=0.5
    )
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1111)

    model = LinearRegression(lr=0.01, max_iters=2000, penalty="l2", C=0.03)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("regression mse", mean_squared_error(y_test, predictions))