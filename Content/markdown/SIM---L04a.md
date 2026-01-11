# SIM   L04a

**Conversion date:** 2026-01-11
**Original file:** `SIM - L04a.pptx`
**Total slides:** 18

---


## Table of Contents

1. [Systems for Information Management](#slide-1-systems-for-information-management)
2. [Previously](#slide-2-previously)
3. [Today](#slide-3-today)
4. [Homework discussion](#slide-4-homework-discussion)
5. [More control within loops](#slide-5-more-control-within-loops)
6. [Useful: Escape sequences in strings](#slide-6-useful-escape-sequences-in-strings)
7. [Useful: Escape sequences in strings](#slide-7-useful-escape-sequences-in-strings)
8. [Better programs with functions](#slide-8-better-programs-with-functions)
9. [Better programs with functions](#slide-9-better-programs-with-functions)
10. [Variable scope in functions](#slide-10-variable-scope-in-functions)
11. [More operators](#slide-11-more-operators)
12. [Reacting to events](#slide-12-reacting-to-events)
13. [Reacting to events](#slide-13-reacting-to-events)
14. [Reacting to events](#slide-14-reacting-to-events)
15. [Reacting to events](#slide-15-reacting-to-events)
16. [Reacting to events](#slide-16-reacting-to-events)
17. [Homework](#slide-17-homework)
18. [Next Lecture](#slide-18-next-lecture)

## 1. Systems for Information Management {#slide-1-systems-for-information-management}

### Content

- Dr Imran U Khan			School of Engineering and Informatics

---

## 2. Previously {#slide-2-previously}

### Content

- Basic programming concepts
- Arrays
- Grouping of data
- Loops

- 2

- instruction1

?

- instruction2

- instruction3

- Yes

- No

- 10

- 45

- …

- …

- 0

- 1

- 2

- 3

- numbers = [];
- numbers[0] = 10;
- numbers[1] = 45;

---

## 3. Today {#slide-3-today}

### Content

- More basic programming concepts: Functions, Variable scope, Event handlers
- Homework discussion
- The use of break and continue in loops
- Escape sequences
- How to improve the structure of programs by using functions
- The scope of variables
- Reacting to events

---

## 4. Homework discussion {#slide-4-homework-discussion}

### Content

- Create a program that can add five integers
- Create an array of integers to store five numbers in
Use a loop of your choice to ask the user to enter five successive integers and store these in the array – to find out how, look up how the prompt() method of the window object works in a Javascript reference documentation
Use another kind of loop to iterate over and add all numbers stored in the array
Print out on screen the sum of all numbers.

---

## 5. More control within loops {#slide-5-more-control-within-loops}

### Content

- break & continue
break will stop the loop, no matter how many iterations would normally be left to do, and execution will continue with the next instruction after the loop.
continue only skips the current turn and will trigger another evaluation of the condition. In a for-loop, the post-loop action (usually incrementing the control variable) will be run before another evaluation is made.

---

## 6. Useful: Escape sequences in strings {#slide-6-useful-escape-sequences-in-strings}

### Content

What are escape sequences?
- Special characters inserted within a string
- Get translated into special symbols or functionality
Start with the back-slash symbol ( \ ), followed by the escape symbole.g. \n creates a new line, as in
Any other, ordinary characters around an escape sequence will be displayed as usual – including " " (space) characters!

- alert("Hello\nWorld!");

---

## 7. Useful: Escape sequences in strings {#slide-7-useful-escape-sequences-in-strings}

### Content

Useful: Escape sequences in strings

Common escape sequences

### Visual Analysis

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

## 8. Better programs with functions {#slide-8-better-programs-with-functions}

### Content

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

## 9. Better programs with functions {#slide-9-better-programs-with-functions}

### Content

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

## 10. Variable scope in functions {#slide-10-variable-scope-in-functions}

### Content

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

## 11. More operators {#slide-11-more-operators}

### Content

More operators

Mathematical operators

### Visual Analysis

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

## 12. Reacting to events {#slide-12-reacting-to-events}

### Content

- Events
Javascript can pick up events that happen around an HTML page and react to these
These events are triggered as an HTML page is loaded or unloaded, or if a user interacts with the webpage
This is useful for web applications, as we can give a user more control over the functions provided by our  programSee a reference of different events here:https://www.w3schools.com/tags/ref_eventattributes.asp

---

## 13. Reacting to events {#slide-13-reacting-to-events}

### Content

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

## 14. Reacting to events {#slide-14-reacting-to-events}

### Content

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

## 15. Reacting to events {#slide-15-reacting-to-events}

### Content

- Denoting event handler actions
Javascript events are often handled as seen in the examples, by referring to a function that has been written in a Javascript section / external file.
It is also possible to write the Javascript code directly as value of the event-handling HTML attribute. This can be useful if the required code is quite short.
However, be careful if quotation marks are needed in the Javascript – since double quotation marks are needed to designate the attribute value in HTML, the Javascript parameters must then use single quotation marks for disambiguation:

- <button onclick="alert('Button clicked')" </button>

---

## 16. Reacting to events {#slide-16-reacting-to-events}

### Content

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

## 17. Homework {#slide-17-homework}

### Content

- Explore how to create forms in HTML
Use the resources on Canvas to familiarise yourselves with HTML forms, especially the following tags:
- <form>
- <input>
- <label>

---

## 18. Next Lecture {#slide-18-next-lecture}

### Content

- Object orientation in programming
- Objects in Javascript

- 18

---


---

## Processing Metadata

### Slide Classification
- Text slides: 16
- Visual slides: 2
- Optimized percentage (without API): 88.9%

### API Costs
- Input tokens: 18,155
- Output tokens: 3,676
- Total cost: $0.1096 USD

### System
- Generated by: PPTX to Markdown Converter
- Date: 2026-01-11 19:05:44