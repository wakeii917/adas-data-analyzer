import pandas as pd
import h5py
import numpy as np

def load_can_log(filepath):
    with h5py.File(filepath, 'r') as f:
        speed = f['speed'][:]
        accel = f['car_accel'][:]
        times = f['times'][:]
        radar = f['UN_D_radar_msg'][:]
        radar_times = f['UN_T_radar_msg'][:]
        
    df_speed = pd.DataFrame({
        'timestamp_s': times,
        'speed_mps': speed,
        'accel_mps2': accel
    })

    df_radar = pd.DataFrame({
        'timestamp_s': radar_times,
        'distance_m': radar[:, 0]
    })

    df_speed = df_speed.sort_values('timestamp_s')
    df_radar = df_radar.sort_values('timestamp_s')

    df = pd.merge_asof(df_speed, df_radar, on='timestamp_s')
    df = df.dropna()
    df = df[df['distance_m'] < 150]
    df['speed_mps'] = df['speed_mps'].clip(lower=0)
    df = df.reset_index(drop=True)
    return(df)