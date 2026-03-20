import pandas as pd

def load_vehicle_log(vehicle_log):
    df = pd.read_csv(vehicle_log)
    # validation d'abord
    colonnes_attendues = {'timestamp_s', 'speed_mps', 'distance_m', 'accel_mps2'}
    if not colonnes_attendues <= set(df.columns):
        raise ValueError('une ou plusieurs colonnes sont erronées')
    df['speed_mps'] = df['speed_mps'].clip(lower=0)
    return df