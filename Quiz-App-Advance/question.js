let questions = [
  // Quiz questions and answers
  {
    numb: 1,
    question: "What is the output of the following code?\n```python\nprint(type([]))\n```",
    answer: "<class 'list'>",
    options: [
      "<class 'list'>",
      "<class 'tuple'>",
      "<class 'dict'>",
      "<class 'set'>"
    ]
  },
  {
    numb: 2,
    question: "Which method can be used to remove whitespace from both ends of a string?",
    answer: "strip()",
    options: [
      "strip()",
      "trim()",
      "cut()",
      "delete()"
    ]
  },
  {
    numb: 3,
    question: "What is the result of `3 ** 2` in Python?",
    answer: "9",
    options: [
      "5",
      "6",
      "9",
      "8"
    ]
  },
  {
    numb: 4,
    question: "Which of the following is the correct syntax for defining a function in Python?",
    answer: "def myFunction():",
    options: [
      "function myFunction():",
      "def myFunction[]:",
      "def myFunction():",
      "function myFunction[]:"
    ]
  },
  {
    numb: 5,
    question: "What is the default value of the `sep` parameter in the `print()` function?",
    answer: "' '",
    options: [
      "','",
      "'\n'",
      "' '",
      "'\t'"
    ]
  },
  {
    numb: 6,
    question: "How do you create a dictionary in Python?",
    answer: "dict = {}",
    options: [
      "dict = {}",
      "dict = []",
      "dict = ()",
      "dict = set()"
    ]
  },
  {
    numb: 7,
    question: "What does the `len()` function do?",
    answer: "Returns the number of items in an object",
    options: [
      "Returns the number of items in an object",
      "Returns the length of an object",
      "Returns the sum of an object",
      "Returns the type of an object"
    ]
  },
  {
    numb: 8,
    question: "Which of the following is used to handle exceptions in Python?",
    answer: "try...except",
    options: [
      "try...except",
      "catch...throw",
      "handle...except",
      "error...catch"
    ]
  },
  {
    numb: 9,
    question: "What is the result of `5 // 2`?",
    answer: "2",
    options: [
      "2",
      "2.5",
      "2.0",
      "3"
    ]
  },
  {
    numb: 10,
    question: "Which of the following data types is immutable in Python?",
    answer: "tuple",
    options: [
      "list",
      "set",
      "dict",
      "tuple"
    ]
  },
  {
    numb: 11,
    question: "What will be the output of the following code?\n```python\nprint(\"Hello\".replace(\"l\", \"L\"))\n```",
    answer: "HeLLo",
    options: [
      "HeLLo",
      "HelLo",
      "HeLlo",
      "HeLLlo"
    ]
  },
  {
    numb: 12,
    question: "How do you access the first element of a list `my_list`?",
    answer: "my_list[0]",
    options: [
      "my_list[0]",
      "my_list[1]",
      "my_list[-1]",
      "my_list.first()"
    ]
  },
  {
    numb: 13,
    question: "Which function is used to get user input in Python?",
    answer: "input()",
    options: [
      "get()",
      "input()",
      "scan()",
      "read()"
    ]
  },
  {
    numb: 14,
    question: "What is the correct way to import the `math` module in Python?",
    answer: "import math",
    options: [
      "import math",
      "include math",
      "require math",
      "using math"
    ]
  },
  {
    numb: 15,
    question: "How can you comment a single line in Python?",
    answer: "# this is a comment",
    options: [
      "// this is a comment",
      "/* this is a comment */",
      "# this is a comment",
      "<!-- this is a comment -->"
    ]
  },
  {
    numb: 16,
    question: "What does the `range()` function return?",
    answer: "A sequence of numbers",
    options: [
      "A list of numbers",
      "A tuple of numbers",
      "A sequence of numbers",
      "A set of numbers"
    ]
  },
  {
    numb: 17,
    question: "Which of the following is NOT a valid variable name in Python?",
    answer: "my-variable",
    options: [
      "my_variable",
      "myVariable",
      "my-variable",
      "myVariable1"
    ]
  },
  {
    numb: 18,
    question: "What does `list.sort()` do in Python?",
    answer: "Sorts the list in place",
    options: [
      "Returns a sorted list",
      "Sorts the list in place",
      "Creates a new sorted list",
      "Sorts the list and returns the sorted list"
    ]
  },
  {
    numb: 19,
    question: "What is the output of the following code?\n```python\nprint(2 + 3 * 4)\n```",
    answer: "14",
    options: [
      "20",
      "14",
      "18",
      "10"
    ]
  },
  {
    numb: 20,
    question: "Which operator is used for floor division in Python?",
    answer: "//",
    options: [
      "/",
      "%",
      "//",
      "**"
    ]
  },
  {
    numb: 21,
    question: "What does `isinstance(x, int)` check?",
    answer: "If `x` is an integer",
    options: [
      "If `x` is an integer",
      "If `x` is a string",
      "If `x` is a float",
      "If `x` is a list"
    ]
  },
  {
    numb: 22,
    question: "How do you write an infinite loop in Python?",
    answer: "while True:",
    options: [
      "while True:",
      "for True:",
      "repeat:",
      "loop True:"
    ]
  },
  {
    numb: 23,
    question: "Which method adds an element to the end of a list?",
    answer: "append()",
    options: [
      "append()",
      "insert()",
      "extend()",
      "add()"
    ]
  },
  {
    numb: 24,
    question: "How do you define a class in Python?",
    answer: "class MyClass:",
    options: [
      "class MyClass:",
      "define MyClass:",
      "class MyClass[]:",
      "MyClass class:"
    ]
  },
  {
    numb: 25,
    question: "Which of the following is used to convert a string to an integer?",
    answer: "int()",
    options: [
      "int()",
      "float()",
      "str()",
      "convert()"
    ]
  },
  {
    numb: 26,
    question: "What does the `*args` syntax in a function definition do?",
    answer: "Allows the function to accept any number of positional arguments",
    options: [
      "Allows the function to accept any number of positional arguments",
      "Allows the function to accept any number of keyword arguments",
      "Multiplies all the arguments",
      "Unpacks a list of arguments"
    ]
  },
  {
    numb: 27,
    question: "Which of the following is used to define a multi-line string in Python?",
    answer: "Triple quotes (''' or \"\"\")",
    options: [
      "Double quotes (\")",
      "Single quotes (')",
      "Triple quotes (''' or \"\"\")",
      "Backticks (`)"
    ]
  },
  {
    numb: 28,
    question: "What is the purpose of the `pass` statement in Python?",
    answer: "To act as a placeholder for future code",
    options: [
      "To skip the rest of the loop",
      "To act as a placeholder for future code",
      "To pass control to the next function",
      "To indicate that a function doesn't return anything"
    ]
  },
  {
    numb: 29,
    question: "Which of the following is NOT a valid way to create a set in Python?",
    answer: "set = {1, 2, 3, 3, 4, 4}",
    options: [
      "set([1, 2, 3, 4])",
      "set((1, 2, 3, 4))",
      "{1, 2, 3, 4}",
      "set = {1, 2, 3, 3, 4, 4}"
    ]
  },
  {
    numb: 30,
    question: "What does the `__init__` method do in a Python class?",
    answer: "Initializes the object's attributes",
    options: [
      "Initializes the object's attributes",
      "Defines the class methods",
      "Creates a new instance of the class",
      "Destroys the object when it's no longer needed"
    ]
  },
  {
    numb: 31,
    question: "Which of the following is used to open a file in binary mode?",
    answer: "open('file.bin', 'rb')",
    options: [
      "open('file.bin', 'b')",
      "open('file.bin', 'binary')",
      "open('file.bin', 'rb')",
      "open('file.bin', 'bin')"
    ]
  },
  {
    numb: 32,
    question: "What is the output of `print(bool([]))`?",
    answer: "False",
    options: [
      "True",
      "False",
      "None",
      "[]"
    ]
  },
  {
    numb: 33,
    question: "Which of the following is used to remove a key-value pair from a dictionary?",
    answer: "del dict_name[key]",
    options: [
      "dict_name.remove(key)",
      "dict_name.pop(key)",
      "del dict_name[key]",
      "dict_name.delete(key)"
    ]
  },
  {
    numb: 34,
    question: "What does the `yield` keyword do in Python?",
    answer: "Creates a generator function",
    options: [
      "Returns a value from a function",
      "Creates a generator function",
      "Pauses the execution of a loop",
      "Raises an exception"
    ]
  },
  {
    numb: 35,
    question: "Which of the following is NOT a valid way to comment out multiple lines in Python?",
    answer: "/* This is a comment */",
    options: [
      "''' This is a comment '''",
      "\"\"\" This is a comment \"\"\"",
      "# This is a comment\n# This is another comment",
      "/* This is a comment */"
    ]
  },
  {
    numb: 36,
    question: "What is the purpose of the `with` statement in Python?",
    answer: "To ensure proper acquisition and release of resources",
    options: [
      "To define a new code block",
      "To handle exceptions",
      "To ensure proper acquisition and release of resources",
      "To create a new namespace"
    ]
  },
  {
    numb: 37,
    question: "Which of the following is used to find the maximum value in a list?",
    answer: "max(list_name)",
    options: [
      "list_name.max()",
      "max(list_name)",
      "list_name.largest()",
      "largest(list_name)"
    ]
  },
  {
    numb: 38,
    question: "What does the `is` operator check for?",
    answer: "Object identity",
    options: [
      "Value equality",
      "Type equality",
      "Object identity",
      "Existence of an object"
    ]
  },
  {
    numb: 39,
    question: "Which of the following is NOT a valid numeric type in Python?",
    answer: "double",
    options: [
      "int",
      "float",
      "complex",
      "double"
    ]
  },
  {
    numb: 40,
    question: "What is the output of `print('Hello'[::-1])`?",
    answer: "olleH",
    options: [
      "Hello",
      "olleH",
      "H",
      "o"
    ]
  },
  {
    numb: 41,
    question: "Which module in Python is used for regular expressions?",
    answer: "re",
    options: [
      "regex",
      "re",
      "regexp",
      "pyregex"
    ]
  },
  {
    numb: 42,
    question: "What does the `lambda` keyword create?",
    answer: "An anonymous function",
    options: [
      "A new variable",
      "A class method",
      "An anonymous function",
      "A decorator"
    ]
  },
  {
    numb: 43,
    question: "Which of the following is used to round a number to the nearest integer?",
    answer: "round(number)",
    options: [
      "round(number)",
      "ceil(number)",
      "floor(number)",
      "int(number)"
    ]
  },
  {
    numb: 44,
    question: "What is the purpose of the `global` keyword in Python?",
    answer: "To declare a global variable inside a function",
    options: [
      "To create a new global variable",
      "To declare a global variable inside a function",
      "To prevent a variable from being modified",
      "To delete a global variable"
    ]
  },
  {
    numb: 45,
    question: "Which of the following is NOT a valid way to create a tuple?",
    answer: "tuple = (item1; item2; item3)",
    options: [
      "tuple = (item1, item2, item3)",
      "tuple = item1, item2, item3",
      "tuple = tuple([item1, item2, item3])",
      "tuple = (item1; item2; item3)"
    ]
  },
  {
    numb: 46,
    question: "What does the `enumerate()` function do?",
    answer: "Returns an iterator of tuples containing indices and values of a list",
    options: [
      "Counts the number of items in an iterable",
      "Returns an iterator of tuples containing indices and values of a list",
      "Enumerates all the methods of an object",
      "Creates a numbered list"
    ]
  },
  {
    numb: 47,
    question: "Which of the following is used to get the memory address of an object in Python?",
    answer: "id(object)",
    options: [
      "address(object)",
      "memory(object)",
      "id(object)",
      "loc(object)"
    ]
  },
  {
    numb: 48,
    question: "What is the purpose of the `__name__` variable in Python?",
    answer: "To determine if a script is being run directly or being imported",
    options: [
      "To store the name of the current module",
      "To determine if a script is being run directly or being imported",
      "To define the name of a class",
      "To store the name of the current function"
    ]
  },
  {
    numb: 49,
    question: "Which of the following is NOT a valid string formatting method in Python?",
    answer: "String concatenation using the '+' operator",
    options: [
      "%-formatting",
      "str.format()",
      "f-strings (formatted string literals)",
      "String concatenation using the '+' operator"
    ]
  },
  {
    numb: 50,
    question: "What is the output of `print(2 * 3 ** 3)`?",
    answer: "54",
    options: [
      "18",
      "54",
      "36",
      "216"
    ]
  }
];   
