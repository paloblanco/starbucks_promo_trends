# Starbucks Promotions: Preference of customers to special offers

This repository has been used to analyze the behavior of starbucks customers in response to promotional offers. This has been assmebled in as part of the Udacity Data Science nanodegree program. The research documented here was done to create a blog post on this topic: https://paloblanco.github.io/starbucks_promos.html

## Motivation
The goal of this project is to inform Starbucks on how to best deploy promotions to drive consumer spending at Starbucks stores. Starbucks has made available to Udacity students a set of simulated data 

## Setup
If you want to recreate this analysis, you can follow the instructions below. This was executed on Windows 10 and edited in VS Code, but I see no reason why this won't run on other platforms. You WILL need python on your system.

1. Clone this repo
2. Create a virtual environment inside the repo:
```
python -m venv venv -- assuming you have python isntalled and in your path. 
```
3. Install requirements. Make sure to activate your virtual environment, then run the following:
```
python -m pip install -r requirements.txt
```

4. After installing the requirements, you can run the notebook "Starbucks Capstone_notebook.ipynb". However, you will need to create a "data" directory containing the proper data assets, which have not been provided here. See the "Data" section for more details.

## Data

This project uses three data files provided by Starbucks. They need to be placed in a directory called "data" to run this repo, as decribed below:

```
data
    |
    - portfolio.json
    - profile.json
    - transcript.json
```

Descriptions for the schema of these files can be found "Starbucks_Captsone_notebook.ipynb," under the header "Data Sets."

## Acknowledgements
Data has been provided to Udacity by Starbucks.