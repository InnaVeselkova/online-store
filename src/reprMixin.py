class ReprMixin:
    def __init__(self):
        super().__init__()

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name} ({self.name}, {self.description}, {self.price}, {self.quantity})"
