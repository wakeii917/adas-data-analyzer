import pandas as pd
import numpy as np

def detect_event(df):
    df['event_group']=(df['distance_violation'].diff()!=0).cumsum()
    violations=df[df['distance_violation']==True]
    event=violations.groupby('event_group').agg(
        start_time=('timestamp_s','min'),
        end_time=('timestamp_s','max')
    )
    event['duration']=event['end_time']-event['start_time']
    return(event)
