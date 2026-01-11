# SIM   L03a

**Conversion date:** 2026-01-11
**Original file:** `SIM - L03a.pptx`
**Total slides:** 41

---


## Table of Contents

1. [Systems for Information ManagementLecture 3a](#slide-1-systems-for-information-managementlecture-3a)
2. [Previously](#slide-2-previously)
3. [Today](#slide-3-today)
4. [Terminology](#slide-4-terminology)
5. [Terminology](#slide-5-terminology)
6. [Terminology](#slide-6-terminology)
7. [Terminology](#slide-7-terminology)
8. [Terminology](#slide-8-terminology)
9. [Terminology](#slide-9-terminology)
10. [Terminology](#slide-10-terminology)
11. [Hello World!](#slide-11-hello-world)
12. [Javascript](#slide-12-javascript)
13. [Basic Coding Conventions](#slide-13-basic-coding-conventions)
14. [Basic Coding Conventions](#slide-14-basic-coding-conventions)
15. [Basic Coding Conventions](#slide-15-basic-coding-conventions)
16. [Basic Coding Conventions](#slide-16-basic-coding-conventions)
17. [Basic Coding Conventions](#slide-17-basic-coding-conventions)
18. [Basic Coding Conventions](#slide-18-basic-coding-conventions)
19. [Basic Coding Conventions](#slide-19-basic-coding-conventions)
20. [Variables](#slide-20-variables)
21. [Variables](#slide-21-variables)
22. [Variables](#slide-22-variables)
23. [Variables](#slide-23-variables)
24. [Variables](#slide-24-variables)
25. [Variables](#slide-25-variables)
26. [Variables](#slide-26-variables)
27. [Variables](#slide-27-variables)
28. [Basic output in Javascript](#slide-28-basic-output-in-javascript)
29. [The Flow of Control & Making Choices](#slide-29-the-flow-of-control--making-choices)
30. [Making choices](#slide-30-making-choices)
31. [Making choices](#slide-31-making-choices)
32. [Making Choices](#slide-32-making-choices)
33. [Preview: Making Choices](#slide-33-preview-making-choices)
34. [Preview: Making Choices](#slide-34-preview-making-choices)
35. [Preview: Making Choices](#slide-35-preview-making-choices)
36. [Preview: Making Choices](#slide-36-preview-making-choices)
37. [Preview: Making Choices](#slide-37-preview-making-choices)
38. [Preview: Making Choices](#slide-38-preview-making-choices)
39. [Useful operators to use in expressions](#slide-39-useful-operators-to-use-in-expressions)
40. [Useful operators to use in expressions](#slide-40-useful-operators-to-use-in-expressions)
41. [Next Lectures](#slide-41-next-lectures)

## 1. Systems for Information ManagementLecture 3a {#slide-1-systems-for-information-managementlecture-3a}

### Content

- Dr Imran U Khan		School of Engineering and Informatics

---

## 2. Previously {#slide-2-previously}

### Content

- Computer Systems, Networks, the Internet / WWW
- How computers work from a physical and logical perspective
- How computers process, store, and transmit information

- 2

---

## 3. Today {#slide-3-today}

### Content

- Client-side scripting / Basic programming concepts
- Markup vs Programs
- Algorithms
- Server- vs client-side scripting
- Introduction to Javascript, and a few handy basics
- Basic syntax and conventions
- Variables & basic control structures

- 3

---

## 4. Terminology {#slide-4-terminology}

### Content

- Markup documents and Programs
A markup document contains structured information that can be read and interpreted by a program (e.g., a web browser, for rendering a web page).
(Imperative) programs implement algorithms as a sequence of instructions.
It is possible to use scripts (computer programs) in combination with the markup code, e.g. to enhance user experience, or provide more functionality.

- 4

<!DOCTYPE html><html>   <head>       <title>My website</title>       <script type=“text/javascript” src=“script.js”></script>   </head>   <body>      <h1 id=“h”>Welcome to my homepage</h1>      <p><button onclick=“myFunction()”>O</button></p>   </body></html>

- // this is  the Javascript in the file “script.js”
- function myFunction() {
- var x = document.getElementById(“h").innerHTML;
- alert(x);
- document.getElementById(“h").innerHTML = “new text";
- }

---

## 5. Terminology {#slide-5-terminology}

### Content

What is an algorithm?
A sequence of instructions that a computer can carry out to perform a task
- Characteristics of algorithms:
- Finite: 		Terminates after a finite number of steps
- Definite: 	Each step must be clearly defined, and instructions unambiguous
Effective:	Operations must be computable – in principle, a human should be 			able to work them out using pen and paper.
- Inputs:		Zero or more well-defined inputs
Outputs:	At least one output as a result, with a specified relation to the inputs

- 5

---

## 6. Terminology {#slide-6-terminology}

### Content

- Algorithm: A simple example
- A vending machine

- 6

- Ask for money p

- User selects drink d

- User inserts money m

- Dispense drink d

- Finish

- Start

Is m >= p?

- Yes

- No

---

## 7. Terminology {#slide-7-terminology}

### Content

- Programming / Scripting
We use programming languages (PL) to create computer programs.
Javascript is a PL that can be used in combination with HTML, for example,
to apply CSS dynamically on a web page.
to check forms have been filled in correctly before they get submitted.
manipulate web page content (e.g., perform calculations, show or hide elements).
Javascript is an “interpreted” language – a web browser can translate and execute the human-readable statements in the “script” at runtime.
Interpreted programming languages are also called “scripting” languages.

- 7

---

## 8. Terminology {#slide-8-terminology}

### Content

Terminology

Client- vs. server-side scripting

On the Internet, user devices and programs (clients) communicate with server hosts to retrieve or exchange information (Websites, mail, media, …)
A simple example would be a web browser on the client side requesting an HTML resource from a web server, when someone visits a website:

8

HTTP

Server

Client

### Visual Analysis

# Client-Side vs. Server-Side Scripting

## Client-Server Architecture

On the Internet, user devices and programs (clients) communicate with server hosts to retrieve or exchange information including:
- Websites
- Mail
- Media
- Other resources

## Basic Client-Server Communication Model

The fundamental interaction involves:

**Client** ↔ **HTTP** ↔ **Server**

### Example Scenario

A web browser (client-side) requests an HTML resource from a web server when someone visits a website. This represents the most basic form of client-server communication on the web.

## Key Components

- **Client**: The user's device or program making requests (e.g., web browser)
- **Server**: The host system that provides resources and responds to requests
- **HTTP**: The communication protocol used to transfer data between client and server

---

## 9. Terminology {#slide-9-terminology}

### Content

Terminology

Server-side scripting

If scripts can be used to interact with and manipulate the HTML, there are two principal opportunities here to do so.
The server could run a script to process the HTTP request and assemble an HTML page that contains the correct information to be sent back to the client:(e.g., the requested information, an error message, an authentication request, …)

9

SCRIPT

Server

Client

HTML

### Visual Analysis

# Server-Side Scripting

## Definition

Server-side scripting is a method where scripts execute on the server to process HTTP requests and dynamically generate HTML pages before sending them to the client.

## How It Works

When a client makes an HTTP request, the server runs a script that:
- Processes the incoming HTTP request
- Assembles an HTML page dynamically
- Includes the appropriate content based on the request
- Sends the complete HTML response back to the client

## Use Cases

Server-side scripts can generate HTML pages containing:
- Requested information from databases or other sources
- Error messages when problems occur
- Authentication requests for user login
- Customized content based on user data or preferences

## Request-Response Flow

1. Client sends HTTP request to server
2. Server executes script to process the request
3. Script generates appropriate HTML content
4. Server sends HTML response back to client
5. Client receives ready-to-display HTML page

## Key Characteristic

The processing and content generation occur entirely on the server before any HTML is transmitted to the client, allowing for dynamic content creation while maintaining control over business logic and data access.

---

## 10. Terminology {#slide-10-terminology}

### Content

Terminology

Client-side scripting

Once the HTML has been delivered to the client, a script could be run there, for example to
Control the rendering and functionality in the client browser, or
Check that information is correct before the next request is made to the server host

10

SCRIPT

Server

Client

HTML

### Visual Analysis

# Client-Side Scripting

## Definition

Client-side scripting refers to scripts that execute on the client (user's browser) after HTML content has been delivered from the server.

## Execution Flow

1. Server sends HTML to client
2. Script runs locally in the client's browser
3. No immediate server communication required for script execution

## Primary Purposes

### 1. Control Rendering and Functionality
- Manages how content appears and behaves in the browser
- Enables interactive user interface elements
- Allows dynamic content manipulation without server requests

### 2. Client-Side Validation
- Verifies information correctness before sending to server
- Reduces unnecessary server requests
- Provides immediate feedback to users
- Improves efficiency by catching errors early

## Architecture Pattern

The client-side scripting model involves:
- **Server**: Delivers initial HTML and script code
- **Client**: Receives HTML and executes the embedded or linked scripts locally
- **Script**: Runs in the browser environment to enhance functionality and user experience

---

## 11. Hello World! {#slide-11-hello-world}

### Content

- Your first program
Create a simple HTML page, and insert the following code into the <body> area:

- <script type="text/javascript">
- alert("Hello world!");
- </script>

<script> is an HTML tag that can be used to define areas that won’t be shown in the browser output, but interpreted as Javascript code instead

This instruction calls a predefined Javascript function, which takes the text “Hello World!” as an input and outputs it in a pop-up window

---

## 12. Javascript {#slide-12-javascript}

### Content

- Basic Syntax
Instead of embedding Javascript into the HTML file, we can also save the program code separately in a *.js file, and then link this file to the HTML markup code using the src attribute.
Go back to slide 4 to see an example of this.
However, no matter which way we choose, note that with <script>, we always need to specify the correct closing tag </script>We can’t use the <link> tag here, as we would for connecting a CSS style sheet and HTML. Browsers do not support this tag in connection with scripts.

- 12

- <script type="text/javascript" src="path_to_file.js"></script>

---

## 13. Basic Coding Conventions {#slide-13-basic-coding-conventions}

### Content

- A simple instruction
Each instruction is defined in the programming language with a unique name and syntax:
Apart from a few exceptions, modern programming languages are usually case-sensitive

- program instruction;
- program instruction;
- program instruction;
- program instruction;

- The semicolon marks
where an instruction ends.

---

## 14. Basic Coding Conventions {#slide-14-basic-coding-conventions}

### Content

- Block of code
A block of code contains one or more program instructions and is enclosed by curly braces:

- block descriptor
- {
- program instruction;
- program instruction;
- program instruction;
- }

---

## 15. Basic Coding Conventions {#slide-15-basic-coding-conventions}

### Content

- Block of code
A block of code contains one or more program instructions and is enclosed by curly braces:

- Open braces need to be
"closed" when a block ends.

- block descriptor
- {
- program instruction;
- program instruction;
- program instruction;
- }

---

## 16. Basic Coding Conventions {#slide-16-basic-coding-conventions}

### Content

- Block of code
A block of code contains one or more program instructions and is enclosed by curly braces:

- Here, too, the semicolon marks
where an instruction ends.
However, do note that the linewith the block descriptor does not end with a semicolon.

- block descriptor
- {
- program instruction;
- program instruction;
- program instruction;
- }

---

## 17. Basic Coding Conventions {#slide-17-basic-coding-conventions}

### Content

- Block of code
A block of code contains one or more program instructions and is enclosed by curly braces:

Instructions within a block of code are usually indented.

- block descriptor
- {
- program instruction;
- program instruction;
- program instruction;
- }

---

## 18. Basic Coding Conventions {#slide-18-basic-coding-conventions}

### Content

- function someName() {
- variable x;
- control structure(exp1) {
- program instruction;
- }
- program instruction;
- control structure(exp2) {
- program instruction;
- program instruction;
- control structure(exp3) {
- program instruction;
- program instruction;
- }
- }
- }

Properly indented code is easier to read.

This is pseudocode, not Javascript!

Opening block braces are often pulled up to the first line of the block

It is common practice to align closing braces with their corresponding block descriptors

---

## 19. Basic Coding Conventions {#slide-19-basic-coding-conventions}

### Content

- function someName() {
- variable x;
- control structure(exp1) {
- program instruction;
- }
- program instruction;
- control structure(exp2) {
- program instruction;
- program instruction;
- control structure(exp3) {
- program instruction;
- program instruction;
- }
- }
- }

- Simple statements: These will be carried out unconditionally

- Program flow

Conditional statements: These will be carried out depending on whether a condition is true.

Blocks of code can also be nested.

---

## 20. Variables {#slide-20-variables}

### Content

- Variables
A variable refers to an area of memory which contains data that can be referenced using a name (identifier) defined in the implementation of the program
Whenever the value of a variable is changed, the corresponding memory space is modified during the execution of the program

- Declaration of variable

- var number;

- identifier

- Keyword

---

## 21. Variables {#slide-21-variables}

### Content

- Variables: Storing data
- Values are stored into variables viaassignment statements
An assignment statement consists of the assignment operator (=) and an expression
An expression can be a number or a combinationof numbers, variables, and other operators
A variable can store different kinds of data (more onthis later…) but will always only store a single instance of that data.
That means if another value is assigned to the same variable, the previous value is lost!

- number = 20;

- Assignment Operator

- Expression

- Assigning a value to a variable

---

## 22. Variables {#slide-22-variables}

### Content

- Variables in memory

- RAM

- number

- var number;

- reserves space

---

## 23. Variables {#slide-23-variables}

### Content

- Variables in memory

- RAM

- 20

- var number;
- number = 20;

---

## 24. Variables {#slide-24-variables}

### Content

- Variables in memory

- RAM

- 25

- var number;
- number = 20;
- number = 20 + 5;

---

## 25. Variables {#slide-25-variables}

### Content

- Variables in memory

- RAM

- 33

- var number;
- number = 20;
- number = 20 + 5;
- number = number + 8;

---

## 26. Variables {#slide-26-variables}

### Content

- Variables in memory

- RAM

- 33

- var number;
- number = 20;
- number = 20 + 5;
- number = number + 8;

- Retrieves current value
- Evaluates expression
- Overwrites current value with new value

---

## 27. Variables {#slide-27-variables}

### Content

- Basic datatypes
Javascript is a so-called “dynamically-typed” language, which means we do not need to say which kind of data the variable stores. Javascript figures it out based on the data.
IntegerA number – the value can be specified as is. E.g. var number = 10;
StringText, the value must be specified using "". E.g., var name = "John";

---

## 28. Basic output in Javascript {#slide-28-basic-output-in-javascript}

### Content

How can we show the contents of a variable in Javascript?
- Alternatives
- Use the alert() function, as in our HelloWorld! Example
- Write as text directly into the HTML document, using document.write()
Write into an HTML element, such as <div>, using the innerHTML property of elements
Print out to the browser’s Javascript console, using the console.log() function.

---

## 29. The Flow of Control & Making Choices {#slide-29-the-flow-of-control--making-choices}

### Content

- The flow of control
By default, instructions in Javascript program will be carried out one by one.
The order of execution is important to consider if we want the program to run properly.

- var x = 12;
- x = x + 5;
- alert("x is " + x + 5);
- x = 25 * 3;
- document.write(x + 5 + " is x");

- finish

- start

- If we wanted to implement an element
- of choice, i.e. code that represents
- alternative paths of execution,
how could we do this?

Careful with dynamic types!Expressions are evaluated from left to right!

---

## 30. Making choices {#slide-30-making-choices}

### Content

- The flow of control
We need to create alternative blocks of code and then determine which of these blocks will be entered for execution by evaluating an expression.
- In pseudo code:							In Javascript:
- if (some expression is true)
- then do the following
- instructions here…
- otherwise, do something else
- other instructions here…

- if (i == 20) {
- alert("You entered 20");
- }
- else {
- alert("You entered something else");
- }

Is this expression true?

- true

- false

---

## 31. Making choices {#slide-31-making-choices}

### Content

- The flow of control
We need to create alternative blocks of code and then determine which of these blocks will be entered for execution by evaluating an expression.
- In pseudo code:							In Javascript:
- if (some expression is true)
- then do the following
- instructions here…
- otherwise, do something else
- other instructions here…

- if (i == 20) {
- alert("You entered 20");
- }
- else {
- alert("You entered something else");
- }

- "equals" operator

---

## 32. Making Choices {#slide-32-making-choices}

### Content

- Control Structures: The Conditional Statement
Conditional statements, also known as if-statements, enable our program to make choices based on the evaluation of a Boolean expression.
A Boolean expression invokes an operation that delivers either true or false as a result.
- Example:

- if (money >= price) {
- alert("Thank You");
- }

- "greater than or equal to" operator

---

## 33. Preview: Making Choices {#slide-33-preview-making-choices}

### Content

- Control Structures: The Conditional Statement
- Simple If-statement

- if(Boolean expression that returns true or false)
- {
- instructions that will be executed
- if Boolean expression returns true;
- }

The entire block of code will be ignored if the expression returns “false”, and the program will simply continue execution after the block

---

## 34. Preview: Making Choices {#slide-34-preview-making-choices}

### Content

- Control Structures: The Conditional Statement
- Simple If-statement

- if(money < 12)
- {
- alert("Insufficient funds");
- }

- "less than" operator

---

## 35. Preview: Making Choices {#slide-35-preview-making-choices}

### Content

- Control Structures: The Conditional Statement
- If – Else

- if(Boolean expression that returns true or false)
- {
- instructions that will be executed
- if Boolean expression returns true;
- }
- else
- {
- instructions that will be executed
- if Boolean expression did not return true;
- }

If the expression returns “false”, the first block will ignored and this second block of code be executed instead. If the result is “true”, then the first block will be executed and the second block ignored.

---

## 36. Preview: Making Choices {#slide-36-preview-making-choices}

### Content

- Control Structures: The Conditional Statement
- If – Else

- if(money < 12)
- {
- alert("Insufficient funds");
- }
- else
- {
- alert("Thank you!");
- }

---

## 37. Preview: Making Choices {#slide-37-preview-making-choices}

### Content

- Control Structures: The Conditional Statement
- If – Else If – Else

- if(Boolean expression that returns true or false) {
- instructions that will be executed
- if Boolean expression returns true;
- }
- else if(Another Boolean expression that returns true or false) {
- instructions that will be executed
- if the first Boolean expression did not return true;
- }
- else {
- instructions that will be executed
- if neither of the above Boolean expressions returned true;
- }

“else if” is useful if we want to evaluate more than one expression

---

## 38. Preview: Making Choices {#slide-38-preview-making-choices}

### Content

- Control Structures: The Conditional Statement
- If – Else If – Else

- if(money < 12)
- {
- alert("Insufficient funds");
- }
- else if(money > 12)
- {
- alert("That is very generous of you!");
- }
- else
- {
- alert("Thank you!");
- }

---

## 39. Useful operators to use in expressions {#slide-39-useful-operators-to-use-in-expressions}

### Content

Useful operators to use in expressions

Relational operators

Two operands x and y are directly compared

### Visual Analysis

# Relational Operators in Expressions

## Definition

Relational operators are used to compare two operands (x and y) directly in programming expressions.

## Purpose

These operators enable direct comparison between two values or variables, forming the basis for conditional logic and decision-making in programs.

## Key Characteristics

- **Binary operators**: Require exactly two operands to function
- **Direct comparison**: Evaluate the relationship between operand values
- **Boolean result**: Typically return true or false based on the comparison outcome

## Common Applications

- Conditional statements (if/else structures)
- Loop control (while, for loops)
- Data validation
- Sorting and filtering operations
- Logical expression evaluation

---

## 40. Useful operators to use in expressions {#slide-40-useful-operators-to-use-in-expressions}

### Content

Useful operators to use in expressions

Logical operators





Truth tables

NOT

AND

OR

### Visual Analysis

# Logical Operators in Expressions

## Core Logical Operators

There are three fundamental logical operators used in expressions:

### NOT Operator
- Negates or inverts a boolean value
- Unary operator (operates on a single operand)

### AND Operator
- Returns true only when both operands are true
- Binary operator (operates on two operands)

### OR Operator
- Returns true when at least one operand is true
- Binary operator (operates on two operands)

## Truth Tables

Truth tables systematically show all possible input combinations and their resulting outputs for logical operations:

### NOT Truth Table
| Input | Output |
|-------|--------|
| True  | False  |
| False | True   |

### AND Truth Table
| Input A | Input B | Output |
|---------|---------|--------|
| False   | False   | False  |
| False   | True    | False  |
| True    | False   | False  |
| True    | True    | True   |

### OR Truth Table
| Input A | Input B | Output |
|---------|---------|--------|
| False   | False   | False  |
| False   | True    | True   |
| True    | False   | True   |
| True    | True    | True   |

## Application in Information Systems

These logical operators are essential for:
- Constructing conditional statements in programming
- Building database queries with complex filter conditions
- Implementing decision logic in business rules
- Creating search expressions with multiple criteria

---

## 41. Next Lectures {#slide-41-next-lectures}

### Content

- How to group data in arrays
- More control: Loops

- 41

---


---

## Processing Metadata

### Slide Classification
- Text slides: 36
- Visual slides: 5
- Optimized percentage (without API): 87.8%

### API Costs
- Input tokens: 44,779
- Output tokens: 8,945
- Total cost: $0.2685 USD

### System
- Generated by: PPTX to Markdown Converter
- Date: 2026-01-11 19:08:28