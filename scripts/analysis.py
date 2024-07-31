import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def load_data(filepath):
    """Load data from a CSV file."""
    try:
        df = pd.read_csv(filepath)
        if df.empty:
            raise ValueError("The dataset is empty.")
        return df
    except FileNotFoundError:
        raise FileNotFoundError("The data file was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("The data file is empty or not properly formatted.")
    except ValueError as e:
        raise ValueError(f"Error reading the data file: {e}")


def perform_regression(x, y):
    """Perform linear regression and return the slope and intercept."""
    try:
        slope, intercept, r_value, p_value, std_err = linregress(x, y)
        return slope, intercept
    except Exception as e:
        raise RuntimeError(f"Error performing regression: {e}")


def plot_data(x, y, y_pred, title, xlabel, ylabel, filename):
    """Plot the data and save the figure."""
    plt.scatter(x, y, label='Data points')
    plt.plot(x, y_pred, color='red', label='Line of Best Fit')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.savefig(filename)
    plt.close()


def main():
    # Load data
    filepath = '../data/epa-sea-level.csv'
    df = load_data(filepath)
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Perform regression for full dataset
    try:
        slope, intercept = perform_regression(x, y)
    except RuntimeError as e:
        print(e)
        return

    # Calculate y-values for the line of best fit
    y_prediction_full = slope * x + intercept

    # Predict sea level for the year 2050
    pred_y = slope * 2050 + intercept

    # Create a DataFrame for the new prediction
    pred_df = pd.DataFrame({'Year': [2050], 'CSIRO Adjusted Sea Level': [pred_y]})

    # Concatenate the original dataframe with the prediction
    df = pd.concat([df, pred_df], ignore_index=True)
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Perform regression for updated dataset
    try:
        slope, intercept = perform_regression(x, y)
    except RuntimeError as e:
        print(e)
        return

    # Calculate y-values for the updated line of best fit
    y_prediction_updated = slope * x + intercept

    # Plot and save the figure
    plot_data(x, y, y_prediction_updated, 'Rise in Sea Level', 'Year', 'Sea Level (inches)',
              '../figures/forecast.jpg')

    # Filter data for analysis from the year 2000 onwards
    df_recent = df[df['Year'] >= 2000].reset_index(drop=True)
    x_recent = df_recent['Year']
    y_recent = df_recent['CSIRO Adjusted Sea Level']

    # Perform regression for recent dataset
    try:
        slope_recent, intercept_recent = perform_regression(x_recent, y_recent)
    except RuntimeError as e:
        print(e)
        return

    # Calculate y-values for the recent line of best fit
    y_prediction_recent = slope_recent * x_recent + intercept_recent

    # Plot and save the recent data figure
    plot_data(x_recent, y_recent, y_prediction_recent, 'Rise in Sea Level (from 2000)', 'Year', 'Sea Level (inches)',
              '../figures/sea-level-recent.jpg')


if __name__ == "__main__":
    main()
