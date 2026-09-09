class DataLoader:
    def __init__(self, data_directory='data'):
        self.data_directory = data_directory

    def load(self, data):
        return data