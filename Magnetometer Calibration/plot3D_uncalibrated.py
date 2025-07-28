import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

def load_file(filename="magnetometer_log4.txt"):
    if not os.path.isfile(filename):
        print(f"File not found: {filename}")
        return None

    try:
        # Accept any whitespace separator (tabs or spaces)
        df = pd.read_csv(filename, sep=r"\s+", engine='python', header=None, names=["X", "Y", "Z"])
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def plot_2d(df):
    df["Time"] = df.index * 0.2  # assuming 0.2 sec interval
    plt.figure(figsize=(10, 6))
    plt.plot(df["Time"], df["X"], label="X-axis")
    plt.plot(df["Time"], df["Y"], label="Y-axis")
    plt.plot(df["Time"], df["Z"], label="Z-axis")
    plt.xlabel("Time (s)")
    plt.ylabel("Magnetic Field (µT)")
    plt.title("2D Plot: Magnetometer Readings")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_3d(df):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df["X"], df["Y"], df["Z"], c='blue', s=5)
    ax.set_title("3D Plot: Magnetometer Readings")
    ax.set_xlabel("X (µT)")
    ax.set_ylabel("Y (µT)")
    ax.set_zlabel("Z (µT)")
    plt.tight_layout()
    plt.show()

def main():
    df = load_file("magnetometer_log4.txt")
    if df is None:
        return

    # Change this flag to switch between plots
    plot_type = "3D"  # or "2D"

    if plot_type == "2D":
        plot_2d(df)
    else:
        plot_3d(df)

if __name__ == "__main__":
    main()

