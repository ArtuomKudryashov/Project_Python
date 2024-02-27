from HW.hw_5.transport import Transport


class Bike(Transport):
    def __init__(self, make, model, year, color, suspension_type):
        super().__init__(make, model, year, color)
        self._suspension_type = suspension_type

    def get_suspension_type(self):
        return self._suspension_type

    def set_suspension_type(self, suspension_type):
        self._suspension_type = suspension_type

    def display_info(self):
        super().display_info()
        print(f"Suspension Type: {self._suspension_type}")
