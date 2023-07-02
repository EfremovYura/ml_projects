from processing.data import Data
from sklearn.preprocessing import StandardScaler, RobustScaler


class NormilizeData(Data):

    def standart_scaler_on_all_data(self):
        """Нормализация с помощью StandartScaler"""

        self.scaler = StandardScaler()
        self.scaler.fit(self.all_data)

        self.df_train[self.num_features] = self.scaler.transform(self.df_train[self.num_features])
        self.df_test[self.num_features] = self.scaler.transform(self.df_test[self.num_features])

        return self.df_train, self.df_test

    def standart_scaler_on_train(self):
        """Нормализация с помощью StandartScaler"""

        self.scaler = StandardScaler()
        self.scaler.fit(self.df_train.drop(columns=[self.target_feature]))

        self.df_train[self.num_features] = self.scaler.transform(self.df_train[self.num_features])
        self.df_test[self.num_features] = self.scaler.transform(self.df_test[self.num_features])

        return self.df_train, self.df_test

    def min_max_scaler_on_train(self):
        """Нормализация с помощью min\max на train"""
        for param in self.num_features:

            # self.df_train[param] = (self.df_train[param] - self.df_train[param].min(axis=0)) / (self.df_train[param].max(axis=0) - self.df_train[param].min(axis=0))
            # self.df_test[param] = (self.df_test[param] - self.df_train[param].min(axis=0)) / (self.df_train[param].max(axis=0) - self.df_train[param].min(axis=0))

            self.df_train[param] = (self.df_train[param] - self.df_train[param].min()) / (self.df_train[param].max() - self.df_train[param].min())
            self.df_test[param] = (self.df_test[param] - self.df_train[param].min()) / (self.df_train[param].max() - self.df_train[param].min())

        return self.df_train, self.df_test

    def min_max_scaler_on_all_data(self):
        """Нормализация с помощью min\max на all_data"""
        for param in self.num_features:
            # self.df_train[param] = (self.df_train[param] - self.all_data[param].min(axis=0)) / (self.all_data[param].max(axis=0) - self.all_data[param].min(axis=0))
            # self.df_test[param] = (self.df_test[param] - self.all_data[param].min(axis=0)) / (self.all_data[param].max(axis=0) - self.all_data[param].min(axis=0))

            self.df_train[param] = (self.df_train[param] - self.all_data[param].min()) / (self.all_data[param].max() - self.all_data[param].min())
            self.df_test[param] = (self.df_test[param] - self.all_data[param].min()) / (self.all_data[param].max() - self.all_data[param].min())

        return self.df_train, self.df_test


    # def robust_scaler_on_train(self):
    #     """Нормализация с помощью RobustScaler"""
    #
    #     self.scaler = RobustScaler()
    #     self.scaler.fit(self.df_train[self.num_features])
    #
    #     self.df_train[self.num_features] = self.scaler.transform(self.df_train[self.num_features])
    #     self.df_test[self.num_features] = self.scaler.transform(self.df_test[self.num_features])
    #
    #     return self.df_train, self.df_test
    #
    # def robust_scaler_on_all_data(self):
    #     """Нормализация с помощью RobustScaler"""
    #
    #     self.scaler = RobustScaler()
    #     self.scaler.fit(self.all_data[self.num_features])
    #
    #     self.df_train[self.num_features] = self.scaler.transform(self.df_train[self.num_features])
    #     self.df_test[self.num_features] = self.scaler.transform(self.df_test[self.num_features])
    #
    #     return self.df_train, self.df_test
    #

    def _get_method(self, methodname):
        if methodname == "standart_scaler_on_all_data":
            return self.standart_scaler_on_all_data()
        elif methodname == "standart_scaler_on_train":
            return self.standart_scaler_on_train()
        elif methodname == "min_max_scaler_on_train":
            return self.min_max_scaler_on_train()
        elif methodname == "min_max_scaler_on_all_data":
            return self.min_max_scaler_on_all_data()
        # elif methodname == "robust_scaler_on_train":
        #     return self.robust_scaler_on_train()
        # elif methodname == "robust_scaler_on_all_data":
        #     return self.robust_scaler_on_all_data()