'''
Project: Predict Customer Churn with Clean Code

author: Gunnar
date: December 9, 2025
'''
import logging
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

logging.basicConfig(
    filename='results_churn.log',  # Name of the log file
    level=logging.DEBUG,      # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)


def import_data(pth):
    '''
    returns dataframe for the csv found at pth

    input:
            pth: a path to the csv
    output:
            df: pandas dataframe
    '''
    try:
        data = pd.read_csv(pth)
        logging.info("SUCCESS: File exist with a shape of %i rows, %i columns",
            data.shape[0], data.shape[1])
        return data
    except FileNotFoundError:
        return logging.error("ERROR: File not found")


def perform_eda(df):
    '''
    perform eda on df and save figures to images folder
    input:
            df: pandas dataframe

    output:
            None
    '''
    df['Churn'] = df['Attrition_Flag'].apply(lambda val: 0 if val == "Existing Customer" else 1)

    file_path = 'images/eda/'

    # Histogram churn
    plt.figure(figsize=(20,10))
    df['Churn'].hist()
    plt.savefig(f"{file_path}histogram_churn.png")

    # Histogram age
    plt.figure(figsize=(20,10)) 
    df['Customer_Age'].hist()
    plt.savefig(f"{file_path}histogram_age.png")

    # Bar chart marital status
    plt.figure(figsize=(20,10)) 
    df['Marital_Status'].value_counts('normalize').plot(kind='bar')
    plt.savefig(f"{file_path}bar_marital_status.png")

    plt.figure(figsize=(20,10))
    sns.histplot(df['Total_Trans_Ct'], stat='density', kde=True)
    plt.savefig(f"{file_path}kde_marital_status.png")

    plt.figure(figsize=(20,10)) 
    sns.heatmap(df.corr(), annot=False, cmap='Dark2_r', linewidths = 2)
    plt.savefig(f"{file_path}corr_heatmap.png")

if __name__ == "__main__":
    df = import_data("data/bank_data.csv")
    print(df.shape)
    perform_eda(df)
