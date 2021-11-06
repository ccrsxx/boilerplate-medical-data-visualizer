import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df['weight'] / df['height'] ** 2 * 10_000
df['overweight'] = [1 if i > 25 else 0 for i in df.overweight]

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = [1 if i > 1 else 0 for i in df.cholesterol]
df['gluc'] = [1 if i > 1 else 0 for i in df.gluc]

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    cats = df[['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke', 'cardio']]

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = cats.melt(id_vars='cardio', value_vars=cats.columns, var_name='variable', value_name='values')

    # Draw the catplot with 'sns.catplot()'
    graph = sns.catplot(x='variable', col='cardio', hue='values', data=df_cat, kind='count')
    graph.set_axis_labels('variable', 'total')

    fig = graph.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])
              & (df['height'] >= df['height'].quantile(0.025)) 
              & (df['height'] <= df['height'].quantile(0.975))
              & (df['weight'] >= df['weight'].quantile(0.025))
              & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=np.bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, center=0, annot=True, square=True, fmt=".1f",
                vmin=-.1, vmax=.25, cbar_kws={"shrink": .45}, ax=ax)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
