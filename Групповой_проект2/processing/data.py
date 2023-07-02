from copy import deepcopy
import pandas as pd
from config import TARGET_PARAM


class Data:
    def __init__(self, df_train: pd.DataFrame, df_test: pd.DataFrame):
        self.df_train = deepcopy(df_train)
        self.df_test = deepcopy(df_test)
        self.target_feature = TARGET_PARAM
        # self.all_features = self.df_train.drop(columns=[self.target_feature]).columns
        self.all_features = self.df_test.columns
        self.all_data = pd.concat([self.df_train.drop(columns=[self.target_feature]), self.df_test], ignore_index=True)
        self.cat_features = self.df_train.select_dtypes(include='object').columns
        self.num_features = self.df_train.drop(columns=[self.target_feature]).select_dtypes(exclude='object').columns
        # self.cat_features = list(set(self.df_train.select_dtypes(include='object').columns).intersection(set(self.df_test.select_dtypes(include='object').columns)))
        # self.num_features = list(set(self.df_train.select_dtypes(exclude='object').columns).intersection(set(self.df_test.select_dtypes(exclude='object').columns)))


