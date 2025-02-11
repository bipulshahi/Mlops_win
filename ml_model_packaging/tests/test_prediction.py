
import pytest
import sys
import pathlib


#print(str(pathlib.Path(__file__).resolve().parents[2]))
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
import Myloanapp

from Myloanapp.config import config
from Myloanapp.predict import generate_predictions
from Myloanapp.processing.data_handling import load_dataset


# Output from predict script is not null
# Output from predict script is str data type
# The output is Y for an example data

@pytest.fixture
def single_prediction():
    test_dataset = load_dataset(config.TEST_FILE)
    single_row = test_dataset[:1]
    result = generate_predictions(single_row)
    return result


def test_single_pred_not_none(single_prediction):           #output is not none
    assert single_prediction is not None


def test_single_pred_str_type(single_prediction):
    assert isinstance(single_prediction.get('Predictions')[0],str)


def test_single_pred_validate(single_prediction):
    assert single_prediction.get('Predictions')[0] == 'Y'

