class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.one_year_earth_sec = 31557600

    def on_earth(self):
        return round(self.seconds/self.one_year_earth_sec,2)

    def on_mercury(self):
        one_year_mercury_sec = self.one_year_earth_sec * 0.2408467
        return round(self.seconds / one_year_mercury_sec,2)

    def on_venus(self):
        one_year_venus_sec = self.one_year_earth_sec * 0.61519726
        return round(self.seconds / one_year_venus_sec,2)

    def on_mars(self):
        one_year_mars_sec = self.one_year_earth_sec * 1.8808158
        return round(self.seconds / one_year_mars_sec,2)

    def on_jupiter(self):
        one_year_jupiter_sec = self.one_year_earth_sec * 11.862615
        return round(self.seconds / one_year_jupiter_sec,2)   

    def on_saturn(self):
        one_year_saturn_sec = self.one_year_earth_sec * 29.447498
        return round(self.seconds / one_year_saturn_sec,2)

    def on_uranus(self):
        one_year_uranus_sec = self.one_year_earth_sec * 84.016846
        return round(self.seconds / one_year_uranus_sec,2)

    def on_neptune(self):
        one_year_neptuno_sec = self.one_year_earth_sec * 164.79132
        return round(self.seconds / one_year_neptuno_sec,2)
