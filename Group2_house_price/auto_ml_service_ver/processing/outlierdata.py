from processing.data import Data


class OutlierData(Data):

    def do_not_remove_outliers(self):
        """Не удалять выбросы"""
        return self.df_train, self.df_test
    def remove_target_outliers(self):
        """Удалить выбросы по целевой переменной"""
        Q1, Q3 = self.df_train[self.target_feature].describe()[['25%', '75%']]
        iqr = Q3 - Q1
        outlier_buttom = Q1 - 1.5 * iqr
        outlier_top = Q3 + 1.5 * iqr
        self.df_train = self.df_train[(outlier_buttom <= self.df_train[self.target_feature]) & (self.df_train[self.target_feature] <= outlier_top)]

        return self.df_train, self.df_test

    def remove_all_outliers(self):
        """Удалить выбросы по всем цифровым параметрам"""
        for param in self.num_features:
            Q1, Q3 = self.df_train[param].describe()[['25%', '75%']]
            iqr = Q3 - Q1
            outlier_buttom = Q1 - 1.5 * iqr
            outlier_top = Q3 + 1.5 * iqr
            self.df_train[param] = self.df_train[(outlier_buttom <= self.df_train[param]) & (
                        self.df_train[param] <= outlier_top)]

        return self.df_train, self.df_test

    def _get_method(self, methodname):
        if methodname == "remove_target_outliers":
            return self.remove_target_outliers()
        elif methodname == "remove_all_outliers":
            return self.remove_all_outliers()
        elif methodname == "do_not_remove_outliers":
            return self.do_not_remove_outliers()
