# SIM   L03b

**Conversion date:** 2026-01-11
**Original file:** `SIM - L03b.pptx`
**Total slides:** 39

---


## Table of Contents

1. [Systems for Information ManagementLecture 3b](#slide-1-systems-for-information-managementlecture-3b)
2. [Previously](#slide-2-previously)
3. [Previously](#slide-3-previously)
4. [Today](#slide-4-today)
5. [More data types: Arrays](#slide-5-more-data-types-arrays)
6. [More data types: Arrays](#slide-6-more-data-types-arrays)
7. [More data types: Arrays](#slide-7-more-data-types-arrays)
8. [More data types: Arrays](#slide-8-more-data-types-arrays)
9. [More data types: Arrays](#slide-9-more-data-types-arrays)
10. [More data types: Arrays](#slide-10-more-data-types-arrays)
11. [More data types: Arrays](#slide-11-more-data-types-arrays)
12. [More data types: Arrays](#slide-12-more-data-types-arrays)
13. [More data types: Arrays](#slide-13-more-data-types-arrays)
14. [The Grouping of Data](#slide-14-the-grouping-of-data)
15. [The Grouping of Data](#slide-15-the-grouping-of-data)
16. [More Control](#slide-16-more-control)
17. [Loops](#slide-17-loops)
18. [Loops](#slide-18-loops)
19. [var i = 0;
var k = 2;
while( i < k )
{
    alert("Turn " + i); 
    i++;
}](#slide-19-var-i--0var-k--2while-i--k-----alertturn---i-----i)
20. [var i = 0;
var k = 2;
while( i < k )
{
    alert("Turn " + i); 
    i++;
}](#slide-20-var-i--0var-k--2while-i--k-----alertturn---i-----i)
21. [var i = 0;
var k = 2;
while( i < k )
{
    alert("Turn " + i); 
    i++;
}](#slide-21-var-i--0var-k--2while-i--k-----alertturn---i-----i)
22. [var i = 0;
var k = 2;
while( i < k )
{
    alert("Turn " + i); 
    i++;
}](#slide-22-var-i--0var-k--2while-i--k-----alertturn---i-----i)
23. [var i = 0;
var k = 2;
while( i < k )
{
    alert("Turn " + i); 
    i++;
}](#slide-23-var-i--0var-k--2while-i--k-----alertturn---i-----i)
24. [var i = 200;

do {
    i = prompt("Enter a number above 100!");
}
while( i <= 100);](#slide-24-var-i--200do-----i--promptenter-a-number-above-100while-i--100)
25. [Loops](#slide-25-loops)
26. [Loops](#slide-26-loops)
27. [var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
}](#slide-27-var-index-k2forindex0-index--k-index--index--1----alertturn--index)
28. [var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
}](#slide-28-var-index-k2forindex0-index--k-index--index--1----alertturn--index)
29. [var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
}](#slide-29-var-index-k2forindex0-index--k-index--index--1----alertturn--index)
30. [var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
}](#slide-30-var-index-k2forindex0-index--k-index--index--1----alertturn--index)
31. [var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
}](#slide-31-var-index-k2forindex0-index--k-index--index--1----alertturn--index)
32. [var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
}](#slide-32-var-index-k2forindex0-index--k-index--index--1----alertturn--index)
33. [var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
}](#slide-33-var-index-k2forindex0-index--k-index--index--1----alertturn--index)
34. [var i, k=2;

for(i=0; i < k; i++)
{
    alert("Turn ", i);
}](#slide-34-var-i-k2fori0-i--k-i----alertturn--i)
35. [Practice time](#slide-35-practice-time)
36. [More control within loops](#slide-36-more-control-within-loops)
37. [Useful: Escape sequences in strings](#slide-37-useful-escape-sequences-in-strings)
38. [Useful: Escape sequences in strings](#slide-38-useful-escape-sequences-in-strings)
39. [Next Lectures](#slide-39-next-lectures)

## 1. Systems for Information ManagementLecture 3b {#slide-1-systems-for-information-managementlecture-3b}

### Content

- Dr Imran U Khan		School of Engineering and Informatics

---

## 2. Previously {#slide-2-previously}

### Content

- Client-side scripting / Basic programming concepts
- Markup vs Programs
- Algorithms
- Server- vs client-side scripting
- Introduction to Javascript, and a few handy basics
- Basic syntax and conventions
- Variables & basic control structures

- 2

---

## 3. Previously {#slide-3-previously}

### Content

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

## 4. Today {#slide-4-today}

### Content

- More basic programming concepts
- Arrays
- Grouping of data
- Loops

- 4

---

## 5. More data types: Arrays {#slide-5-more-data-types-arrays}

### Content

What is an array?
An array is a grouping of data.
- Arrays can have multiple dimensions

- 1-dimensional array

- 2-dimensional array

---

## 6. More data types: Arrays {#slide-6-more-data-types-arrays}

### Content

How do arrays work?
- An array can store multiple elements
- Elements can be addressed using an index number

- 0

- 1

- 2

- 3

- Maximum index = size - 1

- size = 4

---

## 7. More data types: Arrays {#slide-7-more-data-types-arrays}

### Content

- Syntax
- Declarationor

- var identifier = [];

- var identifier = new Array();

- Use square brackets here

- In the object notation, use normal brackets

---

## 8. More data types: Arrays {#slide-8-more-data-types-arrays}

### Content

- Syntax
- Declarationor
- Declaration & instant initialisation
- or

- 4

- 12

- 3

- Tom

- 0

- 1

- 2

- 3

- var numbers = [4,12,3,"Tom"];

- data

- index

- var identifier = new Array();

- var numbers = new Array(4,12,3,"Tom");

In Javascript, one can store different data types in a single array (unlike in other PLs)However, it can be useful for data processing to keep the datatypes uniform.

- var identifier = [];

---

## 9. More data types: Arrays {#slide-9-more-data-types-arrays}

### Content

- Example: How to create an empty array

- 0

- 1

- 2

- 3        …

- var numbers = [];

---

## 10. More data types: Arrays {#slide-10-more-data-types-arrays}

### Content

- 10

- 45

- 0

- 1

- numbers[0] = 10;
- numbers[1] = 45;

- Example: How to assign single values to an array

---

## 11. More data types: Arrays {#slide-11-more-data-types-arrays}

### Content

- Example: How to access a single element in an array

- 10

- 45

- 0

- 1

- var elem1 = numbers[0];

- The value of this variable is 10

---

## 12. More data types: Arrays {#slide-12-more-data-types-arrays}

### Content

Example: How to access & remove the last element of an array

- 10

- 45

- 0

- 1

- var elem2 = numbers.pop();

- The value of this variable is 45

---

## 13. More data types: Arrays {#slide-13-more-data-types-arrays}

### Content

Example: How to add another element at the end of an array

- 10

- 88

- 0

- 1

- numbers.push(88);

---

## 14. The Grouping of Data {#slide-14-the-grouping-of-data}

### Content

The Grouping of Data

Why would we want to group data?

	There are many applications
Library catalogue
Online shopping basket
Phone number directory
Address book / Diary

### Visual Analysis

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

## 15. The Grouping of Data {#slide-15-the-grouping-of-data}

### Content

The Grouping of Data

What can we do with grouped data?

Common operations 
Adding an item to a group
Retrieving a specific item (read data)
Modifying a single data item or all items in a group
Removing a data item / all items from a group

### Visual Analysis

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

## 16. More Control {#slide-16-more-control}

### Content

- Loops
In programming, we often need to perform an action multiple times
- Most programming languages include loop statements to make this possible
- Basically, there two kinds of loops:
while loop (the do-while loop is a variant worthwhile knowing about)
for loop ( for-in / for-of loop are special variants that we won’t need to look at)

---

## 17. Loops {#slide-17-loops}

### Content

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

## 18. Loops {#slide-18-loops}

### Content

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

- 1

---

## 19. var i = 0;
var k = 2;
while( i < k )
{
    alert("Turn " + i); 
    i++;
} {#slide-19-var-i--0var-k--2while-i--k-----alertturn---i-----i}

### Content

- Loops

- While loop
- No explicit control variable, only a condition
- Performance depends on the condition
Danger of infinite loops if condition never yields false!

- i = 0

- true

- 1

- 2

- k = 2

---

## 20. var i = 0;
var k = 2;
while( i < k )
{
    alert("Turn " + i); 
    i++;
} {#slide-20-var-i--0var-k--2while-i--k-----alertturn---i-----i}

### Content

- Loops

- While loop
- No explicit control variable, only a condition
- Performance depends on the condition
Danger of infinite loops if condition never yields false!

- i = 1

- 1

- 3

- 4

- 2

- k = 2

---

## 21. var i = 0;
var k = 2;
while( i < k )
{
    alert("Turn " + i); 
    i++;
} {#slide-21-var-i--0var-k--2while-i--k-----alertturn---i-----i}

### Content

- i = 1

- 1

- 3

- 4

- 2

- Loops

- While loop
- No explicit control variable, only a condition
- Performance depends on the condition
Danger of infinite loops if condition never yields false!

- true

- 5

- k = 2

---

## 22. var i = 0;
var k = 2;
while( i < k )
{
    alert("Turn " + i); 
    i++;
} {#slide-22-var-i--0var-k--2while-i--k-----alertturn---i-----i}

### Content

- i = 2

- 1

- 3

- 4

- 2

- 5

- Loops

- While loop
- No explicit control variable, only a condition
- Performance depends on the condition
Danger of infinite loops if condition never yields false!

- 6

- 7

- k = 2

---

## 23. var i = 0;
var k = 2;
while( i < k )
{
    alert("Turn " + i); 
    i++;
} {#slide-23-var-i--0var-k--2while-i--k-----alertturn---i-----i}

### Content

- i = 2

- 1

- 3

- 4

- 2

- 5

- 6

- 7

- Loops

- While loop
- No explicit control variable, only a condition
- Performance depends on the condition
Danger of infinite loops if condition never yields false!

- false

- 8

- k = 2

- exit loop

---

## 24. var i = 200;

do {
    i = prompt("Enter a number above 100!");
}
while( i <= 100); {#slide-24-var-i--200do-----i--promptenter-a-number-above-100while-i--100}

### Content

- Loops

- Do-While loop
Similar to while-loop with the difference that the loop body is executedonce before the condition is checked

Semicolon here!

---

## 25. Loops {#slide-25-loops}

### Content

- For loop
Initialises a control variable; matches it against a condition; modifies the control variable after each loop iteration
Performance depends on the value of the control variable / condition

- for(initialisation; condition; post-loop action)
- {
- // instructions to be repeated
- }

---

## 26. Loops {#slide-26-loops}

### Content

- For loop
Initialises a control variable; matches it against a condition; modifies the control variable after each loop
Performance depends on the value of the control variable / condition

- var index, k=2;
- for(index=0; index < k; index = index + 1)
- {
- alert("Turn ", index);
- }

- 1

- k = 2

- index = 0

---

## 27. var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
} {#slide-27-var-index-k2forindex0-index--k-index--index--1----alertturn--index}

### Content

- 1

- Loops

- For loop
Initialises a control variable; matches it against a condition; modifies the control variable after each loop
Performance depends on the value of the control variable / condition

- 2

- true

- k = 2

- index = 0

---

## 28. var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
} {#slide-28-var-index-k2forindex0-index--k-index--index--1----alertturn--index}

### Content

- 1

- 2

- Loops

- For loop
Initialises a control variable; matches it against a condition; modifies the control variable after each loop
Performance depends on the value of the control variable / condition

- k = 2

- index = 0

- 3

---

## 29. var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
} {#slide-29-var-index-k2forindex0-index--k-index--index--1----alertturn--index}

### Content

- 1

- 2

- Loops

- For loop
Initialises a control variable; matches it against a condition; modifies the control variable after each loop
Performance depends on the value of the control variable / condition

- 4

- index = 1

- k = 2

- 3

---

## 30. var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
} {#slide-30-var-index-k2forindex0-index--k-index--index--1----alertturn--index}

### Content

- 1

- 2

- 4

- Loops

- For loop
Initialises a control variable; matches it against a condition; modifies the control variable after each loop
Performance depends on the value of the control variable / condition

- 5

- k = 2

- index = 1

- true

- 3

---

## 31. var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
} {#slide-31-var-index-k2forindex0-index--k-index--index--1----alertturn--index}

### Content

- 1

- 2

- 4

- 5

- k = 2

- Loops

- For loop
Initialises a control variable; matches it against a condition; modifies the control variable after each loop
Performance depends on the value of the control variable / condition

- index = 1

- 3

- 6

---

## 32. var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
} {#slide-32-var-index-k2forindex0-index--k-index--index--1----alertturn--index}

### Content

- 1

- 2

- 3

- 4

- 5

- k = 2

- 6

- Loops

- For loop
Initialises a control variable; matches it against a condition; modifies the control variable after each loop
Performance depends on the value of the control variable / condition

- 7

- index = 2

---

## 33. var index, k=2;

for(index=0; index < k; index = index + 1)
{
    alert("Turn ", index);
} {#slide-33-var-index-k2forindex0-index--k-index--index--1----alertturn--index}

### Content

- 1

- 2

- 4

- 5

- k = 2

- 7

- Loops

- For loop
Initialises a control variable; matches it against a condition; modifies the control variable after each loop
Performance depends on the value of the control variable / condition

- 8

- false

- index = 2

- 3

- 6

- exit loop

---

## 34. var i, k=2;

for(i=0; i < k; i++)
{
    alert("Turn ", i);
} {#slide-34-var-i-k2fori0-i--k-i----alertturn--i}

### Content

- Loops

- For loop
Initialises a control variable; matches it against a condition; modifies the control variable after each loop
Performance depends on the value of the control variable / condition

- Shorter, equivalent code

---

## 35. Practice time {#slide-35-practice-time}

### Content

- Create a program that can add five integers
- Create an array of integers to store five numbers in
Use a loop of your choice to ask the user to enter five successive integers and store these in the array – to find out how, look up how the prompt() method of the window object works in a Javascript reference documentation
Use another kind of loop to iterate over and add all numbers stored in the array
Print out on screen the sum of all numbers.
- Extension
Make the program "talk" a bit more about what it is doing:E.g., output details about calculation steps and intermediate results.

---

## 36. More control within loops {#slide-36-more-control-within-loops}

### Content

- break & continue
break will stop the loop, no matter how many iterations would normally be left to do, and execution will continue with the next instruction after the loop.
continue only skips the current turn and will trigger another evaluation of the condition. In a for-loop, the post-loop action (usually incrementing the control variable) will be run before another evaluation is made.
Experiment with break and continue in your number-adding program.

---

## 37. Useful: Escape sequences in strings {#slide-37-useful-escape-sequences-in-strings}

### Content

What are escape sequences?
- Special characters inserted within a string
- Get translated into special symbols or functionality
Start with the back-slash symbol ( \ ), followed by the escape symbole.g. \n creates a new line, as in
Any other, ordinary characters around an escape sequence will be displayed as usual – including “ ” (space) characters!

- alert("Hello\nWorld!");

---

## 38. Useful: Escape sequences in strings {#slide-38-useful-escape-sequences-in-strings}

### Content

Useful: Escape sequences in strings

Common escape sequences

### Visual Analysis

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

## 39. Next Lectures {#slide-39-next-lectures}

### Content

- Better code organisation with functions
- Event handlers

- 39

---


---

## Processing Metadata

### Slide Classification
- Text slides: 36
- Visual slides: 3
- Optimized percentage (without API): 92.3%

### API Costs
- Input tokens: 69,841
- Output tokens: 15,305
- Total cost: $0.4391 USD

### System
- Generated by: PPTX to Markdown Converter
- Date: 2026-01-11 19:11:29