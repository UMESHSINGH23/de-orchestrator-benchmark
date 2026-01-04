from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(model, X, y):
    """
    Evaluate model performance.
    """
    preds = model.predict(X)

    metrics = {
        "rmse": mean_squared_error(y, preds, squared=False),
        "r2": r2_score(y, preds)
    }

    return metrics
