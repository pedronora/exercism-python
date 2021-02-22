class Clock:
    def __init__(self, hour, minute):
        self.minute = minute
        self.hour = hour + self.minute // 60
        
        self.minute %= 60
        self.hour %= 24     

    def __repr__(self):
        return f'{self.hour:02}:{self.minute:02}'

    def __eq__(self, other):
        return repr(self) == other

    def __add__(self, minutes):
        return Clock(self.hour, (self.minute + minutes))

    def __sub__(self, minutes):
        return Clock(self.hour, (self.minute - minutes))
