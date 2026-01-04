from sklearn.linear_model import LinearRegression

def train_model(X, y):
    """
    Train a simple interpretable model.
    """
    model = LinearRegression()
    model.fit(X, y)
    return model
