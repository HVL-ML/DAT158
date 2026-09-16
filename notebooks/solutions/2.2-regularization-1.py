def generate_data(m, seed):
    np.random.seed(seed)
    
    X = 3 * np.random.rand(m, 1)
    y = 1 + 0.5 * X + np.random.randn(m, 1) / 1.5

    return X, y

X_many, y_many = generate_data(10000, 2)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_many, y_many)

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train)

alpha = 0.001
degree = 10

ridge_reg = get_ridgereg(degree, alpha)

ridge_reg.fit(X_train, y_train)

# Score it on the validation set
print(ridge_reg.score(X_val, y_val))

# Score it on the test set
print(ridge_reg.score(X_test, y_test))

# Optional: use GridSearchCV
from sklearn.model_selection import GridSearchCV