from copy import deepcopy

from processing.outlierdata import OutlierData
from tqdm.auto import tqdm


class OutlierDataService():
    def __init__(self, pipilines, DataType=OutlierData):
        self.DataType = DataType
        self.pipelines = pipilines
        self.methods = [attribute for attribute in dir(self.DataType) if callable(getattr(self.DataType, attribute)) and attribute.startswith('__') is False and attribute.startswith('_') is False]


    def process(self):
        """Получить новые датасеты, путем обработки предыдущих"""
        new_pipelines = []

        for pipeline in tqdm(self.pipelines):
            for method in self.methods:

                new_pipeline = deepcopy(pipeline)
                try:
                    new_pipeline["df_train"], new_pipeline["df_test"] = self.DataType(pipeline["df_train"], pipeline["df_test"])._get_method(method)
                    new_pipeline["description"] = f"{pipeline['description']} OutlierData: {method}."
                    new_pipelines.append(new_pipeline)
                except Exception as e:
                    new_pipeline["error"] = e

        return new_pipelines
