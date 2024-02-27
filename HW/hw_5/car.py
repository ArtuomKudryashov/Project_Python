from HW.hw_5.transport import Transport


class Car (Transport):
    def __init__(self,make,model,year,color,emgine_type):
        super().__init__(make,model,year,color)
        self.engine_type = emgine_type

    def get_engine_type(self):
        return self.engine_type

    def set_engine_type(self, engine_type):
        self.engine_type = engine_type

    def display_info(self):
        super().display_info()
        print(f"Engine Type: {self.engine_type}")