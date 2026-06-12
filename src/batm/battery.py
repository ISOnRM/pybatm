import os
from datetime import datetime

from batm._batm import ffi, lib

class Battery:
    def __init__(self, battery_name: str) -> None:
        self.updated: bool = False
        self.snap_ptr = ffi.new("struct batm_snap *")
        self.battery_name: str = battery_name
        if not self.update():
            raise OSError(self._errno, os.strerror(self._errno), self.battery_name)

    def update(self) -> bool:
        if lib.batm_snap_update(ffi.NULL, self.battery_name.encode(), self.snap_ptr) == -1:
            self._errno = ffi.errno
            self.updated = False
            return False
        self.updated = True
        return True

    # access raw fields

    def get_field(self, field: str) -> str | int:
        val = getattr(self.snap_ptr, field)
        if isinstance(val, int):
            return val
        return ffi.string(val).decode()

    # attributes from metric functions (libbatm 0.1.x)

    @property
    def energy_rate(self) -> float:
        return lib.batm_energy_rate_w(self.snap_ptr)

    @property
    def energy_full(self) -> float:
        return lib.batm_energy_full_wh(self.snap_ptr)

    @property
    def energy_full_design(self) -> float:
        return lib.batm_energy_full_design_wh(self.snap_ptr)

    @property
    def soc(self) -> float:
        return lib.batm_soc_pct(self.snap_ptr)

    @property
    def health(self) -> float:
        return lib.batm_health_pct(self.snap_ptr)

    @property
    def time_to_full(self) -> float:
        """ Returns hours """
        return lib.batm_time_to_full_hr(self.snap_ptr)

    @property
    def time_to_empty(self) -> float:
        """ Returns hours """
        return lib.batm_time_to_empty_hr(self.snap_ptr)

    def __str__(self) -> str:
        return f"""
                            Meta fields:
meta_name:                  {self.get_field("meta_name")}
meta_snap_time:             {datetime.fromtimestamp(self.get_field("meta_snap_time"))} 
meta_scanned_fields_amt:    {self.get_field("meta_scanned_fields_amt")}
                            Fields:
manufacturer:               {self.get_field("manufacturer")}
model_name:                 {self.get_field("model_name")}
technology:                 {self.get_field("technology")}
status:                     {self.get_field("status")}
                            Metrics:
energy_rate:                {round(self.energy_rate, 2)} W
energy_full:                {round(self.energy_full, 2)} Wh
energy_full_design:         {round(self.energy_full_design, 2)} Wh
soc:                        {round(self.soc, 2)} %
health:                     {round(self.health, 2)} %
time_to_full:               {round(self.time_to_full, 2)} Hrs
time_to_empty:              {round(self.time_to_empty, 2)} Hrs
"""


if __name__ == "__main__":
    bat: Battery = Battery("BAT1")
    print(bat)
