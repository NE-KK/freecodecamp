# freecodecamp
# Daily Coding Challenges
# Day 11 (2025-08-21)
# Mile Pace

import math

"""
Given a number of miles ran, and a time in "MM:SS" (minutes:seconds) it took to run those miles, 
return a string for the average time it took to run each mile in the format "MM:SS".

Add leading zeros when needed.
"""


def dismantle_duration(duration: str) -> list: 
    duration_list = duration.split(":")

    for i in range(2):
        duration_list[i] = int(duration_list[i])
    
    return duration_list


def transform_duration(list_min_sec: list, miles: float) -> float:
    decimal_seconds = list_min_sec[1] * (100 / 60) / 100
    decimal_time = list_min_sec[0] + decimal_seconds
    decimal_time_per_mile = decimal_time / miles

    return decimal_time_per_mile


def built_sec_str(float_sec_decimal) -> str:
    float_sec_decimal = float_sec_decimal * 100
    float_sec_int = int(float_sec_decimal * (60 / 100))
    float_sec_str = str(float_sec_int)

    return float_sec_str


def per_mile_duration(float_per_mile: float) -> str: 
    list_sec_min = math.modf(float_per_mile)
    str_min = "0" + str((int(list_sec_min[1])))
    str_sec = built_sec_str(list_sec_min[0])
    
    if len(str_sec) < 2:
        str_sec = "0" + str_sec

    duration_str = str_min + ":" + str_sec

    return duration_str


def mile_pace(miles: float, duration: str) -> str:
    list_min_sec = dismantle_duration(duration)
    float_per_mile = transform_duration(list_min_sec, miles)
    string_duration = per_mile_duration(float_per_mile)

    return string_duration
