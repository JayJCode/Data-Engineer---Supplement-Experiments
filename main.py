import pandas as pd
import numpy as np

def extract(file):
    
    return pd.read_csv(file)

def get_age_group(age):
    if age == 'Unknown':
        return 'Unknown'
    if age < 18:
        return 'Under 18'
    elif 18 <= age <= 25:
        return '18-25'
    elif 26 <= age <= 35:
        return '26-35'
    elif 36 <= age <= 45:
        return '36-45'
    elif 46 <= age <= 55:
        return '46-55'
    elif 56 <= age <= 65:
        return '56-65'
    else:
        return 'Over 65'

def missed_values(df):
    
    # Checking missing values of all needed to data, also implement fillna when needed
    assert not df['user_id'].isna().any(), "There are missing values in 'user_id'"
    
    assert not df['date'].isna().any(), "There are missing values in 'date'"
    
    assert not df['email'].isna().any(), "There are missing values in 'email'"
    
    assert not df['supplement_name'].isna().any(), "There are missing values in 'supplement_name'"
    
    # While there is supplement takn, there cann't be any missing values in 'name', 'dosage', 'is_placebo'
    supplement_taken_df = df[df['supplement_name'] != 'No intake']
    
    assert not supplement_taken_df['name'].isna().any(), "There are missing values in 'name'"
    
    assert not supplement_taken_df['dosage'].isna().any(), "There are missing values in 'dosage'"
    
    assert not supplement_taken_df['is_placebo'].isna().any(), "There are missing values in 'is_placebo'"
    
    return df

def fill_missed_values(df):
    
    # Have to be a data in it
    df['user_id'] = df['user_id'].fillna('default_id')
    df['date'] = df['date'].fillna('2020-07-18')
    df['email'] = df['email'].fillna('default@example.com')
    
    # Got from describtion info how to fill
    df['age'] = df['age'].fillna('Unknown')
    df['supplement_name'] = df['supplement_name'].fillna("No intake")
    
    # Missing values are permited only when 'supplement_name' has 'No intake'
    supplement_taken_df = df[df['supplement_name'] != 'No intake']
    df.loc[supplement_taken_df.index, 'name'] = supplement_taken_df['name'].fillna('placebo testing')
    df.loc[supplement_taken_df.index, 'dosage'] = supplement_taken_df['dosage'].fillna(1000)
    df.loc[supplement_taken_df.index, 'is_placebo'] = supplement_taken_df['is_placebo'].fillna(True)
    
    # Missing values are permited
    df['average_heart_rate'] = df['average_heart_rate'].fillna('')
    df['average_glucose'] = df['average_glucose'].fillna('')
    df['sleep_hours'] = df['sleep_hours'].fillna('')
    df['activity_level'] = df['activity_level'].fillna('')
    
    return df

def transform(df):
    
    # Clean 'date'
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Clean 'user_age_group'
    df['user_age_group'] = df['age'].apply(get_age_group)
    
    # Clean 'experiment_name'
    df = df.rename(columns={'name': 'experiment_name'})
    
    # Clean 'dosage_grams'
    df.loc[df['dosage_unit'] == 'mg', 'dosage'] = df.loc[df['dosage_unit'] == 'mg', 'dosage'] / 1000
    df = df.rename(columns={'dosage': 'dosage_grams'})
    
    # Clean 'sleep_hours'
    df['sleep_hours'] = df['sleep_hours'].astype(str)
    df['sleep_hours'] = df['sleep_hours'].str.replace('h', '', case=False)
    df['sleep_hours'] = pd.to_numeric(df['sleep_hours'], errors='coerce')
    
    # Drop unnecessary columns
    df.drop(columns=['dosage_unit', 'experiment_id', 'description', 'age'], inplace=True)
    
    
    # Reorder columns
    desired_order = [
        'user_id', 'date', 'email', 'user_age_group', 'experiment_name',
        'supplement_name', 'dosage_grams', 'is_placebo', 
        'average_heart_rate', 'average_glucose', 'sleep_hours', 'activity_level'
    ]
    df = df.reindex(columns=desired_order)
    
    # Clean 'activity_level'
    activity_level_map = {
        1: 0,
        2: 33,
        3: 66,
        4: 100
    }
    df['activity_level'] = df['activity_level'].map(activity_level_map).fillna(df['activity_level'])
    df['activity_level'] = pd.to_numeric(df['activity_level'], errors='coerce').fillna(0).astype(int)

    return df

def merge_all_data(file1, file2, file3, file4):
    
    # Load all files to df
    user_health_data = extract(file1)
    supplement_usage = extract(file2)
    experiments = extract(file3)
    user_profiles = extract(file4)
    
    # Merge tables
    merged_df = pd.merge(user_health_data, user_profiles, on='user_id', how='left')
    merged_df = pd.merge(merged_df, supplement_usage, on=['user_id', 'date'], how='outer')
    merged_df = pd.merge(merged_df, experiments, on='experiment_id', how='left')
    
    # Identify and replace missing values
    merged_df = fill_missed_values(merged_df)
    
    # Check for missed values
    merged_df = missed_values(merged_df)
    
    # Transform data
    merged_df = transform(merged_df)
        
    return merged_df

merged_df = merge_all_data("user_health_data.csv", "supplement_usage.csv", "experiments.csv", "user_profiles.csv")
#print(merged_df.head(40))
