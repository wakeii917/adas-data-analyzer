import pandas as pd
import numpy as np

def compute_kpi(df):
    df['safe_distance_m']=df['speed_mps']*2
    df['thw_s']=np.where(df['speed_mps']>8.3,df['distance_m']/df['speed_mps'],np.nan)
    df['distance_violation']=df['distance_m']<df['safe_distance_m']
    df['hard_braking']=df['accel_mps2']<-3
    return df
    