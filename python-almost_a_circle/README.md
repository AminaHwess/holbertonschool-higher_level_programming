<h1><p align="center"> Python - Almost a Circle </h1></p></font>

Greetings to the "Almost a Circle" project! In this endeavor, I've leveraged my proficiency in Python's object-oriented programming paradigm to craft a trio of interconnected classes that encapsulate the essence of rectangles and squares. To rigorously validate the correctness and robustness of each class, I've meticulously constructed an extensive suite of tests utilizing the unittest module.


Throughout this project, I've applied a lot of Python concepts, including:

- Private attributes
- Getter/setter methods
- Class/static methods
- Inheritance
- File input / output
- `args`/`kwargs`
- JSON and CSV serialization/deserialization

## Classes
### Base
* The Base class serves as the foundational class for managing rectangles and squares.
* It features a private class attribute __nb_objects to keep track of the number of instances created.
* The constructor __init__ allows for object creation with an optional ID parameter.
* Static methods such as to_json_string and from_json_string facilitate JSON representation and parsing of lists of dictionaries.
* The save_to_file and load_from_file methods enable saving and loading instances to and from JSON files.

### Rectangle
* The Rectangle class represents rectangles and extends the functionality provided by the Base class.
* The constructor __init__ allows for the creation of rectangle instances with specified width, height, position (x, y), and an optional ID.
* Properties (width, height, x, y) and corresponding setters ensure encapsulation and validate input data.
* Methods include area() to calculate the area of the rectangle, display() to print the rectangle to stdout, __str__() to provide a string representation, update() to modify attributes based on arguments or keyword arguments, and to_dictionary() for dictionary representation.

### Square
* The Square class inherits from the Rectangle class and shares similar attributes and methods.
* The constructor __init__ enables the creation of square instances with a specified size, position (x, y), and an optional ID.
* The __str__ method provides a string representation for square instances.
* The size property and corresponding setter ensure encapsulation and validate input data.
* Additional methods include update() for modifying attributes based on arguments or keyword arguments and to_dictionary() for dictionary representation.

# Author
Amina Hwess <https://github.com/AminaHwess/>
