from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, mean_absolute_error


class Model():

    def __init__(self, model):
        self.model = model

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def get_scores(self, y_valid, y_pred):
        # словарь с оценками
        scores = {}

        scores['root_mean_squared_error']  = mean_squared_error(y_valid, y_pred, squared=False)
        scores['mean_squared_error'] = mean_squared_error(y_valid, y_pred)
        scores['mean_absolute_error'] = mean_absolute_error(y_valid, y_pred)
        scores['mean_absolute_percentage_error'] = mean_absolute_percentage_error(y_valid, y_pred)

        return scores

    def feature_importances(self):
        pass
        # # Посмотрим на важность признаков (feature_importances_) в модели регрессии и проанализируем топ признаки
        # sorted(zip(X_train.columns, model_reg.feature_importances_), key=lambda x: -x[1])
