# calendar_convertor

 ## Table of contents
* [General info](#general-info)
* [Details](#details)

## General info
It's a simple python project that converts dates: Gregorian > Hijri > Jalali 


## Details
### 1. Converting Hijri date to Gregorian date

Example:

```
dc = DateConvert(1444,8,7)
gregorian_date = dc.hijri_to_gregorian() out: (2023,2,28) #Gregorian
```
### 2. Converting Gregorian date to Hijri date

Example:

```
dc = DateConvert(2023,2,28)
hijri_date = dc.gregorian_to_hijri() out: (1444,8,7) #Hijri
```
### 3. Converting Jalali date to Hijri date

Example:

```
dc = DateConvert(1401,12,9)
hijri_date = dc.jalali_to_hijri() out: (1444,8,7) #Hijri
```
