# Language Recognize

## Contents
- [About](#about)
  - [Description](#description)
  - [Data Sources](#data-sources)
- [Repository Contents](#repository-contents)
- [Bucket Organization](#bucket-organization)
- [Data Processing](#data-preprocessing)
- [API](#api)
  - [Run Server Locally](#run-server-locally)
  - [Run with Docker](#run-with-docker)

## About

### Description
The idea of this project is to develop a basic ML model to recognize the language a given
text is written in and deploy it to an instance on AWS so that it can be consulted.

### Data Sources
The data we are using to train the model is from the following sources:
- [Wikibooks Dataset](https://www.kaggle.com/dhruvildave/wikibooks-dataset)
- [TED Talks Dataset](https://www.kaggle.com/miguelcorraljr/ted-ultimate-dataset)

## Repository Contents
- The `notebooks` directory contains Jupyter notebooks for data exploration and model development. 
- The `data-preparation` directory contains scripts and utilities to prepare the dataset for
  the models.
- The `service` directory contains the code for running and deploying the model as an HTTP API.

## Bucket Organization
The S3 bucket of the project is organized as follows:
- `raw-data/` contains the raw data as downloaded from the datasets.
- `data-preparation/` contains the necessary scripts and utilities to prepare the data for the model.

## Data Preprocessing
Since the model will be trained using a TensorFlow text line dataset, the data must be organized along
the following structure:
```
output_dir
  - Language1
    - Text1.txt
    - Text2.txt
    ...
  - Language2
    - Text1.txt
    ...
```
In order to prepare the data from the TED dataset csvs and store it in this format, you can run
the `data-preparation/make_dataset` script as follows:
```shell
python data-preparation/make_dataset.py --input_dir=data/raw-data/ted-dataset
```
You can pass the following optional arguments as well:
- `--output_dir=<directory to store output>`
- `--col_name=<name of column with text in the csvs>`

## API

### Run Server Locally
To run the model server locally, first install the required dependencies from `service/src/requirements.txt`.
If your python version is *different* from 3.7, you must install the appropriate version of 
`tflite_runtime` from [here](https://github.com/google-coral/pycoral/releases/tag/v2.0.0).
Next, ensure you have saved the prediction model in
[tflite format](https://www.tensorflow.org/lite/guide) in `service/src/assets/model.tflite`,
and then go to the `service/src` directory and start the server with:
```shell
uvicorn main:app
```
Then you can consult the model via `HTTP` requests. The documentation url for the API is
`/docs`.

### Run with Docker
In order to run the service with docker, first navigate to the `service` directory and build
the image with
```shell
docker build -t language-recognize .
```
Then you can start the service with
```shell
docker run --name lang-recognize-container -p 3000:3000 language-recognize
```

[Back to top.](#language-recognize)
