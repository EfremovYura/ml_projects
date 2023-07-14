from copy import deepcopy

from processing.nonedata import NoneData
from tqdm.auto import tqdm


class NoneDataService():
    def __init__(self, pipilines: list, DataType=NoneData):
        self.DataType = DataType
        self.pipelines = pipilines
        self.methods = [attribute for attribute in dir(self.DataType) if callable(getattr(self.DataType, attribute)) and attribute.startswith('__') is False and attribute.startswith('_') is False]


    def process(self):
        """Варианты заполнения пропусков"""
        new_pipelines = []

        for pipelene in tqdm(self.pipelines):
            for method in tqdm(self.methods):

                new_pipeline = deepcopy(pipelene)

                new_pipeline["df_train"], new_pipeline["df_test"] = self.DataType(new_pipeline["df_train"], new_pipeline["df_test"])._get_method(method)

                new_pipeline["description"] = f"{new_pipeline['description']} NoneData: {method}."

                new_pipelines.append(new_pipeline)

        return new_pipelines
    
