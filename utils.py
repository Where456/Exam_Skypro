import json
import os
import datetime


def get_data_all():
    with open(os.path.join("data", "data1.json"), 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_data_by_pk(pk):
    text = get_data_all()
    for i in text:
        if i['pk'] == pk:
            return i


def today():
    weekday = datetime.date.today().weekday()
    spisok = []
    if weekday == 5 or weekday == 6:
        spisok.append(timetable_weekend())
        spisok.append(timetable_everyday())
        return spisok
    if weekday >= 0 and weekday < 5:
        spisok.append(timetable_workday())
        spisok.append(timetable_everyday())
        return spisok
    if weekday >= 0 and weekday >= 7:
        spisok.append(timetable_everyday())
        spisok.append(timetable_everyday())
        return spisok


def timetable_everyday():
    data = get_data_all()
    travel = []
    for i in data:
        if i["days"] == "ежедн.":
            travel.append(i)
    return travel


def timetable_workday():
    data = get_data_all()
    travel = []
    for i in data:
        if i["days"] == "раб.":
            travel.append(i)
    return travel


def timetable_weekend():
    data = get_data_all()
    travel = []
    for i in data:
        if i["days"] == "вых.":
            travel.append(i)
    return travel


def search_station(station):
    list_stations = []
    text = get_data_all()
    for i in text:
        if i['halt'] == 'везде':
            list_stations.append(i)
        elif station.lower() in i['halt'].lower():
            list_stations.append(i)
    return list_stations
