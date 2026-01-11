# SIM   L03b


## Systems for Information ManagementLecture 3b


- Dr Imran U Khan		School of Engineering and Informatics

---

## Previously


- Client-side scripting / Basic programming concepts
- Markup vs Programs
- Algorithms
- Server- vs client-side scripting
- Introduction to Javascript, and a few handy basics
- Basic syntax and conventions
- Variables & basic control structures

---

## Previously


- Making decisions
- Making choices: Conditional statements
- If-else / else-if
- Operators in expressions
- Relational operators
- Logical operators

- instruction1

?

- instruction2

- instruction3

- Yes

- No

- if(money < 12)
- {
- alert(“Insufficient funds”);
- }
- else
- {
- alert(“Thank you!”);
- }

---

## Today


- More basic programming concepts
- Arrays
- Grouping of data
- Loops

---

## More data types: Arrays


What is an array?
An array is a grouping of data.
- Arrays can have multiple dimensions

- 1-dimensional array

- 2-dimensional array

---

## More data types: Arrays


How do arrays work?
- An array can store multiple elements
- Elements can be addressed using an index number

- 1

- 3

- Maximum index = size - 1

- size = 4

---

## More data types: Arrays


- Syntax
- Declarationor

- var identifier = [];

- var identifier = new Array();

- Use square brackets here

- In the object notation, use normal brackets

---

## More data types: Arrays


- Syntax
- Declarationor
- Declaration & instant initialisation
- or

- 12

- Tom

- 1

- 3

- var numbers = [4,12,3,"Tom"];

- data

- index

- var identifier = new Array();

- var numbers = new Array(4,12,3,"Tom");

In Javascript, one can store different data types in a single array (unlike in other PLs)However, it can be useful for data processing to keep the datatypes uniform.

- var identifier = [];

---

## More data types: Arrays


- Example: How to create an empty array

- 1

- 3        …

- var numbers = [];

---

## More data types: Arrays


- 45

- 1

- numbers[0] = 10;
- numbers[1] = 45;

- Example: How to assign single values to an array

---

## More data types: Arrays


- Example: How to access a single element in an array

- 45

- 1

- var elem1 = numbers[0];

- The value of this variable is 10

---

## More data types: Arrays


Example: How to access & remove the last element of an array

- 45

- 1

- var elem2 = numbers.pop();

- The value of this variable is 45

---

## More data types: Arrays


Example: How to add another element at the end of an array

- 88

- 1

- numbers.push(88);

---

## The Grouping of Data


The Grouping of Data

Why would we want to group data?

	There are many applications
Library catalogue
Online shopping basket
Phone number directory
Address book / Diary


# Data Grouping

## Core Concept

Data grouping refers to the organization and collection of related data items into structured units or containers.

## Purpose of Data Grouping

Data grouping serves essential organizational purposes in information systems by allowing related information to be stored, accessed, and managed together as logical units.

## Real-World Applications

### Library Catalogue
Groups related bibliographic information including:
- Book titles
- Authors
- ISBN numbers
- Publication dates
- Available copies
- Location information

### Online Shopping Basket
Collects and maintains:
- Selected products
- Quantities
- Prices
- Product specifications
- Total cost calculations

### Phone Number Directory
Organizes contact information:
- Names
- Phone numbers
- Contact categories
- Associated details

### Address Book / Diary
Combines multiple types of personal information:
- Contact details
- Addresses
- Appointments
- Dates and times
- Notes and reminders

## Benefits

- Enables logical organization of related data elements
- Facilitates efficient data retrieval and manipulation
- Supports complex data structures in applications
- Improves data management and maintenance

---

## The Grouping of Data


The Grouping of Data

What can we do with grouped data?

Common operations
Adding an item to a group
Retrieving a specific item (read data)
Modifying a single data item or all items in a group
Removing a data item / all items from a group


# Grouping of Data

## Common Operations on Grouped Data

When working with grouped data structures, there are four fundamental operations that can be performed:

### 1. Adding an Item to a Group
- Inserting new data elements into an existing group or collection
- Expands the size of the data structure

### 2. Retrieving a Specific Item (Read Data)
- Accessing and reading data from the group
- Does not modify the data structure
- Allows inspection of individual elements within the collection

### 3. Modifying Data Items
- **Single item modification**: Updating one specific data element within the group
- **Bulk modification**: Changing all items in the group simultaneously
- Alters the content while maintaining the structure

### 4. Removing Data Items
- **Single item removal**: Deleting one specific element from the group
- **Complete removal**: Clearing all items from the group
- Reduces the size of the data structure or empties it entirely

These operations form the basis for manipulating collections, arrays, lists, and other data grouping structures in information systems.

---

## More Control


- Loops
In programming, we often need to perform an action multiple times
- Most programming languages include loop statements to make this possible
- Basically, there two kinds of loops:
while loop (the do-while loop is a variant worthwhile knowing about)
for loop ( for-in / for-of loop are special variants that we won’t need to look at)

---

## Loops


- While loop
- No explicit control variable, only a condition
- Performance depends on the condition
Danger of infinite loops if condition never yields false!

- while(condition)
- {
- // instructions to be repeated
// important: include an instruction that affects the condition!
- }

---

## Loops


- While loop
- No explicit control variable, only a condition
- Performance depends on the condition
Danger of infinite loops if condition never yields false!

- var i = 0;
- var k = 2;
- while( i < k )
- {
- alert("Turn " + i);
- i++;
- }

- k = 2

- i = 0

---

## var i = 0;
var k = 2;
while( i < k )
{
    alert("Turn " + i);
    i++;
}


- Loops

- While loop
- No explicit control variable, only a condition
- Performance depends on the condition
Danger of infinite loops if condition never yields false!

- i = 0

- true

- 2

- k = 2

---

## var i = 0;
var k = 2;
while( i < k )
{
    alert("Turn " + i);
    i++;
}


- Loops

- While loop
- No explicit control variable, only a condition
- Performance depends on the condition
Danger of infinite loops if condition never yields false!

- i = 1

- 3

- 2

- k = 2

---

## var i = 0;
var k = 2;
while( i < k )
{
    alert("Turn " + i);
    i++;
}


- i = 1

- 3

- 2

- Loops

- While loop
- No explicit control variable, only a condition
- Performance depends on the condition
Danger of infinite loops if condition never yields false!

- true

- k = 2

---

## var i = 0;
var k = 2;
while( i < k )
{
    alert("Turn " + i);
    i++;
}


- i = 2

- 3

- 2

- Loops

- While loop
- No explicit control variable, only a condition
- Performance depends on the condition
Danger of infinite loops if condition never yields false!

- 7

- k = 2

---

## var i = 0;
var k = 2;
while( i < k )
{
    alert("Turn " + i);
    i++;
}


- i = 2

- 3

- 2

- 6

- Loops

- While loop
- No explicit control variable, only a condition
- Performance depends on the condition
Danger of infinite loops if condition never yields false!

- false

- k = 2

- exit loop

---

## var i = 200;

do {
    i = prompt("Enter a number above 100!");
}
while( i <= 100);


- Loops

- Do-While loop
Similar to while-loop with the difference that the loop body is executedonce before the condition is checked

Semicolon here!

---

## Loops


- For loop
Initialises a control variable; matches it against a condition; modifies the control variable after each loop iteration
Performance depends on the value of the control variable / condition

- for(initialisation; condition; post-loop action)
- {
- // instructions to be repeated
- }

---

## Loops


- For loop
Initialises a control variable; matches it against a condition; modifies the control variable after each loop
Performance depends on the value of the control variable / condition

- var index, k=2;
- for(index=0; index < k; index = index + 1)
- {
- alert("Turn ", index);
- }

- k = 2

- index = 0

---

## var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
}


- Loops

- For loop
Initialises a control variable; matches it against a condition; modifies the control variable after each loop
Performance depends on the value of the control variable / condition

- true

- k = 2

- index = 0

---

## var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
}


- 2

- Loops

- For loop
Initialises a control variable; matches it against a condition; modifies the control variable after each loop
Performance depends on the value of the control variable / condition

- k = 2

- index = 0

---

## var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
}


- 2

- Loops

- For loop
Initialises a control variable; matches it against a condition; modifies the control variable after each loop
Performance depends on the value of the control variable / condition

- index = 1

- k = 2

---

## var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
}


- 2

- Loops

- For loop
Initialises a control variable; matches it against a condition; modifies the control variable after each loop
Performance depends on the value of the control variable / condition

- k = 2

- index = 1

- true

---

## var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
}


- 2

- 5

- k = 2

- Loops

- For loop
Initialises a control variable; matches it against a condition; modifies the control variable after each loop
Performance depends on the value of the control variable / condition

- index = 1

- 6

---

## var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
}


- 2

- 4

- k = 2

- Loops

- For loop
Initialises a control variable; matches it against a condition; modifies the control variable after each loop
Performance depends on the value of the control variable / condition

- index = 2

---

## var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
}


- 2

- 5

- k = 2

- Loops

- For loop
Initialises a control variable; matches it against a condition; modifies the control variable after each loop
Performance depends on the value of the control variable / condition

- false

- index = 2

- 6

- exit loop

---

## var i, k=2;

for(i=0; i < k; i++)
{
    alert("Turn ", i);
}


- Loops

- For loop
Initialises a control variable; matches it against a condition; modifies the control variable after each loop
Performance depends on the value of the control variable / condition

- Shorter, equivalent code

---

## Practice time


- Create a program that can add five integers
- Create an array of integers to store five numbers in
Use a loop of your choice to ask the user to enter five successive integers and store these in the array – to find out how, look up how the prompt() method of the window object works in a Javascript reference documentation
Use another kind of loop to iterate over and add all numbers stored in the array
Print out on screen the sum of all numbers.
- Extension
Make the program "talk" a bit more about what it is doing:E.g., output details about calculation steps and intermediate results.

---

## More control within loops


- break & continue
break will stop the loop, no matter how many iterations would normally be left to do, and execution will continue with the next instruction after the loop.
continue only skips the current turn and will trigger another evaluation of the condition. In a for-loop, the post-loop action (usually incrementing the control variable) will be run before another evaluation is made.
Experiment with break and continue in your number-adding program.

---

## Useful: Escape sequences in strings


What are escape sequences?
- Special characters inserted within a string
- Get translated into special symbols or functionality
Start with the back-slash symbol ( \ ), followed by the escape symbole.g. \n creates a new line, as in
Any other, ordinary characters around an escape sequence will be displayed as usual – including “ ” (space) characters!

- alert("Hello\nWorld!");

---

## Useful: Escape sequences in strings


Useful: Escape sequences in strings

Common escape sequences


# Escape Sequences in Strings

## Common Escape Sequences

Escape sequences are special character combinations used in strings to represent characters that cannot be typed directly or have special meaning in code.

### Standard Escape Sequences

| Escape Sequence | Meaning |
|----------------|---------|
| `\n` | Newline (line break) |
| `\t` | Tab (horizontal tab) |
| `\\` | Backslash character |
| `\'` | Single quote |
| `\"` | Double quote |
| `\r` | Carriage return |
| `\b` | Backspace |
| `\f` | Form feed |

## Purpose and Usage

Escape sequences allow you to:
- Include special characters within string literals
- Format text output with proper spacing and line breaks
- Represent characters that would otherwise conflict with string syntax
- Control text display and formatting in programs

---

## Next Lectures


- Better code organisation with functions
- Event handlers

---
