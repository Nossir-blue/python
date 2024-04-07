class time:
    @classmethod
    def fomrtimestamp(cls, t):
        y, m ,d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
        return cls(y,m,d)

    @classmethod
    def today(cls):
        t = _time.time()
        return cls.fomrtimestamp(t)
    
    @classmethod
    def fromordinal(cls, n):
        pass