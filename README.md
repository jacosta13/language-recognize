# Language Recognize

## Contents
- [About](#about)
  - [Description](#description)
  - [Data Sources](#data-sources)
- [Repository Contents](#repository-contents)
- [Bucket Organization](#bucket-organization)

## About

### Description
The idea of this project is to develop a basic ML model to recognize the language a given
text is written in and deploy it to an instance on AWS so that it can be consulted.

### Data Sources
The data we are using to train the model is from the following sources:
- [Wikibooks Dataset](https://www.kaggle.com/dhruvildave/wikibooks-dataset)
- [TED Talks Dataset](https://www.kaggle.com/miguelcorraljr/ted-ultimate-dataset)

## Repository Contents
The `notebooks` directory contains Jupyter notebooks for data exploration and model development.

## Bucket Organization
The S3 bucket of the project is organized as follows:
- `raw-data/` contains the raw data as downloaded from the datasets.

[Back to top.](#language-recognize)
