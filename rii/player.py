class Player:
    __instance = None

    def __new__(cls, name):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.name = name
        return cls.__instance

    def get_name(self):
        return self.name