#!/usr/bin/env python
# coding: utf-8

def task_2_1_exploratory_analysis():
    ''' 
        This function corresponds to the task 2.1 in the homework assignment document 
        and should print the information required to answer the questions. 

        Specifically, you will need to fill the blanks below to complete the requirements.
    '''
    import pandas as pd 

    score_data = pd.read_csv('score.csv')
    print(type(score_data), "the score dataset") 
    ### Your task is to use pandas.DataFrame APIs to print the info required for the questions.
    ### Reference: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

    ######## Your code. Blank #1. ######## 
    print("\n")

    print("Q1: Data instances (students) in dataset:", len(score_data))

    print("Q2: Columns in dataset:", len(score_data.columns))
    print("Data types of each column:", score_data.dtypes)

    hours = score_data['Hours']
    print("Q3: Average Study Hours:", sum(hours)/len(hours))

    scores = score_data['Scores']
    print("Q4: Average Scores:", sum(scores)/len(scores))

    print("Q5: My Observation: This dataset can be used to analyze the relationship between study hours and scores. It can help identify if there is a correlation between the amount of time spent studying and the scores achieved by students.")

    ######## Your code. Blank #1. ########

    cereal_data = pd.read_csv('cereal.csv')
    print(type(cereal_data), "the cereal dataset")
    ### Your task is to use pandas.DataFrame APIs to print the info required for the questions.
    ### Reference: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

    ######## Your code. Blank #2. ######## 
    print("\n")

    print("Q1: Data instances (cereals) in dataset:", len(cereal_data))
    print("Q2: Data types of each column:", cereal_data.dtypes)

    mfr = cereal_data['mfr']
    print("Q3: Unique manufacturers in dataset:", len(mfr.unique()))

    print("Q4: Max/Min/Average for each column:\n", cereal_data.describe())

    print("Q5: My Observation: This dataset can be used to analyze the nutritional content of different cereals and their manufacturers. It can help identify trends in cereal production and consumer preferences based on nutritional values.")

    ######## Your code. Blank #2. ########


def task_2_2_data_visualization():
    ''' 
        This function corresponds to the task 2.2 in the homework assignment document 
        and should print the information required to answer the questions. 

        Specifically, you will need to fill the blanks below to complete the requirements.
    '''
    import pandas as pd
    import matplotlib.pyplot as plt

    score_data = pd.read_csv('score.csv')
    print(type(score_data), "the score dataset") 
    ### Your task is to use APIs from pandas and matplotlib to plot some charts described in the assignment document. 

    ######## Your code. Blank #3. ######## 
    ### Hints: plt.hist, use bins=10.
    scores = score_data['Scores']

    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    low_scores = scores[scores < 60]
    mid_scores = scores[(scores >= 60) & (scores < 80)]
    high_scores = scores[scores >= 80]

    plt.hist(low_scores, bins=bins, color='red', alpha=0.7, label='Below 60')
    plt.hist(mid_scores, bins=bins, color='blue', alpha=0.7, label='60-79')
    plt.hist(high_scores, bins=bins, color='green', alpha=0.7, label='80+')

    plt.xlabel('Score')
    plt.ylabel('Number of Students')
    plt.title('Distribution of Student Scores')
    plt.legend()

    ######## Your code. Blank #3. ######## 
    plt.savefig('hours_scores_hist')
    plt.clf()

    ######## Your code. Blank #4. ######## 
    ### Hints: plt.scatter.
    plt.scatter(score_data['Hours'], score_data['Scores'])
    
    plt.xlabel('Study Hours')
    plt.ylabel('Score')
    plt.title('Study Hours vs Score')

    ######## Your code. Blank #4. ######## 
    plt.savefig('hours_scores_scatter')
    plt.clf()

    cereal_data = pd.read_csv('cereal.csv')
    print(type(cereal_data), "the cereal dataset")
    
    mfr_abbr2label_mapping = {
        "A":  "American Home Food Products",
        "G":  "General Mills",
        "K":  "Kelloggs",
        "N":  "Nabisco",
        "P":  "Post",
        "Q":  "Quaker Oats",
        "R":  "Ralston Purina",
    }

    ######## Your code. Blank #5. ######## 
    ### Hints: plt.pie, show the full name of manufacturer using mfr_abbr2label_mapping.
    manufacturer_counts = cereal_data['mfr'].value_counts()

    labels = []

    for mfr in manufacturer_counts.index:
        labels.append(mfr_abbr2label_mapping[mfr])

    plt.pie(
        manufacturer_counts,
        labels=labels,
        autopct='%1.1f%%'
    )

    plt.title('Distribution of Cereal Manufacturers')
    ######## Your code. Blank #5. ######## 
    
    plt.savefig('manufacturer_pie')
    plt.clf()

    ######## Your code. Blank #6. ######## 
    ### Hints: plt.scatter.

    ### chart calories v.s. rating ###
    plt.scatter(cereal_data['calories'], cereal_data['rating'])

    plt.xlabel('Calories')
    plt.ylabel('Rating')
    plt.title('Calories vs Rating')
    ### chart calories v.s. rating ###

    plt.savefig('calories_rating_scatter')
    plt.clf()

    ### chart sugars v.s. rating ###
    plt.scatter(cereal_data['sugars'], cereal_data['rating'])

    plt.xlabel('Sugars')
    plt.ylabel('Rating')
    plt.title('Sugars vs Rating')
    ### chart sugars v.s. rating ###

    plt.savefig('sugars_rating_scatter')
    plt.clf()

    ### chart fiber v.s. rating ###
    plt.scatter(cereal_data['fiber'], cereal_data['rating'])

    plt.xlabel('Fiber')
    plt.ylabel('Rating')
    plt.title('Fiber vs Rating')
    ### chart fiber v.s. rating ###

    plt.savefig('fiber_rating_scatter')
    plt.clf()
    ######## Your code. Blank #6. ######## 


if __name__ == "__main__":
    ''' 
        This is the start of your ML program. 
        Please study the overall code flow before you start working on the homework.
    '''
    
    task_2_1_exploratory_analysis()
    task_2_2_data_visualization()