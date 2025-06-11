# Assignemnt 2

## Question 1 (Basic Decorator for Logging):
Create a Python decorator called
```bash
@log_function_call
```
that, when applied to a function,
prints a message to the console before the function is executed and after it completes. The
message before execution should state the function's name and the arguments it was called
with. The message after execution should state the function's name and its return value.


## Question 2 (Decorator for Caching/Memoization):
Design a decorator called 
```bash
@cache_result
```
that caches the return values of a function
based on its arguments. If the function is called with the same arguments again, it should
return the cached result instead of re-executing the function. The decorator should optionally
print a message indicating whether the result was retrieved from the cache or computed.


## Question 3 (Enforcing Interface with ABC):
Create an Abstract Base Class (ABC) called Shape using the abc module. This Shape
class should define two abstract methods:
```bash
area()
``` and
``bash
perimeter()
```
Then, create two
concrete classes, Circle and Rectangle, that inherit from Shape and implement these
abstract methods. Ensure that attempting to instantiate Shape directly raises an error.


## Question 4 (Pluggable Component Architecture with ABC):
Imagine you're building a data processing pipeline. Define an ABC called DataSource with
an abstract method
```bash
fetch_data()
```
This method should return some data (e.g., a list of
dictionaries). Then, create two concrete DataSourceimplementations: FileDataSource
(which reads data from a local file path) and APIDataSource (which simulates fetching
data from a web API endpoint).


## Question 5 (Defining a Printable Protocol):
Define a Python Protocol called Printable using the typing.Protocol module. This
protocol should specify that any class implementing it must have a method 
```bash
to_string()
```
that takes no arguments and returns a str. Create two classes, Book and Movie, that
conform to this Printable protocol (without explicitly inheriting from Printable). Write a
function
```bash
print_item(item: Printable)
```
that takes an object conforming to Printable
and calls its to_string() method.


## Question 6 (Data Processor Protocol):
Create a Protocol called DataProcessor that defines a method
```baah
process(data: list[int]) -> list[int]
```
This protocol represents any object that can take a list of
integers and return a processed list of integers. Implement two classes that conform to this
protocol: EvenFilter (which returns only even numbers) and SquareProcessor (which
returns the squares of the numbers). Write a function
```bash
apply_processor(processor: DataProcessor, input_data: list[int]) -> list[int]
```
that uses the protocol
for type hinting.


## Question 7 (Basic Command-Line Calculator):
Write a Python script that uses argparse to create a simple command-line calculator. It
should accept two numbers and an operation (add, subtract, multiply) as command-line
arguments. The script should then perform the specified operation and print the result.
Include a helpful description and argument help messages.


## Question 8 (Calculator with Decorator and Argparse):
Combine concepts from previous questions. Create a command-line calculator using
argparse (similar to Question 7). However, for each arithmetic operation function (e.g.,
add, subtract), apply the @log_function_call decorator you created in Question 1.
This will allow you to see the logging output when the calculator functions are called via the
command line.


## Question 9 (Pluggable Data Importer with ABC and Argparse):
Extend the DataSource ABC and its concrete implementations (from Question 4). Now,
modify the script to use argparse to allow the user to specify which data source to use from
the command line (e.g., --source file or --source api) and any necessary
arguments (e.g., --file-path data.txt or --api-endpoint
https://api.example.com/data). The script should then instantiate the appropriate
DataSource and fetch_data() from it.