# install virtual environment
python -m pip install virtualenv

# check version
virtual --version

# create virtual environmet
virtualenv ml_package1

virtualenv ml_package2

# activate
# Linux/Mac => 
source ml_package1/bin/activate

# windows 
ml_package1\Scripts\activate
ml_package2\Scripts\activate

# change folder location where requirements.txt stored
D:
cd D:\Packaging-ML-Model\packaging_ml_model

# install requiremnts.txt
pip install -r requirements.txt

python training pipeline.py

# creating distribution package
python setup.py sdist bdist_wheel

# Upload your files & folder to git

# using distribution package from GIT
virtualenv ml_package2
ml_package2\Scripts\activate
pip install git+https://github.com/bipulshahi/loanapp.git

python
import Myloanapp
from Myloanapp import trainingpipeline
trainingpipeline.perform_training()
import pandas as pd
test_data = pd.read_csv('C:/Users/vipul/ml_package2/Lib/site-packages/Myloanapp/datasets/test_loan.csv')
from Myloanapp import predict
predict.generate_predictions(test_data[:1])

