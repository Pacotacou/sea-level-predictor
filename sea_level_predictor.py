import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    y = df['CSIRO Adjusted Sea Level']
    x = df['Year']
    # Create scatter plot
    plt.scatter(x, y)
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    
    x_pred = list(range(1880, 2051))
    y_pred = [slope * year + intercept for year in x_pred]
    plt.plot(x_pred, y_pred, 'r')
    # Create second line of best fit
    x_2000 = df[df['Year'] >= 2000]['Year']
    y_2000 = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(x_2000, y_2000)
    x_pred_2000 = list(range(2000, 2051))
    y_pred_2000 = [slope_2000 * year + intercept_2000 for year in x_pred_2000]
    plt.plot(x_pred_2000, y_pred_2000, 'g')
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


