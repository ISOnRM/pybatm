# pybatm
Python interface for libbatm - C library for reading battery state from Linux sysfs

## Installation
```bash
#later
```

# Usage
```plaintext
your_python_project $ .venv/bin/python3
>>> from batm.battery import Battery
>>> bat = Battery("BAT1")
>>> bat.updated
True
>>> print(bat)

                            Meta fields:
meta_name:                  BAT1
meta_snap_time:             2026-06-12 11:56:38
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

>>>
```

## Requirenments
libbatm >= 0.1.x

## Status
In development. You can read the module - it is self-explanatory

## License 
MIT (See LICENSE)
