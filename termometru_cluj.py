class Thermometer():
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def get_temperature(self, unit="celsius"):
        if unit=="celsius":
            return self.temperature
        elif unit=="fahrenheit":
            return self.to_fahrenheit(self.temperature)

    def set_temperature(self, temperature):
        self.temperature = temperature

    def to_celsius(self, temperature):
        temperature = (temperature - 32) * 5 / 9
        return temperature

    def to_fahrenheit(self, temperature):
        temperature = temperature * 1.8 + 32
        return temperature
