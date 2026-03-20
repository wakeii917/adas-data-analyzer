import matplotlib.pyplot as plt   
import pandas as pd
import numpy as np


def plot_dashboard(df):
    print("plot.py chargé")
    fig, axes = plt.subplots(2, 1, figsize=(12,8)) 
    axes[0].plot(df['timestamp_s'], df['speed_mps']) 
    axes[1].plot(df['timestamp_s'], df['safe_distance_m'], label='safe distance')
    axes[1].plot(df['timestamp_s'], df['distance_m'], label='distance') 
    axes[1].legend()
    axes[0].set_title('speed(time)')
    axes[0].set_xlabel('time')
    axes[0].set_ylabel('speed')
    axes[1].set_title('safedistance(time)')
    axes[1].set_xlabel('time')
    axes[1].set_ylabel('safedistance')
    plt.savefig('dashboard.png')
    return df