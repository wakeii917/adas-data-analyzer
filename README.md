# 🚗 ADAS Data Analyzer

Python tool for vehicle data analysis and ADAS performance evaluation — supports simulated data and real vehicle logs (HDF5).

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![pandas](https://img.shields.io/badge/pandas-2.0+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

---

## 📌 Overview

This project implements a complete data pipeline for analyzing vehicle driving data with a focus on **ACC (Adaptive Cruise Control)** performance metrics.

It was built as a hands-on project to develop skills in vehicle data analysis, ADAS logic, and signal processing — directly aligned with automotive industry requirements.

Two data modes are supported:
- **Simulated data** — generated with realistic driving phases (acceleration, cruise, braking)
- **Real vehicle logs** — parsed from HDF5 logs recorded on a real vehicle (comma.ai dataset, Mercedes E350 2010)

---

## ✨ Features

| Module | Description |
|--------|-------------|
| `data/generate_data.py` | Generates realistic simulated vehicle logs (CSV) |
| `src/parser.py` | Loads and validates CSV vehicle logs |
| `src/can_parser.py` | Parses real HDF5 vehicle logs (radar + kinematics) |
| `src/kpi.py` | Computes ADAS KPIs |
| `src/analysis.py` | Detects and classifies critical events |
| `src/plot.py` | Generates visualization dashboard |
| `src/report.py` | Prints aggregated KPI report |
| `main.py` | Orchestrates the full pipeline |

---

## 📊 ADAS KPIs Implemented

| KPI | Formula | Threshold |
|-----|---------|-----------|
| Safe distance | `speed_mps × 2` | 2-second rule |
| Time Headway (THW) | `distance_m / speed_mps` | Critical < 1.5s |
| Hard braking | `accel_mps2 < -3.0` | > 0.3g deceleration |
| Distance violation | `distance_m < safe_distance_m` | Boolean flag |

---

## 📁 Project Structure

```
adas-data-analyzer/
│
├── data/
│   └── generate_data.py      ← simulated data generation
│
├── src/
│   ├── parser.py             ← CSV loader & validator
│   ├── can_parser.py         ← HDF5 real log parser
│   ├── kpi.py                ← ADAS KPI computation
│   ├── analysis.py           ← event detection
│   ├── plot.py               ← dashboard visualization
│   └── report.py             ← KPI report
│
├── main.py                   ← pipeline entry point
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

```bash
git clone https://github.com/YOUR_USERNAME/adas-data-analyzer.git
cd adas-data-analyzer
pip install -r requirements.txt
```

---

## ▶️ Usage

### Mode 1 — Simulated data

```bash
# Generate simulated data
python data/generate_data.py

# Run the full pipeline
python main.py
```

### Mode 2 — Real vehicle logs (HDF5)

Download a drive log from the [comma.ai dataset](https://research.comma.ai) and place the `.h5` file in the `data/` folder.

```bash
python main.py
```

In `main.py`, switch between modes by choosing the loader:

```python
# Simulated data
from src.parser import load_vehicle_log
df = load_vehicle_log('data/vehicle_log.csv')

# Real HDF5 logs
from src.can_parser import load_can_log
df = load_can_log('data/your_log.h5')
```

---

## 📈 Example Output

```
Violation rate  : 19.7 %
Min distance    : 4.3 m
Mean speed      : 66.6 km/h
Events detected : 3975
```

Dashboard (real vehicle data — Mercedes E350 2010):

![Dashboard](outputs/dashboard.png)

---

## 🧠 ADAS Business Logic

### 2-Second Rule (Safe Distance)
```python
safe_distance_m = speed_mps * 2.0
```
At 90 km/h (25 m/s), the safe following distance is 50m. This is the baseline for ACC intervention.

### Time Headway (THW)
```python
thw_s = distance_m / speed_mps  # only computed if speed > 8.3 m/s
```
A THW below 1.5s is considered critical in ACC industry standards.

### Hard Braking Detection
```python
hard_braking = accel_mps2 < -3.0  # > 0.3g deceleration
```

### Event Detection (diff + cumsum pattern)
```python
df['event_group'] = (df['distance_violation'].diff() != 0).cumsum()
events = df[df['distance_violation']].groupby('event_group').agg(
    start_time=('timestamp_s', 'min'),
    end_time=('timestamp_s', 'max')
)
```

---

## 📂 Data

### Simulated data
```bash
python data/generate_data.py
# → generates data/vehicle_log.csv
```

### Real vehicle logs
Download a drive from the [comma.ai dataset](https://research.comma.ai) (HDF5 format).

The parser extracts the following signals:
- `speed` — vehicle speed (m/s)
- `car_accel` — longitudinal acceleration (m/s²)
- `UN_D_radar_msg` — radar distance to leading vehicle (m)
- `times` — timestamps (s)

> ⚠️ HDF5 log files are not included in this repository due to file size.

---

## 🔧 Possible Extensions

- **Dynamic thresholds** — replace fixed safe distance with rolling average (pandas rolling)
- **Multi-scenario analysis** — urban vs highway comparison
- **CAN bus decoding** — decode `.dbc` files with `cantools`
- **Anomaly detection** — replace fixed thresholds with ML-based detection

---

## 📝 License

MIT — personal project for learning and demonstration purposes.
