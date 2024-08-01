# Global Average Sea Level Change Analysis and Prediction

## Overview
This project performs a comprehensive analysis of the global average sea level change since 1880 and makes predictions for future 
changes using linear regression. The dataset used for this analysis is sourced from [FreeCodeCamp's Data Analysis with Python Projects](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor).

## About Dataset
The dataset `epa-sea-level.csv` contains the following columns:
- **Year**: The year of the measurement.
- **CSIRO Adjusted Sea Level**: The adjusted sea level measurement in inches.

## Project Structure
The project is organized into the following directories:

```
sea-level-analysis/
│
├── data/
│   └── epa-sea-level.csv
│
├── docs/
│   ├── data-description.md
│   ├── methodology.md
│   └── results.md
│
├── figures/
│   ├── forecast.jpg
│   └── sea-level-recent.jpg
│
├── scripts/
│   └── analysis.py
│
└── requirements.txt
```

### Description of Directories
- **data/**: Contains the dataset used for analysis.
  - `epa-sea-level.csv`: Raw data as received from the source.

- **docs/**: Documentation for different stages of the project.
  - `data-description.md`: Detailed description of the dataset.
  - `methodology.md`: Explanation of the methods used for analysis and prediction.
  - `results.md`: Summary of the results obtained from the analysis.

- **figures/**: Generated plots/visualizations from the scripts.
  - `forecast.jpg`: Visualization of the sea level predictions.
  - - `sea-level-recent.jpg`: Visualization of the current sea level.

- **scripts/**: Python scripts for data processing and analysis.
  - `analysis.py`: Main script for performing the analysis and generating plots.

- **requirements.txt**: Contains the libraries (specific versions) used for the project.

## Installation
Clone the repository and install the necessary dependencies using `pip`:

```sh
git clone https://github.com/yourusername/sea-level-analysis.git
cd sea-level-analysis
pip install -r requirements.txt
```

## Usage
1. **Run the Analysis**: Execute the main analysis script to perform the analysis and generate plots.

    ```sh
    python scripts/analysis.py
    ```

## Project Details
### Script Overview
The `analysis.py` script is the main script for data processing and analysis. It includes:
- **Data Loading**: Loads the dataset from the CSV file.
- **Regression Analysis**: Performs linear regression to calculate the line of best fit.
- **Prediction**: Predicts the sea level for the year 2050.
- **Plotting**: Creates and saves visualizations of the analysis results.

### Error Handling
The script includes robust error handling to manage common issues:
- **File Not Found**: Raises an error if the data file is missing.
- **Data Loading Errors**: Handles errors related to empty or improperly formatted data files.
- **Regression Calculation Errors**: Raises errors for empty input data or issues during the regression analysis.
- **General Exceptions**: Catches and reports unexpected errors.

## Results
The output figures shows two plots:
1. **Overall Analysis**: Displays the scatter plot and line of best fit for the entire dataset, including a prediction for 2050.
2. **Recent Analysis**: Displays the scatter plot and line of best fit starting from the year 2000, showing recent trends in sea level rise.

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests with any improvements or additional features.

## License
This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

---
The conversation continues on [**Kaggle**](https://www.kaggle.com/code/mrowurakwarteng/global-average-sea-level-change-analysis)
