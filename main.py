from parser import load_vehicle_log
from kpi import compute_kpi
from analysis import detect_event
from plot import plot_dashboard
from report import print_report
from can_parser import load_can_log

df = load_can_log('2016-01-30--11-24-51.h5')
df = compute_kpi(df)
events = detect_event(df)
print_report(df, events)
plot_dashboard(df)