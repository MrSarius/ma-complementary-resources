import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from typing import List

def plot_throughput(data: List[List[float]]):
    # Convert data to a DataFrame
    df = pd.DataFrame(data)
    df = df.melt(var_name='Second', value_name='Throughput')
    df['Second'] = df['Second'].astype(int)

    # Calculate the mean and standard deviation for each second
    throughput_stats = df.groupby('Second')['Throughput'].agg(['mean', 'std']).reset_index()

    # Plotting the data using seaborn
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Second', y='mean', data=throughput_stats, marker='o', label='Mean Throughput')
    plt.fill_between(throughput_stats['Second'],
                     throughput_stats['mean'] - throughput_stats['std'],
                     throughput_stats['mean'] + throughput_stats['std'],
                     alpha=0.2, label='Standard Deviation')

    # Set plot labels and title
    plt.xlabel('Time (seconds)')
    plt.ylabel('Throughput')
    plt.title('Throughput Time Series with Error Bands')
    plt.legend()

    # Show the plot
    plt.show()

def plot_throughput_ebpf(data: List[List[float]]):
    # Convert data to a DataFrame
    df = pd.DataFrame(data)
    df = df.melt(var_name='Second', value_name='Throughput')
    df['Second'] = df['Second'].astype(int)

    # Calculate the mean and standard deviation for each second
    throughput_stats = df.groupby('Second')['Throughput'].agg(['mean', 'std']).reset_index()

    # Plotting the data using seaborn
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Second', y='mean', data=throughput_stats, marker='o', label='Mean Throughput')
    plt.fill_between(throughput_stats['Second'],
                     throughput_stats['mean'] - throughput_stats['std'],
                     throughput_stats['mean'] + throughput_stats['std'],
                     alpha=0.2, label='Standard Deviation')

    # Set plot labels and title
    plt.xlabel('Time (seconds)')
    plt.ylabel('Throughput')
    plt.title('Throughput Over Time (ebpf enabled)')
    plt.legend()

    # Show the plot
    plt.show()

def plot_throughput_compare(data1: List[List[float]], data2: List[List[float]]):
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    # Melt the DataFrames
    df1 = df1.melt(var_name='Second', value_name='Throughput')
    df1['Second'] = df1['Second'].astype(int)
    df1['Dataset'] = 'Dataset 1'

    df2 = df2.melt(var_name='Second', value_name='Throughput')
    df2['Second'] = df2['Second'].astype(int)
    df2['Dataset'] = 'Dataset 2'

    # Combine both DataFrames
    df_combined = pd.concat([df1, df2])

    # Calculate the mean and standard deviation for each second and dataset
    throughput_stats = df_combined.groupby(['Dataset', 'Second'])['Throughput'].agg(['mean', 'std']).reset_index()

    # Plotting the data using seaborn
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Second', y='mean', hue='Dataset', data=throughput_stats, marker='o')

    for dataset in throughput_stats['Dataset'].unique():
        subset = throughput_stats[throughput_stats['Dataset'] == dataset]
        plt.fill_between(subset['Second'], subset['mean'] - subset['std'], subset['mean'] + subset['std'], alpha=0.2)

    # Set plot labels and title
    plt.xlabel('Time (seconds)')
    plt.ylabel('Throughput')
    plt.title('Throughput Time Series with Error Bands')
    plt.legend(title='Dataset')

    # Show the plot
    plt.show()