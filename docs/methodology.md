# Methodology

## Data Loading
The dataset `epa-sea-level.csv` is loaded into a Pandas DataFrame for analysis. The data is read from a CSV file, and basic validation checks are performed to ensure it is not empty and is properly formatted.

## Data Analysis
The analysis involves the following steps:

1. **Exploratory Data Analysis (EDA)**:
   - Examine the dataset for any missing or erroneous values.
   - Understand the distribution and characteristics of the sea level measurements over time.

2. **Linear Regression**:
   - **Full Dataset Analysis**:
     - Perform linear regression on the entire dataset to determine the trend in sea level changes.
     - Calculate the line of best fit using the least squares method.
     - Predict future sea level for the year 2050 using the regression model.
   
   - **Recent Dataset Analysis**:
     - Filter the dataset to include only data from the year 2000 onwards.
     - Perform linear regression on this subset to analyze more recent trends.
   
3. **Visualization**:
   - **Overall Analysis Plot**:
     - Create a scatter plot of the original data and overlay the line of best fit.
     - Include the prediction for the year 2050.
   
   - **Recent Analysis Plot**:
     - Create a scatter plot of the data from the year 2000 onwards and overlay the new line of best fit.

## Error Handling
The script includes error handling mechanisms to manage common issues:
- **File Not Found**: Alerts if the data file is missing.
- **Data Loading Errors**: Handles cases of empty or incorrectly formatted files.
- **Regression Errors**: Manages issues related to performing linear regression.
- **General Exceptions**: Catches any unexpected errors and provides informative messages.
