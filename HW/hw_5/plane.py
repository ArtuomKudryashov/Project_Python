from HW.hw_5.transport import Transport


class Plane(Transport):
    def __init__(self, make, model, year, color, wingspan):
        super().__init__(make, model, year, color)
        self._wingspan = wingspan

    def get_wingspan(self):
        return self._wingspan

    def set_wingspan(self, wingspan):
        self._wingspan = wingspan

    def display_info(self):
        super().display_info()
        print(f"Wingspan: {self._wingspan}")