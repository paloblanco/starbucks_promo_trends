# Starbucks Promotions: Preference of customers to special offers

This repository has been used to analyze the behavior of starbucks customers in response to promotional offers. This has been assmebled in as part of the Udacity Data Science nanodegree program. The research documented here was done to create a blog post on this topic: https://paloblanco.github.io/starbucks_promos.html

## Motivation
The goal of this project is to inform Starbucks on how to best deploy promotions to drive consumer spending at Starbucks stores. Starbucks has made available to Udacity students a set of simulated data 

## Setup
If you want to recreate this analysis, you can follow the instructions below. This was executed on Windows 10 and edited in VS Code, but I see no reason why this won't run on other platforms. You WILL need python on your system. This was coded in python 10.

1. Clone this repo
2. Create a virtual environment inside the repo:
```
python -m venv venv -- assuming you have python installed and in your path. 
```
3. Install requirements. Make sure to activate your virtual environment, then run the following:
```
python -m pip install -r requirements.txt
```
The primary dependencies of this project include jupyterlab, pandas, and [simplepysite](https://pypi.org/project/simplepysite/), a simple static site generator I built, also in pursuit of the Udacity Data Science Nanodegree.

If you wish to build the blog post (pages/index.md), after installing dependencies, open a terminal and run:

```
python simplepysite
```

4. After installing the requirements, you can run the notebook "Starbucks Capstone_notebook.ipynb". 

## Data

This project uses three data files provided by Starbucks, as decribed below:

```
data
    |
    - portfolio.json
    - profile.json
    - transcript.json
```

Descriptions for the schema of these files can be found "Starbucks_Captsone_notebook.ipynb," under the header "Data Sets." In short, these files contain information on the types of promotions Starbucks has offered (portfolio), demographic information about simulated customers (profile), and a list of transactions and customer responses to promotions (transcript).

## Acknowledgements
Data has been provided to Udacity by Starbucks.