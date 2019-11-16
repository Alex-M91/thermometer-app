class Themperature(Cluj):
    def __init__(self, themperature = 0):
        self.themperature = themperature

    def get_themperature(self, instance, owner):
        return self.themperature

    def set_themperature(self, instance, themperature):
        return self.themperature


    def to_celsius(self):
        pass

    def to_fahrenheit(self):
        pass
