class TimeSpan:
    def __init__(self,weeks,days,hours):
        if (type(weeks) is not int) or (type(days) is not int) or (type(hours) is not int):
            raise TypeError
        if (weeks < 0) or (days < 0) or (hours < 0):
            raise ValueError
        self.weeks = weeks
        self.days = days
        self.hours = hours
        self.days += self.hours//24
        self.weeks += self.days//7
        self.hours %= 24
        self.days %= 7

    def __str__(self):
        weeks = str(self.weeks)
        days = str(self.days)
        hours = str(self.hours)
        return weeks.zfill(2)+"W "+days+"D "+hours.zfill(2)+"H"

    def getTotalHours(self):
        return self.weeks*7*24 + self.days*24 + self.hours

    def __add__(self, other):
        if isinstance(other, TimeSpan):
            return TimeSpan(self.weeks + other.weeks, self.days + other.days, self.hours + other.hours)
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, int):
            if other > 0:
                return TimeSpan(self.weeks*other, self.days*other, self.hours*other)
            else:
                raise ValueError
        else:
            raise TypeError

    def __rmul__(self, other):
        if isinstance(other, int):
            if other > 0:
                return TimeSpan(self.weeks*other, self.days*other, self.hours*other)
            else:
                raise ValueError
        else:
            raise TypeError
