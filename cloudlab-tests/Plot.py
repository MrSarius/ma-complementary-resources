import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from Parser import BASE_PATH, load_samples_file

latency_samples = load_samples_file("latency")
throughput_samples = load_samples_file("throughput")
jitter_samples = load_samples_file("jitter")

latency_samples_ebpf = load_samples_file("latency_ebpf")
throughput_samples_ebpf = load_samples_file("throughput_ebpf")
jitter_samples_ebpf = load_samples_file("jitter_ebpf")

def plot_throughput():
    df = pd.read_csv(f'{BASE_PATH}/throughput.csv')
    df = pd.melt(df, id_vars=['Seconds'], var_name='Measurement', value_name='Throughput')
    df['Throughput'] = df['Throughput'] / 1e9 # bit/s to Gbit/s

    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Seconds', y='Throughput', data=df, errorbar='sd')
    plt.title('Throughput of Original Proxy')
    plt.xlabel('Seconds')
    plt.ylabel('Throughput (Gbit/s)')

    plt.savefig("plots/throughput.pdf")

def plot_throughput_ebpf():
    df = pd.read_csv(f'{BASE_PATH}/throughput_ebpf.csv')
    df = pd.melt(df, id_vars=['Seconds'], var_name='Measurement', value_name='Throughput')
    df['Throughput'] = df['Throughput'] / 1e9  # bit/s to Gbit/s

    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Seconds', y='Throughput', data=df, errorbar='sd', color='orange')
    plt.title('Throughput of eBPF Proxy')
    plt.xlabel('Seconds')
    plt.ylabel('Throughput (Gbit/s)')

    plt.savefig("plots/throughput_ebpf.pdf")

def plot_throughput_compare():
    df = pd.read_csv(f'{BASE_PATH}/throughput.csv')
    df = pd.melt(df, id_vars=['Seconds'], var_name='Measurement', value_name='Throughput')
    df['Throughput'] = df['Throughput'] / 1e9  # bit/s to Gbit/s
    df['Group'] = 'Throughput'

    # Load and reshape the second dataframe
    df_ebpf = pd.read_csv(f'{BASE_PATH}/throughput_ebpf.csv')
    df_ebpf = pd.melt(df_ebpf, id_vars=['Seconds'], var_name='Measurement', value_name='Throughput')
    df_ebpf['Throughput'] = df_ebpf['Throughput'] / 1e9  # bit/s to Gbit/s
    df_ebpf['Group'] = 'Throughput eBPF'

    # Combine the dataframes
    df_combined = pd.concat([df, df_ebpf], ignore_index=True)

    # Plot the combined dataframe
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Seconds', y='Throughput', hue='Group', data=df_combined, errorbar='sd')
    plt.title('Throughput Comparison of Original Proxy and eBPF Proxy')
    plt.xlabel('Seconds')
    plt.ylabel('Throughput (bits/s)')
    plt.legend()

    plt.savefig("plots/throughput_compare.pdf")

def plot_jitter_cdf():
    jitter_results_sorted = np.sort(jitter_samples)

    # Calculate the CDF values
    cdf = np.arange(1, len(jitter_results_sorted) + 1) / len(jitter_results_sorted)

    # Plot the CDF
    plt.figure(figsize=(8, 6))
    plt.plot(jitter_results_sorted, cdf, marker='o', linestyle='-', color='b')

    # Set plot labels and title
    plt.xlabel('Jitter (ms)')
    plt.ylabel('CDF')
    plt.title('Cumulative Distribution Function (CDF) of Jitter Results')

    # Save the plot to a file
    plt.savefig('plots/jitter_cdf.pdf')

def plot_jitter_box():
    data = jitter_samples + jitter_samples_ebpf
    labels = ['Set 1'] * len(jitter_samples) + ['Set 2'] * len(jitter_samples_ebpf)

    # Create a DataFrame
    df = pd.DataFrame({'Jitter': data, 'Set': labels})

    # Create a box plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Set', y='Jitter', data=df)

    # Set plot labels and title
    plt.xlabel('Data Set')
    plt.ylabel('Jitter (ms)')
    plt.title('Box Plot of Jitter Results')

    # Save the plot to a file
    plt.savefig('plots/jitter_boxplot_comparison.pdf')

def main():
    plot_throughput()
    plot_throughput_ebpf()
    plot_throughput_compare()

if __name__ == '__main__':
    main()