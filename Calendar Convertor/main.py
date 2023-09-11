from convertor import hijri_julian, julian_gregorian, gregorian_hijri, jalali_gregorian

class DateConvert:

    def __init__(self, year, month, day):
        if isinstance(year, int):
            if year < 0:
                raise ValueError('year must be positive')
            else:
                self.year = year
        else:
            raise TypeError('year must be an int')

        if isinstance(month, int):
            if not (month in range(1, 13)):
                raise ValueError('month should be bitween 1 and 12')
            else:
                self.month = month
        else:
            raise TypeError('month must be an int')

        if isinstance(day, int):
            if not (month in range(1, 31)):
                raise ValueError('day should be bitween 1 and 30')
            else:
                self.day = day
        else:
            raise TypeError('day must be an int')


    def hijri_to_gregorian(self):
        jd = hijri_julian(self.year, self.month, self.day)
        gd = julian_gregorian(jd)
        return gd
    
    def gregorian_to_hijri(self):       
        hd = gregorian_hijri(self.year, self.month, self.day)
        return hd
    
    def jalali_to_hijri(self):
        jd = jalali_gregorian(self.year, self.month, self.day)
        hd = gregorian_hijri(jd[0], jd[1], jd[2])
        return hd

"""dc = DateConvert(1444,8,7)
gregorian_date = dc.hijri_to_gregorian()
print(gregorian_date)

dc = DateConvert(2023,2,28)
hijri_date = dc.gregorian_to_hijri()
print(hijri_date)

dc = DateConvert(1401,12,9)
hijri_date = dc.jalali_to_hijri()
print(hijri_date)"""