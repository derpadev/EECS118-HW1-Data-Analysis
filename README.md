# EECS 118 HW1 — Data Analysis & Visualization

This repository contains my solution for **EECS 118 Homework 1: Environment Setup and Data Analysis Visualization** at UC Irvine.

The assignment introduces **Exploratory Data Analysis (EDA)** using Python, Pandas, and Matplotlib. The analysis is performed on two datasets: student study hours/scores and cereal nutritional information.

## Overview

The goal of this homework is to practice:

* Setting up a Python 3.8 development environment using Anaconda
* Working with Python virtual environments
* Using **Pandas** to inspect and analyze datasets
* Using **Matplotlib** to visualize data
* Performing basic Exploratory Data Analysis (EDA)
* Interpreting data and identifying relationships between variables

## Technologies

* **Python 3.8**
* **Pandas**
* **Matplotlib**
* **Anaconda**

## Datasets

### Study Hours & Scores

`score.csv` contains student study hours and corresponding scores.

The analysis includes:

* Number of students
* Number and data types of columns
* Average study hours
* Average scores
* General observations about the dataset
* Score distribution
* Relationship between study hours and scores

### Cereal Dataset

`cereal.csv` contains nutritional information and ratings for cereal products.

The analysis includes:

* Number of cereal products
* Data types of each column
* Number of cereal manufacturers
* Minimum, maximum, and average values
* General observations about the dataset
* Manufacturer distribution
* Relationships between:

  * Calories and rating
  * Sugars and rating
  * Fiber and rating

## Visualizations

The program generates the following visualizations:

### Score Dataset

1. **Score Distribution Histogram**

   * Scores below 60 are shown in red
   * Scores from 60–79 are shown in blue
   * Scores 80 and above are shown in green

2. **Study Hours vs. Score Scatterplot**

   * X-axis: Study Hours
   * Y-axis: Score

### Cereal Dataset

3. **Cereal Manufacturer Distribution**

   * Pie chart showing the distribution of cereal manufacturers

4. **Calories vs. Rating Scatterplot**

5. **Sugars vs. Rating Scatterplot**

6. **Fiber vs. Rating Scatterplot**

## Project Structure

```text
EECS118-HW1-Data-Analysis/
│
├── hw1_<student_id>.py
├── score.csv
├── cereal.csv
│
├── plots/
│   ├── score_histogram.png
│   ├── score_scatter.png
│   ├── cereal_manufacturers.png
│   ├── calories_rating.png
│   ├── sugars_rating.png
│   └── fiber_rating.png
│
├── screenshots/
│   └── ...
│
├── report/
│   └── hw1_<student_id>.pdf
│
└── README.md
```

## Environment Setup

Create a Conda environment using Python 3.8:

```bash
conda create -n eecs118 python=3.8
```

Activate the environment:

```bash
conda activate eecs118
```

Install the required packages:

```bash
conda install pandas matplotlib
```

Verify the installations:

```python
import pandas
import matplotlib
```

## Running the Program

After activating the `eecs118` environment, run:

```bash
python hw1_<student_id>.py
```

The program performs the required dataset analysis and generates the visualization files.

## Assignment

**Course:** EECS 118
**Assignment:** Homework 1 — Environment Setup and Data Analysis Visualization
**Assigned:** October 2, 2026
**Due:** October 9, 2026 at 11:59 PM

## Dataset Sources

* [80 Cereals Dataset](https://www.kaggle.com/datasets/crawford/80-cereals)
* [Student Study Hours Dataset](https://www.kaggle.com/datasets/himanshunakrani/student-study-hours)
