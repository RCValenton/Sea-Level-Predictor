import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = range(1880, 2051)
    y1 = res.slope * pd.Series(x1) + res.intercept
    plt.plot(x1, y1, 'r')

    # Create second line of best fit
    recent = df[df['Year'] >= 2000]
    res_recent = linregress(recent['Year'], recent['CSIRO Adjusted Sea Level'])
    x2 = range(2000, 2051)
    y2 = res_recent.slope * pd.Series(x2) + res_recent.intercept
    plt.plot(x2, y2, 'g')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()