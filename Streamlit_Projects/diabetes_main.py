# Code for 'diabetes_main.py' file.

# Importing the necessary Python modules.
import numpy as np
import pandas as pd

# Loading the dataset.
def load_data():
    # Load the Diabetes dataset into DataFrame.

    df = pd.read_csv('diabetes_df.csv')
    df.head()

    # Rename the column names in the DataFrame.
    df.rename(columns = {"BloodPressure": "Blood_Pressure"}, inplace = True)
    df.rename(columns = {"SkinThickness": "Skin_Thickness"}, inplace = True)
    df.rename(columns = {"DiabetesPedigreeFunction": "Pedigree_Function",}, inplace = True)

    df.head()

    return df

diabetes_df = load_data()

