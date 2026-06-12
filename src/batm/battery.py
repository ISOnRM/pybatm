from batm._batm import ffi, lib

class Battery:
    def __init__(self, battery_name: str) -> None:
        self.updated: bool = False
        self.snap_ptr = ffi.new("struct batm_snap *")
        self.battery_name: str = battery_name
        self.update()

    def update(self) -> bool:
        if lib.batm_snap_update(ffi.NULL, self.battery_name.encode(), self.snap_ptr) == -1:
            self.updated = False
            return False
        self.updated = True
        return True

    # attributes from metric functions

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
energy_rate:        {round(self.energy_rate, 2)} W
energy_full:        {round(self.energy_full, 2)} Wh
energy_full_design: {round(self.energy_full_design, 2)} Wh
soc:                {round(self.soc, 2)} %
health:             {round(self.health, 2)} %
time_to_full:       {round(self.time_to_full, 2)} Hrs
time_to_empty:      {round(self.time_to_empty, 2)} Hrs
"""


if __name__ == "__main__":
    bat: Battery = Battery("BAT1")
    print(bat)
