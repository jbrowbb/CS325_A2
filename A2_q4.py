from abc import ABC, abstractmethod
import json
import random

class DataSource(ABC):
    @abstractmethod
    def fetch_data(self):
        pass

class FileDataSource(DataSource):
    def __init__(self, file_path):
        self.file_path = file_path

    def fetch_data(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return data
    

class APIDataSource(DataSource):
    def fetch_data(self):
        sample_data = [
            {"id": 1, "name": "Billy", "score": random.randint(50, 100)},
            {"id": 2, "name": "Bob", "score": random.randint(50, 100)},
            {"id": 3, "name": "Joe", "score": random.randint(50, 100)},
        ]
        return sample_data
    

def process_data(data_source: DataSource):
    data = data_source.fetch_data()
    for item in data:
        print(item)


api_data_source = APIDataSource()
process_data(api_data_source)