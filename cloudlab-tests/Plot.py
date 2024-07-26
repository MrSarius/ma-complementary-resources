import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

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
    plt.xlim(left=1, right=20)

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
    plt.xlim(left=1, right=20)

    plt.savefig(f"{PLOT_BASE_PATH}/throughput_ebpf.pdf")


def plot_throughput_compare():
    df = pd.read_csv(f'{BASE_PATH}/throughput.csv')
    df = pd.melt(df, id_vars=['Seconds'], var_name='Measurement', value_name='Throughput')
    df['Throughput'] = df['Throughput'] / 1e9  # bit/s to Gbit/s

    df_ebpf = pd.read_csv(f'{BASE_PATH}/throughput_ebpf.csv')
    df_ebpf = pd.melt(df_ebpf, id_vars=['Seconds'], var_name='Measurement', value_name='Throughput')
    df_ebpf['Throughput'] = df_ebpf['Throughput'] / 1e9  # bit/s to Gbit/s

    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Seconds', y='Throughput', data=df, errorbar='sd', label='Original Proxy')
    sns.lineplot(x='Seconds', y='Throughput', data=df_ebpf, errorbar='sd', label='eBPF Proxy')

    plt.axhline(21.8, color='r', linestyle='--', label=f'HW Limitation')

    plt.title('Throughput Comparison of Original Proxy and eBPF Proxy')
    plt.xlabel('Seconds')
    plt.ylabel('Throughput [Gbit/s]')
    plt.legend()
    plt.xlim(left=1, right=20)

    plt.savefig(f"{PLOT_BASE_PATH}/throughput_compare.pdf")


def plot_jitter_cdf():
    df = pd.read_csv(f'{BASE_PATH}/jitter.csv')
    df_ebpf = pd.read_csv(f'{BASE_PATH}/jitter_ebpf.csv')

    plt.figure(figsize=(10, 6))

    sns.ecdfplot(df['Jitter'], label='Original Proxy')
    sns.ecdfplot(df_ebpf['Jitter'], label='eBPF Proxy')

    plt.xlabel('Jitter')
    plt.ylabel('CDF')
    plt.title('Jitter Comparison of Original Proxy and eBPF Proxy')
    plt.legend()
    plt.xlim(left=0)

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
    df = pd.read_csv(f'{BASE_PATH}/latency.csv')
    df = pd.melt(df, id_vars=['Ping_Nr.'], var_name='Measurement', value_name='Latency')

    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Ping_Nr.', y='Latency', data=df, errorbar='sd', label='Latency')

    mean_latency = df['Latency'].mean()
    plt.axhline(mean_latency, color='r', linestyle='--', label=f'Mean: {mean_latency:.2f} ms')

    plt.title('Latency of Original Proxy')
    plt.xlabel('Ping Nr.')
    plt.ylabel('RTT [ms]')
    # plt.xlim(left=1)
    plt.legend()
    plt.xlim(left=1, right=15)

    plt.savefig(f"{PLOT_BASE_PATH}/latency.pdf")


def plot_latency_ebpf():
    df = pd.read_csv(f'{BASE_PATH}/latency_ebpf.csv')
    df = pd.melt(df, id_vars=['Ping_Nr.'], var_name='Measurement', value_name='Latency')

    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Ping_Nr.', y='Latency', data=df, errorbar='sd', label='Latency', color='orange')

    mean_latency = df['Latency'].mean()
    plt.axhline(mean_latency, color='r', linestyle='--', label=f'Mean: {mean_latency:.2f} ms')

    plt.title('Latency of eBPF Proxy')
    plt.xlabel('Ping Nr.')
    plt.ylabel('RTT [ms]')
    plt.legend()
    plt.xlim(left=1, right=15)

    plt.savefig(f"{PLOT_BASE_PATH}/latency_ebpf.pdf")


def plot_latency_cdf():
    df = pd.read_csv(f'{BASE_PATH}/latency.csv')
    df_ebpf = pd.read_csv(f'{BASE_PATH}/latency_ebpf.csv')#

    df = df.melt(id_vars=["Ping_Nr."], var_name="Measurement", value_name="Latency")
    df_ebpf = df_ebpf.melt(id_vars=["Ping_Nr."], var_name="Measurement", value_name="Latency")

    plt.figure(figsize=(10, 6))

    sns.ecdfplot(df["Latency"], label='Original Proxy')
    sns.ecdfplot(df_ebpf["Latency"], label='eBPF Proxy')
    plt.xlabel('RTT [ms]')
    plt.ylabel('CDF')
    plt.title('Latency Comparison of Original Proxy and eBPF Proxy')
    plt.legend()
    plt.xlim(left=0)

    plt.savefig(f"{PLOT_BASE_PATH}/latency_cdf.pdf")

def plot_cpu():
    df = pd.read_csv(f'{BASE_PATH}/cpu_ram.csv')
    # df_ebpf = pd.read_csv(f'{BASE_PATH}/cpu_ram_ebpf.csv')

    alpha = 0.1  # Transparency level
    ewma_span = 20

    # Normalize the timestamps so that each measurement starts at time zero
    df['relative_time'] = df.groupby('measurement')['timestamp'].transform(lambda x: x - x.min())

    # Convert relative time to seconds
    df['relative_time_seconds'] = df['relative_time'] / 1000

    # Determine the maximum relative time in seconds to set the background sections
    max_time_seconds = df['relative_time_seconds'].max()
    third = max_time_seconds / 3

    # Plot CPU usage over relative time with light grey lines
    plt.figure(figsize=(14, 7))

    # Shade the background with specified colors
    plt.axvspan(0, third, facecolor='green', alpha=alpha)
    plt.axvspan(third, 2 * third, facecolor='red', alpha=alpha)
    plt.axvspan(2 * third, max_time_seconds, facecolor='blue', alpha=alpha)

    # Plot each measurement in light grey
    for measurement in df['measurement'].unique():
        subset = df[df['measurement'] == measurement]
        plt.plot(subset['relative_time_seconds'], subset['cpu_usage'], color='lightgrey')

    # Calculate and plot the EWMA of CPU usage
    ewma_cpu_usage = df.groupby('relative_time_seconds')['cpu_usage'].mean().ewm(span=ewma_span).mean()
    plt.plot(ewma_cpu_usage.index, ewma_cpu_usage.values, color='black', linewidth=2, label='EWMA CPU Usage')

    # Calculate the average EWMA between second 15 and 30
    ewma_avg = ewma_cpu_usage[(ewma_cpu_usage.index >= 15) & (ewma_cpu_usage.index <= 30)].mean()

    # Plot the average EWMA as a horizontal red line
    plt.axhline(y=ewma_avg, color='red', linestyle='--', linewidth=2, label='Average EWMA during load phase')

    # Annotate the average EWMA value on the y-axis
    plt.annotate(f'{ewma_avg:.2f}%', xy=(0, ewma_avg), xytext=(-10, 0),
                 textcoords='offset points', va='center', ha='right', color='red', fontsize=12)

    # Create custom legend patches
    idle_patch = mpatches.Patch(color='green', alpha=alpha, label='Idle')
    load_patch = mpatches.Patch(color='red', alpha=alpha, label='Load')
    cleanup_patch = mpatches.Patch(color='blue', alpha=alpha, label='Clean Up')
    ewma_line = mpatches.Patch(color='black', label=f'EWMA (α={(1 / (ewma_span + 1)):.2f}) CPU Usage')
    avg_ewma_line = mpatches.Patch(color='red', linestyle='--', label='Average EWMA during load phase', fill=False)

    plt.title('eBPF Proxy: CPU Usage Over Time')
    plt.xlabel('Time [seconds]')
    plt.ylabel('CPU Usage [%]')
    plt.legend(loc='upper left', handles=[idle_patch, load_patch, cleanup_patch, ewma_line, avg_ewma_line])

    # Set xlim to start at 0
    plt.xlim(0, max_time_seconds)
    plt.ylim(0, 100)

    plt.savefig(f"{PLOT_BASE_PATH}/cpu.pdf")

def plot_cpu_ebpf():
    df = pd.read_csv(f'{BASE_PATH}/cpu_ram_ebpf.csv')

    alpha = 0.1  # Transparency level
    ewma_span = 20

    # Normalize the timestamps so that each measurement starts at time zero
    df['relative_time'] = df.groupby('measurement')['timestamp'].transform(lambda x: x - x.min())

    # Convert relative time to seconds
    df['relative_time_seconds'] = df['relative_time'] / 1000

    # Determine the maximum relative time in seconds to set the background sections
    max_time_seconds = df['relative_time_seconds'].max()
    third = max_time_seconds / 3

    # Plot CPU usage over relative time with light grey lines
    plt.figure(figsize=(14, 7))

    # Shade the background with specified colors
    plt.axvspan(0, third, facecolor='green', alpha=alpha)
    plt.axvspan(third, 2 * third, facecolor='red', alpha=alpha)
    plt.axvspan(2 * third, max_time_seconds, facecolor='blue', alpha=alpha)

    # Plot each measurement in light grey
    for measurement in df['measurement'].unique():
        subset = df[df['measurement'] == measurement]
        plt.plot(subset['relative_time_seconds'], subset['cpu_usage'], color='lightgrey')

    # Calculate and plot the EWMA of CPU usage
    ewma_cpu_usage = df.groupby('relative_time_seconds')['cpu_usage'].mean().ewm(span=ewma_span).mean()
    plt.plot(ewma_cpu_usage.index, ewma_cpu_usage.values, color='black', linewidth=2, label='EWMA CPU Usage')

    # Calculate the average EWMA between second 15 and 30
    ewma_avg = ewma_cpu_usage[(ewma_cpu_usage.index >= 15) & (ewma_cpu_usage.index <= 30)].mean()

    # Plot the average EWMA as a horizontal red line
    plt.axhline(y=ewma_avg, color='red', linestyle='--', linewidth=2, label='Average EWMA during load phase')

    # Annotate the average EWMA value on the y-axis
    plt.annotate(f'{ewma_avg:.2f}%', xy=(0, ewma_avg), xytext=(-10, 0),
                 textcoords='offset points', va='center', ha='right', color='red', fontsize=12)

    # Create custom legend patches
    idle_patch = mpatches.Patch(color='green', alpha=alpha, label='Idle')
    load_patch = mpatches.Patch(color='red', alpha=alpha, label='Load')
    cleanup_patch = mpatches.Patch(color='blue', alpha=alpha, label='Clean Up')
    ewma_line = mpatches.Patch(color='black', label=f'EWMA (α={(1 / (ewma_span + 1)):.2f}) CPU Usage')
    avg_ewma_line = mpatches.Patch(color='red', linestyle='--', label='Average EWMA during load phase', fill=False)

    plt.title('eBPF Proxy: CPU Usage Over Time')
    plt.xlabel('Time [seconds]]')
    plt.ylabel('CPU Usage [%]')
    plt.legend(loc='upper left', handles=[idle_patch, load_patch, cleanup_patch, ewma_line, avg_ewma_line])

    # Set xlim to start at 0
    plt.xlim(0, max_time_seconds)
    plt.ylim(0, 100)

    plt.savefig(f"{PLOT_BASE_PATH}/cpu_ebpf.pdf")

def plot_ram():
    df = pd.read_csv(f'{BASE_PATH}/cpu_ram.csv')

    alpha = 0.1  # Transparency level
    ewma_span = 20

    # Normalize the timestamps so that each measurement starts at time zero
    df['relative_time'] = df.groupby('measurement')['timestamp'].transform(lambda x: x - x.min())

    # Convert relative time to seconds
    df['relative_time_seconds'] = df['relative_time'] / 1000

    # Convert used_ram from Kbit to MB
    df['used_ram'] = df['used_ram'] / 8192

    # Determine the maximum relative time in seconds to set the background sections
    max_time_seconds = df['relative_time_seconds'].max()
    third = max_time_seconds / 3

    # Plot RAM usage over relative time with light grey lines
    plt.figure(figsize=(14, 7))

    # Shade the background with specified colors
    plt.axvspan(0, third, facecolor='green', alpha=alpha)
    plt.axvspan(third, 2 * third, facecolor='red', alpha=alpha)
    plt.axvspan(2 * third, max_time_seconds, facecolor='blue', alpha=alpha)

    # Plot each measurement in light grey
    for measurement in df['measurement'].unique():
        subset = df[df['measurement'] == measurement]
        plt.plot(subset['relative_time_seconds'], subset['used_ram'], color='lightgrey')

    # Calculate and plot the EWMA of RAM usage
    ewma_ram_usage = df.groupby('relative_time_seconds')['used_ram'].mean().ewm(span=ewma_span).mean()
    plt.plot(ewma_ram_usage.index, ewma_ram_usage.values, color='black', linewidth=2, label='EWMA RAM Usage')

    # Calculate the average EWMA between second 15 and 30
    ewma_avg = ewma_ram_usage[(ewma_ram_usage.index >= 15) & (ewma_ram_usage.index <= 30)].mean()

    # Plot the average EWMA as a horizontal red line
    plt.axhline(y=ewma_avg, color='red', linestyle='--', linewidth=2, label='Average EWMA during load phase')

    # Annotate the average EWMA value on the y-axis
    plt.annotate(f'{ewma_avg:.2f} MB', xy=(0, ewma_avg), xytext=(-10, 0),
                 textcoords='offset points', va='center', ha='right', color='red', fontsize=12)

    # Create custom legend patches
    idle_patch = mpatches.Patch(color='green', alpha=alpha, label='Idle')
    load_patch = mpatches.Patch(color='red', alpha=alpha, label='Load')
    cleanup_patch = mpatches.Patch(color='blue', alpha=alpha, label='Clean Up')
    ewma_line = mpatches.Patch(color='black', label=f'EWMA (α={(1 / (ewma_span + 1)):.2f}) RAM Usage')
    avg_ewma_line = mpatches.Patch(color='red', linestyle='--', label='Average EWMA during load phase', fill=False)

    plt.title('Original Proxy: RAM Usage Over Time')
    plt.xlabel('Time [seconds]')
    plt.ylabel('RAM Usage [MB]')
    plt.legend(loc='upper left', handles=[idle_patch, load_patch, cleanup_patch, ewma_line, avg_ewma_line])

    # Set xlim to start at 0
    plt.xlim(0, max_time_seconds)

    plt.tight_layout()
    plt.savefig(f"{PLOT_BASE_PATH}/ram.pdf")

def plot_ram_ebpf():
    df = pd.read_csv(f'{BASE_PATH}/cpu_ram_ebpf.csv')

    alpha = 0.1  # Transparency level
    ewma_span = 20

    # Normalize the timestamps so that each measurement starts at time zero
    df['relative_time'] = df.groupby('measurement')['timestamp'].transform(lambda x: x - x.min())

    # Convert relative time to seconds
    df['relative_time_seconds'] = df['relative_time'] / 1000

    # Convert used_ram from Kbit to MB
    df['used_ram'] = df['used_ram'] / 8192

    # Determine the maximum relative time in seconds to set the background sections
    max_time_seconds = df['relative_time_seconds'].max()
    third = max_time_seconds / 3

    # Plot RAM usage over relative time with light grey lines
    plt.figure(figsize=(14, 7))

    # Shade the background with specified colors
    plt.axvspan(0, third, facecolor='green', alpha=alpha)
    plt.axvspan(third, 2 * third, facecolor='red', alpha=alpha)
    plt.axvspan(2 * third, max_time_seconds, facecolor='blue', alpha=alpha)

    # Plot each measurement in light grey
    for measurement in df['measurement'].unique():
        subset = df[df['measurement'] == measurement]
        plt.plot(subset['relative_time_seconds'], subset['used_ram'], color='lightgrey')

    # Calculate and plot the EWMA of RAM usage
    ewma_ram_usage = df.groupby('relative_time_seconds')['used_ram'].mean().ewm(span=ewma_span).mean()
    plt.plot(ewma_ram_usage.index, ewma_ram_usage.values, color='black', linewidth=2, label='EWMA RAM Usage')

    # Calculate the average EWMA between second 15 and 30
    ewma_avg = ewma_ram_usage[(ewma_ram_usage.index >= 15) & (ewma_ram_usage.index <= 30)].mean()

    # Plot the average EWMA as a horizontal red line
    plt.axhline(y=ewma_avg, color='red', linestyle='--', linewidth=2, label='Average EWMA during load phase')

    # Annotate the average EWMA value on the y-axis
    plt.annotate(f'{ewma_avg:.2f} MB', xy=(0, ewma_avg), xytext=(-10, 0),
                 textcoords='offset points', va='center', ha='right', color='red', fontsize=12)

    # Create custom legend patches
    idle_patch = mpatches.Patch(color='green', alpha=alpha, label='Idle')
    load_patch = mpatches.Patch(color='red', alpha=alpha, label='Load')
    cleanup_patch = mpatches.Patch(color='blue', alpha=alpha, label='Clean Up')
    ewma_line = mpatches.Patch(color='black', label=f'EWMA (α={(1 / (ewma_span + 1)):.2f}) RAM Usage')
    avg_ewma_line = mpatches.Patch(color='red', linestyle='--', label='Average EWMA during load phase', fill=False)

    plt.title('eBPF Proxy: RAM Usage Over Time')
    plt.xlabel('Time [seconds]')
    plt.ylabel('RAM Usage [MB]')
    plt.legend(loc='upper left', handles=[idle_patch, load_patch, cleanup_patch, ewma_line, avg_ewma_line])

    # Set xlim to start at 0
    plt.xlim(0, max_time_seconds)

    plt.tight_layout()
    plt.savefig(f"{PLOT_BASE_PATH}/ram_ebpf.pdf")

def main():
    plot_throughput()
    plot_throughput_ebpf()
    plot_throughput_compare()

    plot_jitter_box()
    plot_jitter_cdf()

    plot_latency()
    plot_latency_ebpf()
    plot_latency_cdf()

    plot_cpu()
    plot_cpu_ebpf()

    plot_ram()
    plot_ram_ebpf()


if __name__ == '__main__':
    main()
