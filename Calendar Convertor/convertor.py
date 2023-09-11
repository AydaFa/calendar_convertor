
def hijri_julian(hijri_year, hijri_month, hijri_day):
    day = int(((11 * int(hijri_year) + 3) / 30 + 354 * int(hijri_year) + 30 * int(hijri_month)
            - (int(hijri_month) - 1) / 2 + int(hijri_day) + 1948440 - 385))
    return day


def julian_gregorian(julian_date):
    j = int(julian_date) - 1721425.5
    year = int((j - 0.5) / 365.242198) + 1
    day = int((j - ((year - 1) * 365.242198 + 0.5)) + 0.5)
    if day < 186:
        month = int((day + 31) / 31)
        day = day % 31
    else:
        month = int((day - 186) / 30) + 7
        day = (day - 186) % 30
    return year, month, day


def gregorian_hijri(gregorian_year, gregorian_month, gregorian_day):
    jd = int((1461 * (gregorian_year + 4800 + (gregorian_month - 14) / 12)) / 4 +
             (367 * (gregorian_month - 2 - 12 * ((gregorian_month - 14) / 12))) / 12 -
             (3 * ((gregorian_year + 4900 + (gregorian_month - 14) / 12) / 100)) / 4 +
             gregorian_day - 32075)
    l = jd - 1948439 + 10632
    n = int((l - 1) / 10631)
    l = l - 10631 * n + 354
    j = ((int((10985 - l) / 5316)) * (int((50 * l) / 17719))) + ((int(l / 5670)) * (int((43 * l) / 15238)))
    l = l - ((int((30 - j) / 15)) * (int((17719 * j) / 50))) - ((int(j / 16)) * (int((15238 * j) / 43))) + 29
    hijri_month = int((24 * l) / 709)
    hijri_day = l - int((709 * hijri_month) / 24)
    hijri_year = (30 * n) + j - 30
    return hijri_year, hijri_month, hijri_day
 

def jalali_gregorian(jalali_year, jalali_month, jalali_day):
    jalali_year += 1595
    days = -355668 + (365 * jalali_year) + ((jalali_year // 33) * 8) + (((jalali_year % 33) + 3) // 4) + jalali_day
    if (jalali_month < 7):
        days += (jalali_month - 1) * 31
    else:
        days += ((jalali_month - 7) * 30) + 186
    gregorian_year = 400 * (days // 146097)
    days %= 146097
    if (days > 36524):
        days -= 1
        gregorian_year += 100 * (days // 36524)
        days %= 36524
        if (days >= 365):
            days += 1
    gregorian_year += 4 * (days // 1461)
    days %= 1461
    if (days > 365):
        gregorian_year += ((days - 1) // 365)
        days = (days - 1) % 365
    gregorian_day = days + 1
    if ((gregorian_year % 4 == 0 and gregorian_year % 100 != 0) or (gregorian_year % 400 == 0)):
        kabise = 29
    else:
        kabise = 28
    sal_a = [0, 31, kabise, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    gregorian_month = 0
    while (gregorian_month < 13 and gregorian_day > sal_a[gregorian_month]):
        gregorian_day -= sal_a[gregorian_month]
        gregorian_month += 1
    return gregorian_year,gregorian_month,gregorian_day

