# Data-Engineer---Supplement-Experiments
Project in PostgreSQL and Python


1001-Experiments makes personalized supplements tailored to individual health needs.

1001-Experiments aims to enhance personal health by using data from wearable devices and health apps.

This data, combined with user feedback and habits, is used to analyze and refine the effectiveness of the supplements provided to the user through multiple small experiments.

The data engineering team at 1001-Experiments plays a crucial role in ensuring the collected health and activity data from thousands of users is accurately organized and integrated with the data from supplement usage.

This integration helps 1001-Experiments provide more targeted health and wellness recommendations and improve supplement formulations.

Task
1001-Experiments currently has the following four datasets with four months of data:

"user_health_data.csv" which logs daily health metrics, habits and data from wearable devices,
"supplement_usage.csv" which records details on supplement intake per user,
"experiments.csv" which contains metadata on experiments, and
"user_profiles.csv" which contains demographic and contact information of the users.
Each dataset contains unique identifiers for users and/or their supplement regimen.

The developers and data scientsits currently manage code that cross-references all of these data sources separately, which is cumbersome and error-prone.

Your manager has asked you to write a Python function that cleans and merges these datasets into a single dataset.

The final dataset should provide a comprehensive view of each user's health metrics, supplement usage, and demographic information.

To test your code, your manager will run only the code merge_all_data('user_health_data.csv', 'supplement_usage.csv', 'experiments.csv', 'user_profiles.csv')
Your merge_all_data function must return a DataFrame, with columns as described below.
All columns must accurately match the descriptions provided below, including names.

Data
The provided data is structured as follows:

![image](https://github.com/user-attachments/assets/35555a13-18b3-49b8-af3f-f1083a86d291)

The function you write should return data as described below.

There should be a unique row for each daily entry combining health metrics and supplement usage.

Where missing values are permitted, they should be in the default Python format unless stated otherwise.

Column Name	Description
user_id	Unique identifier for each user.
There should not be any missing values.
date	The date the health data was recorded or the supplement was taken, in date format.
There should not be any missing values.
email	Contact email of the user.
There should not be any missing values.
user_age_group	The age group of the user, one of: 'Under 18', '18-25', '26-35', '36-45', '46-55', '56-65', 'Over 65' or 'Unknown' where the age is missing.
experiment_name	Name of the experiment associated with the supplement usage.
Missing values for users that have user health data only is permitted.
supplement_name	The name of the supplement taken on that day. Multiple entries are permitted.
Days without supplement intake should be encoded as 'No intake'.
dosage_grams	The dosage of the supplement taken in grams. Where the dosage is recorded in mg it should be converted by division by 1000.
Missing values for days without supplement intake are permitted.
is_placebo	Indicator if the supplement was a placebo (true/false).
Missing values for days without supplement intake are permitted.
average_heart_rate	Average heart rate as recorded by the wearable device.
Missing values are permitted.
average_glucose	Average glucose levels as recorded on the wearable device.
Missing values are permitted.
sleep_hours	Total sleep in hours for the night preceding the current day’s log.
Missing values are permitted.
activity_level	Activity level score between 0-100.
Missing values are permitted.


