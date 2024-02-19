from HW.hw_5.transport import Transport


class Train(Transport):
    def __init__(self, make, model, year, color, carriage_count):
        super().__init__(make, model, year, color)
        self._carriage_count = carriage_count

    def get_carriage_count(self):
        return self._carriage_count

    def set_carriage_count(self, carriage_count):
        self._carriage_count = carriage_count

    def display_info(self):
        super().display_info()
        print(f"Carriage Count: {self._carriage_count}")