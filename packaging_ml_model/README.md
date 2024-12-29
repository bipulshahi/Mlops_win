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

# install required python version
* Download the Python 3.12 installer for your operating system from the official Python website.
* Install Python 3.12 but do not add it to PATH during installation if you're on Windows. This ensures it doesn't interfere with the default Python.
* pip install virtualenv
* virtualenv -p C:\Users\vipul\AppData\Local\Programs\Python\Python312\python.exe ml_package1
* 

# using distribution package from GIT
* ml_package1\Scripts\activate
* pip install git+https://github.com/bipulshahi/loanapp.git

* python
* import Myloanapp
* from Myloanapp import trainingpipeline
* trainingpipeline.perform_training()
* import pandas as pd
* test_data = pd.read_csv('C:/Users/vipul/ml_package2/Lib/site-packages/Myloanapp/datasets/test_loan.csv')
* from Myloanapp import predict
* predict.generate_predictions(test_data[:1])

