from cffi import FFI

BATM_STR_MAX: int = 64

ffibuilder: FFI = FFI()

ffibuilder.cdef(
f"""
typedef int... time_t;
typedef int... int32_t;
typedef int... int64_t;

struct batm_snap {{
    time_t meta_snap_time;
    int32_t meta_scanned_fields_amt;
    char meta_name[{BATM_STR_MAX}];

    char manufacturer[{BATM_STR_MAX}];
    char model_name[{BATM_STR_MAX}];
    char serial_number[{BATM_STR_MAX}];
    char type[{BATM_STR_MAX}];
    char status[{BATM_STR_MAX}];
    char charge_behaviour[{BATM_STR_MAX}];
    char technology[{BATM_STR_MAX}];
    char capacity_level[{BATM_STR_MAX}];
    char health[{BATM_STR_MAX}];
    char charge_type[{BATM_STR_MAX}];

    int32_t present;
    int32_t online;
    int32_t capacity;
    int32_t capacity_alert_min;
    int32_t capacity_alert_max;
    int32_t charge_control_start_threshold;
    int32_t charge_control_end_threshold;
    int32_t cycle_count;
    int32_t manufacture_year;
    int32_t manufacture_month;
    int32_t manufacture_day;

    int64_t voltage_now, voltage_avg;
    int64_t voltage_min, voltage_max;
    int64_t voltage_min_design, voltage_max_design;

    int64_t current_now, current_avg;
    int64_t current_max, charge_control_limit;
    int64_t charge_control_limit_max, charge_term_current, precharge_current;

    int64_t charge_now, charge_avg;
    int64_t charge_full, charge_full_design;
    int64_t charge_counter;

    int64_t energy_now, energy_avg;
    int64_t energy_full, energy_full_design;

    int64_t power_now;
    int64_t power_avg;

    int64_t temp;
    int64_t temp_alert_min, temp_alert_max;
    int64_t temp_min, temp_max;

    int64_t time_to_empty_now, time_to_empty_avg;
    int64_t time_to_full_now, time_to_full_avg;

    int64_t alarm;
    int64_t internal_resistance;
}};

int batm_snap_update(const char *base,
                     const char *name,
                     struct batm_snap *snap);

double batm_energy_rate_w(const struct batm_snap *s);
double batm_energy_full_wh(const struct batm_snap *s);
double batm_energy_full_design_wh(const struct batm_snap *s);
double batm_soc_pct(const struct batm_snap *s);
double batm_health_pct(const struct batm_snap *s);
double batm_time_to_full_hr(const struct batm_snap *s);
double batm_time_to_empty_hr(const struct batm_snap *s);
"""
)

ffibuilder.set_source(
    "batm._batm",
    r"#include <batm/batm.h>",
    libraries=["batm", "m"]
)

if __name__ == "__main__":
    _ = ffibuilder.compile()