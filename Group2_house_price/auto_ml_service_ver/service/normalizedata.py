from copy import deepcopy

from processing.normalizedata import NormilizeData
from tqdm.auto import tqdm


class NormalizeDataService():
    def __init__(self, pipilines, DataType=NormilizeData):
        self.DataType = DataType
        self.pipelines = deepcopy(pipilines)
        self.methods = [attribute for attribute in dir(self.DataType) if callable(getattr(self.DataType, attribute)) and attribute.startswith('__') is False and attribute.startswith('_') is False]


    def process(self):
        """Получить новые датасеты, путем нормализации предыдущих"""
        new_pipelines = []

        for pipeline in tqdm(self.pipelines):
            for method in tqdm(self.methods):
                new_pipeline = deepcopy(pipeline)

                try:
                    new_pipeline["df_train"], new_pipeline["df_test"] = self.DataType(new_pipeline["df_train"], new_pipeline["df_test"])._get_method(method)
                except Exception as e:
                    new_pipeline["error"] = e

                new_pipeline["description"] = f"{pipeline.get('description')} NormilizeData: {method}."
                new_pipelines.append(new_pipeline)
                print("description after", new_pipeline.get('description'))

        return new_pipelines
