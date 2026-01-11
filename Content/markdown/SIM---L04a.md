# SIM   L04a


## Systems for Information Management


- Dr Imran U Khan			School of Engineering and Informatics

---

## Previously


- Basic programming concepts
- Arrays
- Grouping of data
- Loops

- instruction1

?

- instruction2

- instruction3

- Yes

- No

- 45

- …

- …

- 1

- 3

- numbers = [];
- numbers[0] = 10;
- numbers[1] = 45;

---

## Today


- More basic programming concepts: Functions, Variable scope, Event handlers
- Homework discussion
- The use of break and continue in loops
- Escape sequences
- How to improve the structure of programs by using functions
- The scope of variables
- Reacting to events

---

## Homework discussion


- Create a program that can add five integers
- Create an array of integers to store five numbers in
Use a loop of your choice to ask the user to enter five successive integers and store these in the array – to find out how, look up how the prompt() method of the window object works in a Javascript reference documentation
Use another kind of loop to iterate over and add all numbers stored in the array
Print out on screen the sum of all numbers.

---

## More control within loops


- break & continue
break will stop the loop, no matter how many iterations would normally be left to do, and execution will continue with the next instruction after the loop.
continue only skips the current turn and will trigger another evaluation of the condition. In a for-loop, the post-loop action (usually incrementing the control variable) will be run before another evaluation is made.

---

## Useful: Escape sequences in strings


What are escape sequences?
- Special characters inserted within a string
- Get translated into special symbols or functionality
Start with the back-slash symbol ( \ ), followed by the escape symbole.g. \n creates a new line, as in
Any other, ordinary characters around an escape sequence will be displayed as usual – including " " (space) characters!

- alert("Hello\nWorld!");

---

## Useful: Escape sequences in strings


Useful: Escape sequences in strings

Common escape sequences


# Escape Sequences in Strings

## Common Escape Sequences

Escape sequences are special character combinations used within strings to represent characters that would otherwise be difficult or impossible to include directly.

### Standard Escape Sequences

| Escape Sequence | Description |
|----------------|-------------|
| `\n` | Newline (line break) |
| `\t` | Tab (horizontal tabulation) |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |
| `\r` | Carriage return |
| `\b` | Backspace |
| `\f` | Form feed |

## Purpose and Usage

Escape sequences allow programmers to:
- Insert special characters that have syntactic meaning in the programming language
- Include non-printable control characters in strings
- Format text output with proper spacing and line breaks
- Represent characters that cannot be typed directly on a keyboard

---

## Better programs with functions


- Functions
Functions can be used to structure code by grouping together those actions that perform a particular task
- Functions make programs more flexible, and minimise code duplication
- They also make code easier to maintain
Functions can be given parametersas input, and can return a result tothe point of call

- <script type="text/javascript">
- some_instruction;
- myFunction(…);
- another_instruction;
...
- function myFunction(parameters) {
- // do stuff
- return something;
- }
- </script>

---

## Better programs with functions


- Function declaration
- e.g.,

- function identifier(parameter1, parameter2, ...)
- {
- instruction;
- another_instruction;
- }

- function add(a, b)
- {
- var result = a + b;
- return result;
- }

---

## Variable scope in functions


- var c = 23;
- var d = add(c,12);		// function call, invokes the function
- alert(d);
- // the "normal" program stops here
- function add(a, b) 	// function declaration
- {
- var result = a + b;
- return result;
- }

- Functions

These variables have local scope here:They are only "known" within the current function

- Important aspect:Variables can have different "scope"

These variables have global scopeWe can access them anywhere in the program

---

## More operators


More operators

Mathematical operators


# Mathematical Operators

## Additional Operators

Beyond basic arithmetic operations, programming languages provide additional mathematical operators for common calculations:

### Exponentiation Operator
- **Operator:** `**`
- **Purpose:** Raises a number to a power
- **Usage:** `base ** exponent`
- **Example:** `2 ** 3` calculates 2³ = 8

### Modulo Operator
- **Operator:** `%`
- **Purpose:** Returns the remainder after division
- **Usage:** `dividend % divisor`
- **Example:** `10 % 3` returns 1 (since 10 ÷ 3 = 3 remainder 1)

### Floor Division Operator
- **Operator:** `//`
- **Purpose:** Performs division and rounds down to the nearest integer
- **Usage:** `dividend // divisor`
- **Example:** `10 // 3` returns 3 (discarding the decimal portion)

## Use Cases

- **Exponentiation:** Scientific calculations, compound interest, area/volume formulas
- **Modulo:** Checking even/odd numbers, cycling through sequences, determining divisibility
- **Floor Division:** Distributing items evenly, calculating whole units, pagination logic

---

## Reacting to events


- Events
Javascript can pick up events that happen around an HTML page and react to these
These events are triggered as an HTML page is loaded or unloaded, or if a user interacts with the webpage
This is useful for web applications, as we can give a user more control over the functions provided by our  programSee a reference of different events here:https://www.w3schools.com/tags/ref_eventattributes.asp

---

## Reacting to events


- Events example: Reacting to a click

- <html>
- <head>
- <script type="text/javascript">
- function doSomething() {
- alert("Button clicked");
- }
- </script>
- </head>
- <body>
- <button onclick="doSomething()"><button>
- </body>
- </html>

---

## Reacting to events


- Events example: Detecting change

- <html>
- <head>
- <script type="text/javascript">
- function doSomething() {
- alert("You changed your name");
- }
- </script>
- </head>
- <body>
- <form>
- <label>Name</label>
- <input type="text" onchange="doSomething()">
- </form>
- </body>
- </html>

---

## Reacting to events


- Denoting event handler actions
Javascript events are often handled as seen in the examples, by referring to a function that has been written in a Javascript section / external file.
It is also possible to write the Javascript code directly as value of the event-handling HTML attribute. This can be useful if the required code is quite short.
However, be careful if quotation marks are needed in the Javascript – since double quotation marks are needed to designate the attribute value in HTML, the Javascript parameters must then use single quotation marks for disambiguation:

- <button onclick="alert('Button clicked')" </button>

---

## Reacting to events


- Events example: A mouseover effect

- <html>
- <body>
- <form>
- <label>Name</label>
- <input type="text" onmouseover="this.style.color='red'" 	onmouseout="this.style.color='black'">
- </form>
- </body>
- </html>

---

## Homework


- Explore how to create forms in HTML
Use the resources on Canvas to familiarise yourselves with HTML forms, especially the following tags:
- <form>
- <input>
- <label>

---

## Next Lecture


- Object orientation in programming
- Objects in Javascript

---
