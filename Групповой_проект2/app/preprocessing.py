import pickle
from copy import deepcopy

from tqdm.auto import tqdm

from service.encodedata import EncodeDataService
from service.nonedata import NoneDataService
from service.normalizedata import NormalizeDataService


def preprocess_data(base_pipelines):
    pipelines = deepcopy(base_pipelines)
    actions = [NoneDataService, EncodeDataService, NormalizeDataService]

    # Способы обработки пустых значений
    for action in tqdm(actions):

        pipelines = action(pipelines).process()

    return pipelines
