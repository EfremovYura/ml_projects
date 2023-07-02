import pickle

from service.modelservice import ModelService
from app.preprocessing import preprocess_data
from app.basepiplines import base_pipelines

from sklearn.linear_model import LinearRegression

from datetime import datetime

time_stats = []

print("Предобработка данных:")
start_time = datetime.now()

pipelines_to_model = preprocess_data(base_pipelines)
time_stats.append({"preprocess": datetime.now() - start_time,
                   "pipelines amount": len(pipelines_to_model)})

# # Сохраним в файл
# with open('pipelines_to_model.pickle', 'wb') as f:
#     pickle.dump(pipelines_to_model, file=f)

# with open('pipelines_to_model.pickle', 'rb') as handle:
#     pipelines_to_model = pickle.load(handle)
# time_stats.append({"preprocess load from pickle": datetime.now() - start_time,
#                    "pipelines amount": len(pipelines_to_model)})



print("LinearRegression work :")
start_time = datetime.now()

lr = LinearRegression()
ms = ModelService(lr, pipelines_to_model)

pipelines_with_result = ms.process()

time_stats.append({"LinearRegression": datetime.now() - start_time,
                   "pipelines amount": len(pipelines_with_result)})

# # Сохраним в файл
# with open('pipelines_with_result.pickle', 'wb') as f:
#     pickle.dump(pipelines_with_result, file=f)


# with open('pipelines_with_result.pickle', 'rb') as handle:
#     pipelines_to_model = pickle.load(handle)
# time_stats.append({"LinearRegression load from pickle": datetime.now() - start_time,
#                    "pipelines amount": len(pipelines_with_result)})
