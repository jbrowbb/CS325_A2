from typing import Protocol, List

class DataProcessor(Protocol):
    def process(self, data: List[int]) -> List[int]:
        ...


class EvenFilter:
    def process (self, data: List[int]) -> List[int]:
        return [x for x in data if x % 2 == 0]


class SquareProcessor:
    def process(self, data: List[int]) -> List[int]:
        return [x ** 2 for x in data]
    

def apply_processor(processor: DataProcessor, input_data: List[int]) -> List[int]:
    return processor.process(input_data)


if __name__ == "__main__":
    numbers = [1,2,3,4,5,6,7,8,9]

    even_filter = EvenFilter()
    square_processor = SquareProcessor()

    print("EvenFilter:", apply_processor(even_filter, numbers))
    print("SquareProcessor:", apply_processor(square_processor, numbers))