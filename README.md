# BrainFuck-Compiler

This is a prototype of a brainfuck compiler implemented in python which just uses the basics of it, so you are only able to write your own brainfuck code and compile it through this project, but you will not be able to see memory and more cool functionalities which will be implemented in a new version made in the browser that will be fully dynamic to the user.

# Tests
In order to run tests you need to use the following command inside the project folder:
```sh
$ python -m unittest test.py
```

if you prefer a more colorful version to run tests you can also install 'green' by using this command:

```sh
$ pip install green
```

and then run tests with this command:
```sh
$ green test.py
```

# TO-DO
- Add more and better tests
- Add support for nested loops
- Be able to load custom BrainFuck code from a file
- Create a function that generates the hexadecimal version of the memory pointers once the program finished executing
