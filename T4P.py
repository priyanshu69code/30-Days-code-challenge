from enum import Enum

class DaysOfWeek(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

today = DaysOfWeek.MONDAY
print(today)  # Output: DaysOfWeek.MONDAY


for day in DaysOfWeek:
    print(day.name, day.value)

# output:
# MONDAY 1
# TUESDAY 2
# WEDNESDAY 3
# THURSDAY 4
# FRIDAY 5
# SATURDAY 6
# SUNDAY 7