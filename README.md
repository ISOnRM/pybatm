# pybatm
Python interface for libbatm - C library for reading battery state from Linux sysfs

## Installation
Make sure libbatm is installed:
```plaintext
$ ldconfig -p | grep libbatm
    libbatm.so.0 (libc6,x86-64) => /usr/lib/libbatm.so.0
```
Create venv in your project and install pybatm
```bash
pip install --upgrade pip wheel
pip install git+https://github.com/ISOnRM/pybatm
```

## Usage
```plaintext
$ ls /sys/class/power_supply/ | grep -i bat
BAT1

$ .venv/bin/python3
>>> from batm.battery import Battery
>>> bat = Battery("BAT1")
>>> # update() method runs in constructor
>>> bat.updated
True
>>> bat.get_field("present")
1
>>> bat.health
98.56281050390348
>>> print(bat)

                            Meta fields:
meta_name:                  BAT1
meta_snap_time:             2026-06-12 13:45:43
meta_scanned_fields_amt:    18
                            Fields:
manufacturer:               ASUS
model_name:                 A32-K55
technology:                 Li-ion
status:                     Not charging
                            Metrics:
energy_rate:                0.0 W
energy_full:                88.71 Wh
energy_full_design:         90.0 Wh
soc:                        81.12 %
health:                     98.56 %
time_to_full:               nan Hrs
time_to_empty:              nan Hrs

```

## Requirenments
libbatm >= 0.1.x

## Status
- 0.1.0. Supports libbatm 0.1.x

## Module
### API
Module `battery.py` provides Battery class.
Method `update` updates underlying `struct batm_snap`'s fields. It also runs in constructor.
Metrics can be accessed like attributes

## License 
MIT (See LICENSE)
