import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from Parser import BASE_PATH

PLOT_BASE_PATH = "plots"


def plot_throughput():
    df = pd.read_csv(f'{BASE_PATH}/throughput.csv')
    df = pd.melt(df, id_vars=['Seconds'], var_name='Measurement', value_name='Throughput')
    df['Throughput'] = df['Throughput'] / 1e9  # bit/s to Gbit/s

    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Seconds', y='Throughput', data=df, errorbar='sd')
    plt.title('Throughput of Original Proxy')
    plt.xlabel('Seconds')
    plt.ylabel('Throughput [Gbit/s]')

    plt.savefig(f"{PLOT_BASE_PATH}/throughput.pdf")


def plot_throughput_ebpf():
    df = pd.read_csv(f'{BASE_PATH}/throughput_ebpf.csv')
    df = pd.melt(df, id_vars=['Seconds'], var_name='Measurement', value_name='Throughput')
    df['Throughput'] = df['Throughput'] / 1e9  # bit/s to Gbit/s

    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Seconds', y='Throughput', data=df, errorbar='sd', color='orange')
    plt.title('Throughput of eBPF Proxy')
    plt.xlabel('Seconds')
    plt.ylabel('Throughput [Gbit/s]')

    plt.savefig(f"{PLOT_BASE_PATH}/throughput_ebpf.pdf")


def plot_throughput_compare():
    df = pd.read_csv(f'{BASE_PATH}/throughput_ebpf.csv')
    df = pd.melt(df, id_vars=['Seconds'], var_name='Measurement', value_name='Throughput')
    df['Throughput'] = df['Throughput'] / 1e9  # bit/s to Gbit/s

    df_ebpf = pd.read_csv(f'{BASE_PATH}/throughput.csv')
    df_ebpf = pd.melt(df_ebpf, id_vars=['Seconds'], var_name='Measurement', value_name='Throughput')
    df_ebpf['Throughput'] = df_ebpf['Throughput'] / 1e9  # bit/s to Gbit/s

    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Seconds', y='Throughput', data=df, errorbar='sd', label='Original Proxy')
    sns.lineplot(x='Seconds', y='Throughput', data=df_ebpf, errorbar='sd', label='eBPF Proxy')

    plt.title('Throughput Comparison of Original Proxy and eBPF Proxy')
    plt.xlabel('Seconds')
    plt.ylabel('Throughput [Gbit/s]')

    plt.savefig(f"{PLOT_BASE_PATH}/throughput_compare.pdf")


def plot_jitter_cdf():
    df = pd.read_csv(f'{BASE_PATH}/jitter.csv')
    df_ebpf = pd.read_csv(f'{BASE_PATH}/jitter_ebpf.csv')

    plt.figure(figsize=(10, 6))

    sns.ecdfplot(df['Jitter'], label='Original Proxy')
    sns.ecdfplot(df_ebpf['Jitter'], label='eBPF Proxy')

    plt.xlabel('Jitter')
    plt.ylabel('CDF')
    plt.title('Cumulative Distribution Function (CDF) of Jitter')
    plt.legend()

    plt.savefig(f"{PLOT_BASE_PATH}/jitter_cdf.pdf")


def plot_jitter_box():
    df = pd.read_csv(f'{BASE_PATH}/jitter.csv')
    df_ebpf = pd.read_csv(f'{BASE_PATH}/jitter_ebpf.csv')

    df['Dataset'] = 'Original Proxy'
    df_ebpf['Dataset'] = 'eBPF Proxy'

    # Combine the DataFrames
    combined_df = pd.concat([df, df_ebpf])

    # Plot boxplots
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Dataset', y='Jitter', data=combined_df, hue="Dataset")
    plt.title('Jitter Comparison of Original Proxy and eBPF Proxy')
    plt.xlabel("")
    plt.ylabel('Jitter [ms]')

    plt.savefig(f"{PLOT_BASE_PATH}/jitter_boxplot.pdf")


def plot_latency():
    pass


def plot_latency_ebpf():
    pass


def main():
    plot_throughput()
    plot_throughput_ebpf()
    plot_throughput_compare()

    plot_jitter_box()
    plot_jitter_cdf()


if __name__ == '__main__':
    main()
