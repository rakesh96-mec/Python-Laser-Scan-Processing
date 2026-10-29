# Python Laser Scan Processing

A university robotics exercise using offline laser-range scan data. The scripts identify the closest positive range reading in a scan and calculate its corresponding angle. A separate class-based implementation supports loading successive scans from a data file.

> **Scope:** The supplied files process saved data in Python. They do not currently subscribe to a live ROS 2 `sensor_msgs/LaserScan` topic or include a ROS 2 node/package wrapper.

## What it demonstrates

- Reading structured scan data from text files with Python
- Ignoring zero/invalid readings when finding the closest measurement
- Converting a scan-array index to an angle using scan angle constants
- Procedural and class-based approaches to sensor-data processing

## Repository structure

```text
.
├── data/
│   ├── laser-testdata_1.txt   # One scan with 99 readings
│   └── laser-testdata_2.txt   # Seven scans, each with 360 readings
├── laser_scan_analysis.py    # Functional analysis of one scan
├── laser_scan_model.py       # LaserModel class for scan-by-scan processing
└── README.md
```

## Requirements

Python 3. No third-party Python packages are required by these scripts; they use the standard library.

## Run the single-scan analysis

```bash
python3 laser_scan_analysis.py
```

The script prints the scan length, index of the closest positive range reading and its angle estimate, using the angle constants defined in `laser_scan_analysis.py`.

## Use the class-based implementation

`LaserModel` accepts the scan angle/range limits and loads data from a specified file path. A basic usage pattern is:

```python
from pathlib import Path
from laser_scan_model import LaserModel

data_file = Path("data/laser-testdata_2.txt")
model = LaserModel(
    angle_min=-1.57079637051,
    angle_max=1.53938043118,
    range_min=0.0,
    range_max=float("inf"),
)
model.update_laserdata(data_file)
model.set_angle_inc(model.calc_angle_inc())
index = model.calc_index_of_closest_point()
angle = model.calc_angle_of_closest_point()
print(index, angle)
```

Use the appropriate angle and range limits for the sensor/data source when adapting the exercise. The class is a learning example; the caller must set the angle increment before asking it to calculate the closest point's angle.
