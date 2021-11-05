import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv', index_col=0)

# Add 'overweight' column
df['overweight'] = round(df['weight'] / df['height'] ** 2 * 10_000, 0)
df['overweight'] = df['overweight'].astype(int)

df.loc[df['overweight'] <= 25, 'overweight'] = 0
df.loc[df['overweight'] > 25, 'overweight'] = 1

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    cats = df[['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke', 'cardio']]
    df_cat = cats.melt(id_vars='cardio', value_vars=cats.columns, var_name='variable', value_name='values')

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    cardio_zero = df_cat[df_cat['cardio'] == 0]
    cardio_one = df_cat[df_cat['cardio'] == 1]

    # Draw the catplot with 'sns.catplot()'
    fig, ((ax0, ax1)) = plt.subplots(figsize=(12, 6), nrows=1, ncols=2)

    sns.countplot(x='variable', hue='values', data=cardio_zero, ax=ax0)
    sns.countplot(x='variable', hue='values', data=cardio_one, ax=ax1)

    ax0.set(title='cardio = 0', ylabel='total')
    ax1.set(title='cardio = 1', ylabel=None)
    ax1.legend([])

    # Do not modify the next two lines
    fig.savefig('catplot.jpg', bbox_inches='tight')

    return fig


# Draw Heat Map
def draw_heat_map():
    pass
    # # Clean the data
    # df_heat = None

    # # Calculate the correlation matrix
    # corr = None

    # # Generate a mask for the upper triangle
    # mask = None



    # # Set up the matplotlib figure
    # fig, ax = None

    # # Draw the heatmap with 'sns.heatmap()'



    # # Do not modify the next two lines
    # fig.savefig('heatmap.png')
    # return fig
