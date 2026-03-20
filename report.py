import pandas as pd
import numpy as np

def print_report(df, events):
    mean=np.mean(df['distance_violation'])*100
    min=np.min(df['distance_m'])
    mean_s=np.mean(df['speed_mps'])*3.6
    events_detected=len(events)
    print(f"Violation rate  : {mean:.1f} %")
    print(f"Min distance    : {min:.1f} m")
    print(f"Mean speed      : {mean_s:.1f} km/h")
    print(f"Events detected : {events_detected}")