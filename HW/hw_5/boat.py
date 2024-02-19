from HW.hw_5.transport import Transport


class Boat(Transport):
    def __init__(self, make, model, year, color, hull_material):
        super().__init__(make, model, year, color)
        self._hull_material = hull_material

    def get_hull_material(self):
        return self._hull_material

    def set_hull_material(self, hull_material):
        self._hull_material = hull_material

    def display_info(self):
        super().display_info()
        print(f"Hull Material: {self._hull_material}")