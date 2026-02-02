class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def print_first_name(self):
        print(f"Юра: {self.first_name}")
    def print_last_name(self):
        print(f"Тараскин: {self.last_name}")
    def print_full_name(self):
           print(f"Юра Таараскин: {self.first_name} {self.last_name}")


