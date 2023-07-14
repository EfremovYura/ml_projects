from sklearn.preprocessing import LabelEncoder
from category_encoders import TargetEncoder
from processing.data import Data


class EncodeData(Data):

    def label_encode_on_train(self):
        """Кодирование c LabelEncoder(), обучение на train """
        for param in self.cat_features:
            self.le = LabelEncoder()
            self.le.fit(self.df_train[param])

            self.df_train[param] = self.le.transform(self.df_train[param])
            self.df_test[param] = self.le.transform(self.df_test[param])

        return self.df_train, self.df_test

    def label_encode_on_all_data(self):
        """Кодирование c LabelEncoder(), обучение на all_data """
        for param in self.cat_features:
            self.le = LabelEncoder()
            self.le.fit(self.all_data[param])

            self.df_train[param] = self.le.transform(self.df_train[param])
            self.df_test[param] = self.le.transform(self.df_test[param])

        return self.df_train, self.df_test

    def target_encode(self):
        """Кодирование c TargetEncoder(), обучение на train """
        for param in self.cat_features:
            self.te = TargetEncoder(min_samples_leaf=20, smoothing=10)
            self.te.fit(self.df_train[param], self.df_train[self.target_feature])

            self.df_train[param] = self.te.transform(self.df_train[param])
            self.df_test[param] = self.te.transform(self.df_test[param])

        return self.df_train, self.df_test

    def _get_method(self, methodname):
        if methodname == "label_encode_on_train":
            return self.label_encode_on_train()
        elif methodname == "label_encode_on_all_data":
            return self.label_encode_on_all_data()
        elif methodname == "target_encode":
            return self.target_encode()
