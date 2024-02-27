from HW.hw_5.transport import Transport


class Car2(Transport):
    def __init__ (self):
        pass
    def set_attribute(self,attribute_model, value):
        setattr(self, attribute_model, value)