from config import DATA_DESCRIPTION
from processing.data import Data
from description_parser import parse_data_description


class NoneData(Data):
    """Обработка пропусков"""
    def dropna_columns(self):
        """Удаление столбцов, содержащими пустые значениями в train или test"""
        to_del = set()
        for param in self.all_features:

            # проверяем df_train на пустые значения в столбце
            has_null_values = any(self.df_train[param].isnull())

            if has_null_values:
                to_del.add(param)

            # проверяем df_test на пустые значения в столбце
            has_null_values = any(self.df_test[param].isnull())

            if has_null_values:
                to_del.add(param)

        to_del = list(to_del)

        self.df_train.drop(columns=to_del, inplace=True)
        self.df_test.drop(columns=to_del, inplace=True)

        return self.df_train, self.df_test

    def fillna_with_0(self):
        """Заполнение NA значениями нулями """

        self.df_train[self.cat_features] = self.df_train[self.cat_features].fillna(value="0")
        self.df_train[self.num_features] = self.df_train[self.num_features].fillna(value=0)

        self.df_test[self.cat_features] = self.df_test[self.cat_features].fillna(value="0")
        self.df_test[self.num_features] = self.df_test[self.num_features].fillna(value=0)

        return self.df_train, self.df_test

    def fillna_with_train_most_common_and_median(self):
        """
        Заполнение недостающих значений категориальных признаков - наиболее распространенным значением.
        Заполнение недостающих значений цифровых признаков - медианой.
        """
        for feature in self.cat_features:
            most_common = self.df_train[feature].describe()['top']
            self.df_train[feature].fillna(value=most_common, inplace=True)
            self.df_test[feature].fillna(value=most_common, inplace=True)

        for feature in self.num_features:
            median_val = self.df_train[feature].describe()['50%']
            self.df_train[feature].fillna(value=median_val, inplace=True)
            self.df_test[feature].fillna(value=median_val, inplace=True)

        return self.df_train, self.df_test

    def fillna_with_all_data_most_common_and_median(self):
        """
        Заполнение недостающих значений категориальных признаков - наиболее распространенным значением.
        Заполнение недостающих значений цифровых признаков - медианой.
        """
        for feature in self.cat_features:
            most_common = self.all_data[feature].describe()['top']
            self.df_train[feature].fillna(value=most_common, inplace=True)
            self.df_test[feature].fillna(value=most_common, inplace=True)

        for feature in self.num_features:
            median_val = self.df_train[feature].describe()['50%']
            self.df_train[feature].fillna(value=median_val, inplace=True)
            self.df_test[feature].fillna(value=median_val, inplace=True)

        return self.df_train, self.df_test

    def fillna_with_train_most_common_and_mean(self):
        """
        Заполнение недостающих значений категориальных признаков - наиболее распространенным значением.
        Заполнение недостающих значений цифровых признаков - средним.
        """

        for feature in self.cat_features:
            most_common = self.df_train[feature].describe()['top']
            self.df_train[feature].fillna(value=most_common, inplace=True)
            self.df_test[feature].fillna(value=most_common, inplace=True)

        for feature in self.num_features:
            median_val = self.df_train[feature].describe()['mean']
            self.df_train[feature].fillna(value=median_val, inplace=True)
            self.df_test[feature].fillna(value=median_val, inplace=True)

        return self.df_train, self.df_test


    def fillna_with_all_data_most_common_and_mean(self):
        """
        Заполнение недостающих значений категориальных признаков - наиболее распространенным значением.
        Заполнение недостающих значений цифровых признаков - средним.
        """

        for feature in self.cat_features:
            most_common = self.all_data[feature].describe()['top']
            self.df_train[feature].fillna(value=most_common, inplace=True)
            self.df_test[feature].fillna(value=most_common, inplace=True)


        for feature in self.num_features:
            median_val = self.df_train[feature].describe()['mean']
            self.df_train[feature].fillna(value=median_val, inplace=True)
            self.df_test[feature].fillna(value=median_val, inplace=True)

        return self.df_train, self.df_test

    def __fillna_num_params_with_prediction(self):
        """Заполнение недостающих значений цифровых признаков - предсказанием линейной регрессии."""
        pass

    def __fillna_cat_params_with_prediction(self):
        """Заполнение недостающих значений цифровых признаков - предсказанием {модель}."""
        pass

    def _get_method(self, methodname):
        if methodname == "dropna_columns":
            return self.dropna_columns()
        elif methodname == "fillna_with_0":
            return self.fillna_with_0()
        elif methodname == "fillna_with_train_most_common_and_median":
            return self.fillna_with_train_most_common_and_median()
        elif methodname == "fillna_with_all_data_most_common_and_median":
            return self.fillna_with_all_data_most_common_and_median()
        elif methodname == "fillna_with_train_most_common_and_mean":
            return self.fillna_with_train_most_common_and_mean()
        elif methodname == "fillna_with_all_data_most_common_and_mean":
            return self.fillna_with_all_data_most_common_and_mean()
