class Transport:
    def __init__(self, __make, model, year, color):
        self.__make = __make
        self._model = model
        self._year = year
        self._color = color

    def  get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    def get_model(self):
        return self._model

    def set_model(self,model):
        self._model = model


    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year

    def get_color(self):
        return self._color

    def set_color(self,color):
        self._color=color

    def display_info(self):
        print(f"Make: {self.__make}, Model: {self._model}, Year: {self._year}, Color: {self._color}")




