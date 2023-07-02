import pickle
from copy import deepcopy
from tqdm.auto import tqdm

from sklearn.model_selection import train_test_split
from models.basemodel import Model
from config import TARGET_PARAM

import pandas as pd

class ModelService():

    def __init__(self, model, pipelines):
        self.modelname = model
        self.model = Model(model)
        self.pipelines = deepcopy(pipelines)

    def train_split(self, df_train: pd.DataFrame, test_size, random_state):
        x = df_train.drop(columns=[TARGET_PARAM])
        y = df_train[TARGET_PARAM]
        X_train, X_val, y_train, y_val = train_test_split(x, y, test_size=test_size, random_state=random_state)
        return X_train, X_val, y_train, y_val

    def process(self):
        test_sizes = [0.05, 0.15, 0.2, 0.25]
        random_states = [12, 500, 1000]

        results = []

        for pipeline in tqdm(self.pipelines):
            for test_size in test_sizes:
                for random_state in random_states:
                    try:
                        pipe = deepcopy(pipeline)

                        X_train, X_val, y_train, y_val = self.train_split(pipe["df_train"], test_size, random_state)

                        self.model.fit(X_train, y_train)

                        pipe["y_pred_test"] = self.model.predict(pipe["df_test"])

                        pipe["y_pred_val"] = self.model.predict(X_val)
                        pipe["scores"] = self.model.get_scores(y_val, pipe["y_pred_val"])


                        pipe["description"] = f"{pipe['description']} test_size: {test_size}. random_state: {random_state}."

                        results.append(pipe)

                    except Exception as e:
                        results.append({"error": e})


        return results
