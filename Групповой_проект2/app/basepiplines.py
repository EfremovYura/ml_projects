import pickle

import pandas as pd
from config import TRAIN_SCV, TEST_CSV, DATA_DESCRIPTION
from description_parser import parse_data_description

df_train = pd.read_csv(TRAIN_SCV, sep = ',')
df_test = pd.read_csv(TEST_CSV, sep = ',')


# Список вариантов обработки данных, содержащий словари, состоящий из df_train, df_test и preprocessing_description
base_pipelines = []

#######################
# Базовый случай без изменений
base_pipeline = {"df_test": df_test,
                 "df_train": df_train,
                 "description": "Base: original datasets."
                 }

base_pipelines.append(base_pipeline)


#######################
# Удалим строки с пропусками в train
base_pipeline2 = {"df_test": df_test,
                 "df_train": df_train.dropna(axis=0),
                 "description": "Base: train dropna lines."
                 }
base_pipelines.append(base_pipeline2)


#######################
# Заполним пустые значения из файла description
cat_features_values = parse_data_description(DATA_DESCRIPTION)

df_train3 = df_train.astype({'MSSubClass': str})
df_test3 = df_test.astype({'MSSubClass': str})

cat_features = df_train3.select_dtypes(include='object').columns

for param in cat_features:
    for value in cat_features_values[param]:
        if (type(value) != int) and "NA=" in value:

            df_train3[param].fillna(value=value, inplace=True)

            df_test3[param].fillna(value=value, inplace=True)

base_pipeline3 = {"df_test": df_test3,
                 "df_train": df_train3,
                 "description": "Base: NA from description."
                 }
base_pipelines.append(base_pipeline3)


# Сохраним в файл
with open('base_pipelines.pickle', 'wb') as f:
    pickle.dump(base_pipelines, file=f)

