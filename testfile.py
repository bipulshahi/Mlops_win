import packaging_ml_model
import pathlib

print(packaging_ml_model.__file__)

print(pathlib.Path(packaging_ml_model.__file__).resolve().parent)