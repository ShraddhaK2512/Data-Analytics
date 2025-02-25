# Titanic Dataset Dashboard

## Project Overview
The Titanic Dataset Dashboard is an interactive Tableau visualization that provides an in-depth analysis of the Titanic passengers' demographics and survivability statistics. 
The dashboard includes several visualizations that explore trends, patterns, and correlations within the Titanic dataset, providing insights into factors like gender, age, 
passenger class, embarkation port, and family status that influenced survival rates. The dashboard aims to make it easier for users to understand complex data, identify key 
factors that impacted survival, and gain insights into historical and demographic aspects of the Titanic disaster.

## Visualizations
The dashboard includes the following visualizations:
  ### 1 Total Survival Rate 
    A bar chart depicting the overall survival rate of Titanic passengers.
  ### 2 Survival by Gender and Age  
    A stacked bar chart comparing survival rates based on gender and age groups.
  ### 3 Passenger Class Breakdown 
    A bar chart displaying the distribution of passengers in each ticket class.
  ### 4 Survival by Ticket Class
    A stacked bar chart illustrating survival rates across different ticket classes.
  ### 5 Age Distribution 
    A bar chart showing the distribution of passenger ages.
  ### 6 Family Status 
    A bar chart representing the proportion of passengers traveling alone or with others.
  ### 7 Survival by Embarkation Port  
    A stacked bar chart examining the relationship between embarkation port and survival rates by age group.
  ### 8 Fare Distribution 
    A stacked bar chart illustrating the distribution of passenger fares by class.
  ### 9 Fare vs. Survival
    A stacked bar chart exploring the relationship between fare and survival.
  ### 10 Passenger’s Age Spread Based on Survival 
    A histogram showcasing the age spread of passengers according to survival status.

## Data Preprocessing
Before creating the visualizations, several data preprocessing steps were performed:
 - Handling Missing Values: Rows with missing values in the "Age" column were removed, as age is an important attribute.
 - Removing the "Cabin" Column: The "Cabin" column was removed due to a large number of missing values, which may have influenced the analysis.
 - Removing Duplicate Data in the "Ticket" Column: Duplicate ticket entries were removed to ensure unbiased analysis.

## Interactive Features
### Filters:
- Age: Users can filter data within specific age ranges using bins to analyze different age groups.
### Marks Card:
- The "People Survival" field indicates survival status. Colors (red for non-survivors, blue for survivors) differentiate between survived and non-survived passengers.
## Calculated Fields
- Age Group: A calculated field categorizing passengers as "Child", "Young", or "Old" based on their age.
- Fare Group: A calculated field that classifies fares into "Cheap", "Regular", or "Expensive" based on fare values.
- Family Status: A calculated field indicating whether a passenger is traveling alone or with others based on the number of parents or children aboard.
- Passenger Class Group: A calculated field grouping passengers by ticket class (1st, 2nd, or 3rd).
- People Survival Group: A calculated field that shows whether a passenger survived or not.

## Intended Users
The dashboard is intended for the following audiences:
- Researchers and Data Scientists: To explore trends and patterns in passenger survival.
- Educators: For teaching data science, statistics, and history.
- Business Analysts: To gain insights into the travel and safety industry.
- Historians: To explore the Titanic disaster's social and cultural aspects.
- Students: For academic projects in data science, computer science, and social sciences.

## Tableau Public Workbook and original data source
The Tableau dashboard is published on Tableau Public. You can view the interactive visualizations by following the link below:
[Titanic DataAnalysis Dashboard](https://public.tableau.com/app/profile/shraddha.kumbharkar/viz/DVFinalTitanicDataset/FInalDashboard) 

Data source link:
[source](https://www.kaggle.com/datasets/brendan45774/test-file?resource=download)

## How to Use the Dashboard
1. Click on the link to open the workbook on Tableau Public.
2. Interact with the visualizations using the provided filters and controls.
3. Explore the data in different views, such as survival rates by gender, age, class, etc.

