#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import time

def stampToStr(timeStamp: int, strFormat = "%d.%m.%Y-%H:%M:%S") -> str:
	dateTime = datetime.fromtimestamp(timeStamp)
	datestr = dateTime.strftime(strFormat)
	return datestr

def stampToDateTime(timeStamp: int) -> datetime:
	dateTime = datetime.fromtimestamp(timeStamp)
	return dateTime

def strToStamp(dateStr: str, strFormat = "%d.%m.%Y-%H:%M:%S") -> int:
	time_Tuple = datetime.strptime(dateStr, strFormat)
	outTimeStamp = time.mktime(time_Tuple.timetuple())
	return int(outTimeStamp)

def dateTimeToStamp(dateTime: datetime) -> int:
	outTimeStamp = time.mktime(dateTime.timetuple())
	return int(outTimeStamp)

def dateTimeToStr(dateTime: datetime, strFormat = "%d.%m.%Y-%H:%M:%S") -> str:
	outDateTime = dateTime.strftime(strFormat)
	return outDateTime

def strToDateTime(dateStr: str, strFormat = "%d.%m.%Y-%H:%M:%S") -> datetime:
	time_Tuple = datetime.strptime(dateStr, strFormat)
	return time_Tuple

if __name__ == '__main__':
	timestamp = 1655615841
	print(type(timestamp))
	print(timestamp)
	datestr = stampToStr(timestamp)
	print(type(datestr))
	print(datestr)
	timestamp = strToStamp(datestr)
	print(type(timestamp))
	print(timestamp)
	datestime = datetime.now()
	print(type(datestime))
	print(datestime)
	datestime_str = dateTimeToStr(datestime)
	print(type(datestime_str))
	print(datestime_str)
	datetime_dtime = strToDateTime(datestime_str)
	print(type(datetime_dtime))
	print(datetime_dtime)
	datestime_str = dateTimeToStr(datetime_dtime)
	print(type(datestime_str))
	print(datestime_str)
	timestamp = 1655615841
	dtime = stampToDateTime(timestamp)
	print(type(dtime))
	print(dtime)
	timestamp = dateTimeToStamp(dtime)
	print(type(timestamp))
	print(timestamp)
