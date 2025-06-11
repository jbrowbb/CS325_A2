from abc import ABC, abstractmethod
import json
import random
import argparse
import os



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


def main():
    parser = argparse.ArgumentParser(description="Choose a data source")
    parser.add_argument('--source', choices=['file', 'api'], required=True, help='Select the data source: file or api')
    parser.add_argument('--file-path', help='Path to the JSON file (required if source is file)')

    args = parser.parse_args()

    if args.source == 'file':
        if not args.file_path:
            parser.error("--file-path is required when --source is 'file'")
        if not os.path.exists(args.file_path):
            parser.error(f"File not found: {args.file_path}")
        data_source = FileDataSource(args.file_path)

    elif args.source == 'api':
        data_source = APIDataSource()

    else:
        parser.error("Invalid data source selected.")

    process_data(data_source)

if __name__ == "__main__":
    main()