# NAME MALIK SHERDIL
# TASK 3
# MATPLOTLIB OPERATIONS

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data for plots
x = np.linspace(0, 10, 100)
y = np.sin(x)
data = np.random.randn(100)
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]
data2d = np.random.rand(10, 4)
df = sns.load_dataset('iris')  # Sample dataset for Seaborn

# Matplotlib Operations

# Basic plot
plt.figure()
plt.plot(x, y)
plt.savefig('matplotlib_basic_plot.png')
plt.close()

# Scatter plot
plt.figure()
plt.scatter(x, y)
plt.savefig('matplotlib_scatter_plot.png')
plt.close()

# Bar chart
plt.figure()
plt.bar(categories, values)
plt.savefig('matplotlib_bar_chart.png')
plt.close()

# Histogram
plt.figure()
plt.hist(data, bins=20)
plt.savefig('matplotlib_histogram.png')
plt.close()

# Pie chart
plt.figure()
plt.pie(values, labels=categories, autopct='%1.1f%%')
plt.savefig('matplotlib_pie_chart.png')
plt.close()

# Line styling
plt.figure()
plt.plot(x, y, color='red', linestyle='--', linewidth=2)
plt.savefig('matplotlib_line_styling.png')
plt.close()

# Labels and titles
plt.figure()
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Basic Plot with Labels and Title')
plt.savefig('matplotlib_labels_titles.png')
plt.close()

# Legend
plt.figure()
plt.plot(x, y, label='Sine wave')
plt.legend()
plt.savefig('matplotlib_legend.png')
plt.close()

# Subplots
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].scatter(x, y)
axs[1, 0].bar(categories, values)
axs[1, 1].hist(data, bins=10)
plt.savefig('matplotlib_subplots.png')
plt.close()

# Figure size
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.savefig('matplotlib_figure_size.png')
plt.close()

# Grid
plt.figure()
plt.plot(x, y)
plt.grid(True)
plt.savefig('matplotlib_grid.png')
plt.close()

# Saving Plot (already done in each above)

# Seaborn Operations

# Scatter Plot
plt.figure()
sns.scatterplot(data=df, x='sepal_length', y='sepal_width')
plt.savefig('seaborn_scatter_plot.png')
plt.close()

# Line plot
plt.figure()
sns.lineplot(data=df, x='sepal_length', y='sepal_width')
plt.savefig('seaborn_line_plot.png')
plt.close()

# Bar plot
plt.figure()
sns.barplot(data=df, x='species', y='sepal_length')
plt.savefig('seaborn_bar_plot.png')
plt.close()

# Count Plot
plt.figure()
sns.countplot(data=df, x='species')
plt.savefig('seaborn_count_plot.png')
plt.close()

# Histogram (displot)
sns.displot(df['sepal_length'], kde=True)
plt.savefig('seaborn_histogram_displot.png')
plt.close()

# Box Plot
plt.figure()
sns.boxplot(data=df, x='species', y='sepal_length')
plt.savefig('seaborn_box_plot.png')
plt.close()

# Violin Plot
plt.figure()
sns.violinplot(data=df, x='species', y='sepal_length')
plt.savefig('seaborn_violin_plot.png')
plt.close()

# Heatmap
plt.figure()
corr = df.corr()
sns.heatmap(corr, annot=True)
plt.savefig('seaborn_heatmap.png')
plt.close()

# Pairplot
sns.pairplot(df)
plt.savefig('seaborn_pairplot.png')
plt.close()

# Jointplot
sns.jointplot(data=df, x='sepal_length', y='sepal_width')
plt.savefig('seaborn_jointplot.png')
plt.close()

# Distribution Plots
plt.figure()
sns.distplot(df['sepal_length'])
plt.savefig('seaborn_distribution_plot.png')
plt.close()

