# Business Process Prediction, Simulation, and Optimization

This repository is the first exercise for the practical course "Business Process Prediction, Simulation, and Optimization" at TUM.

It analyzes the [BPI Challenge 2020](https://data.4tu.nl/repository/collection:event_log_bpi_challenge_2020) dataset, which contains event logs from a loan application process.

## How to Install

It is created via [uv](https://docs.astral.sh/uv/) package and project manager. I have used Python 3.13 for this project. 
To install the required packages, run either of the following commands:

```bash
uv install
```

```bash
pip install -r requirements.txt
```

## Repo Structure

- `data/`: Contains the dataset files.
- `src/`: Contains Jupyter notebooks for analysis.


## Notebooks

The analysis is divided into several Jupyter notebooks:
- `01_data_preprocessing.ipynb`: Data loading and preprocessing.

## Libraries Used

- pm4py <https://processintelligence.solutions/static/api/2.7.17/pm4py.html>
