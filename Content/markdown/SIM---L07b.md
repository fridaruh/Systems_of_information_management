# SIM   L07b

**Conversion date:** 2026-01-11
**Original file:** `SIM - L07b.pptx`
**Total slides:** 33

---


## Table of Contents

1. [Systems for Information ManagementLecture 7b](#slide-1-systems-for-information-managementlecture-7b)
2. [Previously](#slide-2-previously)
3. [Today](#slide-3-today)
4. [Recap: Relational algebra](#slide-4-recap-relational-algebra)
5. [Recap: SQL basics](#slide-5-recap-sql-basics)
6. [More selection](#slide-6-more-selection)
7. [More selection](#slide-7-more-selection)
8. [Connecting expressions](#slide-8-connecting-expressions)
9. [Value enumerations](#slide-9-value-enumerations)
10. [Value ranges](#slide-10-value-ranges)
11. [Multi-table queries](#slide-11-multi-table-queries)
12. [Multi-table queries](#slide-12-multi-table-queries)
13. [Query customisation](#slide-13-query-customisation)
14. [Query customisation](#slide-14-query-customisation)
15. [Multi-table queries](#slide-15-multi-table-queries)
16. [Multi-table queries](#slide-16-multi-table-queries)
17. [Multi-table queries](#slide-17-multi-table-queries)
18. [Special conditions](#slide-18-special-conditions)
19. [Special conditions](#slide-19-special-conditions)
20. [Special conditions](#slide-20-special-conditions)
21. [Special conditions](#slide-21-special-conditions)
22. [Special conditions](#slide-22-special-conditions)
23. [Recap](#slide-23-recap)
24. [PHP](#slide-24-php)
25. [PHP](#slide-25-php)
26. [PHP](#slide-26-php)
27. [PHP](#slide-27-php)
28. [PHP](#slide-28-php)
29. [PHP](#slide-29-php)
30. [PHP](#slide-30-php)
31. [PHP](#slide-31-php)
32. [Read](#slide-32-read)
33. [Next Lecture](#slide-33-next-lecture)

## 1. Systems for Information ManagementLecture 7b {#slide-1-systems-for-information-managementlecture-7b}

### Content

- Dr Imran U Khan		School of Engineering and Informatics

---

## 2. Previously {#slide-2-previously}

### Content

- SQL & Relational algebra
- Basics of relational algebra
- Basics of SQL for data definition
- Basics of SQL for data manipulation

- 2

---

## 3. Today {#slide-3-today}

### Content

- More SQL, Server-side scripting
- More SQL operations for data manipulation
- More selection: SELECT DISTINCT
- Logical operators
- Disambiguation of attributes from multiple tables
- Use of abbreviations and renaming (AS)
- Ordering (ORDER BY) of results
- JOIN operations
- Special conditions WHERE EXISTS, LIKE, IS NULL
- Server-side scripting revisited & a brief introduction to PHP

- 3

---

## 4. Recap: Relational algebra {#slide-4-recap-relational-algebra}

### Content

Recap: Relational algebra

Relational database systems support different operations on the data in their data tables (which implement properties of relations) that produce relations as a result.
Core relational algebra operations are RESTRICT, PROJECT, and JOIN
Other supported operations include common set operations such as UNION, INTERSECTION, DIFFERENCE, or CARTESIAN PRODUCT.

4

### Visual Analysis

# Relational Algebra Operations

## Overview
Relational database systems perform operations on data tables that implement properties of relations. All operations produce relations as their result.

## Core Relational Algebra Operations

### RESTRICT
Filters rows from a relation based on specified conditions.

### PROJECT
Selects specific columns from a relation.

### JOIN
Combines data from two or more relations based on related columns.

## Additional Set Operations

Relational databases also support common mathematical set operations:

- **UNION** - Combines rows from two relations, eliminating duplicates
- **INTERSECTION** - Returns only rows that appear in both relations
- **DIFFERENCE** - Returns rows that appear in one relation but not in another
- **CARTESIAN PRODUCT** - Returns all possible combinations of rows from two relations

---

## 5. Recap: SQL basics {#slide-5-recap-sql-basics}

### Content

SQL has DDL commands for creating, changing, and deleting schemas and domains
SQL has DML commands that correspond to the fundamental operations on data in a database (CRUD)
- SQL implements relational algebra operations

- Queries that run operations on the data
- Create:	  INSERT INTO
- Read:	  SELECT
- Update:	  UPDATE
- Delete:	  DELETE

- Commands for schema creation & updates:
- Create relation or domain:    CREATE
- Change relation or domain:  ALTER
- Delete relation or domain:     DROP

- SELECT title
- FROM films
- WHERE runtime < 100

- CREATE TABLE films(
- title VARCHAR(60),
- year YEAR,
- runtime INT NOT NULL,
- PRIMARY KEY (title, year)
- )

- 5

---

## 6. More selection {#slide-6-more-selection}

### Content

- SELECT DISTINCT
This will filter out all duplicates of the selected attributes and so, returndistinct values.
- Syntax:

- SELECT DISTINCT attribute1, attribute2
- FROM table

- 6

---

## 7. More selection {#slide-7-more-selection}

### Content

- SELECT DISTINCT
This will filter out all duplicates of the selected attributes and so, returndistinct values.
- Example:

- SELECT DISTINCT composer
- FROM track

- 7

---

## 8. Connecting expressions {#slide-8-connecting-expressions}

### Content

- Logical operators
- SQL supports AND, OR, and NOT
But be wary of the usual caveats of logical expressions.The following query will remove customers from Canada, but not those from the US.

- SELECT FirstName, LastName, Country
- FROM customer
- WHERE country = "Canada" OR country = "USA"

- SELECT FirstName, LastName, Country
- FROM customer
- WHERE NOT country = "Canada" OR country = "USA"

- 8

---

## 9. Value enumerations {#slide-9-value-enumerations}

### Content

- IN operator
The IN operator can be used instead of having to specify several interconnected OR statements
The values in brackets can also be supplied by a sub-query

- SELECT FirstName, LastName, Country
- FROM customer
- WHERE country IN ("Canada","USA","Brazil","Germany")

- SELECT FirstName, LastName, Country
- FROM customer
- WHERE country IN (SELECT country FROM someOtherTable)

- 9

---

## 10. Value ranges {#slide-10-value-ranges}

### Content

- BETWEEN operator
The BETWEEN operator is similar to IN, but can be used to define a range of values, such as the numbers between 1 and 100.
- Example:

- SELECT Name, UnitPrice
- FROM track
- WHERE UnitPrice BETWEEN 0 AND 1.50

- 10

---

## 11. Multi-table queries {#slide-11-multi-table-queries}

### Content

- Naming conventions
Attribute names can be expressed in dot notation (relation.attribute), sois a short form of
Dot notation can be useful to avoid ambiguity when referring to attributes from multiple tables, or if there are multiple queries (later)

- SELECT LastName from customer

- SELECT customer.LastName from customer

- 11

---

## 12. Multi-table queries {#slide-12-multi-table-queries}

### Content

- Disambiguation of attributes from multiple tables
- Example

- SELECT FirstName, LastName, InvoiceDate
- FROM   customer, invoice
- WHERE  customer.CustomerId = invoice.CustomerId

- 12

---

## 13. Query customisation {#slide-13-query-customisation}

### Content

- Ordering of results
The ORDER BY keyword can be added at the end of a SELECT query,and qualified with the ASC or DESC keywords
- Example:

- SELECT something FROM someTable WHERE condition
- ORDER BY attribute1 [, attribute2] [ASC|DESC]

- SELECT FirstName, LastName, InvoiceDate
- FROM   customer, invoice
- WHERE  customer.CustomerId = invoice.CustomerId
- ORDER BY InvoiceDate DESC

- 13

---

## 14. Query customisation {#slide-14-query-customisation}

### Content

- Use of aliases for tables and attributes/results
We can use the AS keyword to create aliases for tables
- We can also rename (and even concatenate) attributes

- SELECT FirstName, LastName, InvoiceDate
- FROM   customer AS c, invoice AS i
- WHERE  c.CustomerId = i.CustomerId

- SELECT CONCAT(FirstName, " ", LastName) AS Name, InvoiceDate
- FROM   customer AS c, invoice AS i
- WHERE  c.CustomerId = i.CustomerId

- 14

---

## 15. Multi-table queries {#slide-15-multi-table-queries}

### Content

- JOIN operations
The JOIN operation combines attributes from several tables, and connects the tuplesbased on shared attributes (using the ON keyword).
- General syntax:

- SELECT something FROM someTable
- INNER|LEFT|RIGHT JOIN anotherTable
- ON someTable.attribute = anotherTable.attribute

- 15

---

## 16. Multi-table queries {#slide-16-multi-table-queries}

### Content

- INNER JOIN
The INNER JOIN keyword will select only those tuples where the connecting attribute value appears in both relations:
- Example:

- SELECT total FROM invoice
- INNER JOIN customer
- ON customer.CustomerId = invoice.CustomerId

- 16

---

## 17. Multi-table queries {#slide-17-multi-table-queries}

### Content

- JOINS LEFT AND RIGHT
In addition to INNER JOIN, MySQL also supports left and right joins of tables. Other implementations of SQL will also do FULL JOINs (the Cartesian Product of two tables).
A LEFT JOIN will return all tuples on the left and those with a matching attribute on the right.
A RIGHT JOIN will return all tuples on the right and those with a matching attribute on the left

- 17

---

## 18. Special conditions {#slide-18-special-conditions}

### Content

- WHERE EXISTS
This allows attaching a sub-query to a WHERE clause, which will return TRUE for every record obtained by the subquery.
- Syntax:

- SELECT attribute
- FROM table
- WHERE EXISTS (SELECT something FROM someTable WHERE condition)

- 18

---

## 19. Special conditions {#slide-19-special-conditions}

### Content

- WHERE EXISTS
This allows attaching a sub-query to a WHERE clause, which will return TRUE for every record obtained by the subquery.
- Example:

- SELECT total FROM invoice WHERE EXISTS
- (SELECT CustomerId FROM customer WHERE 						customer.CustomerId = invoice.CustomerId
- AND customer.Company IS NOT NULL)

- 19

---

## 20. Special conditions {#slide-20-special-conditions}

### Content

- Searching for patterns
The LIKE operator allows specifying a pattern rather than a specific value in a WHERE clause
- Special symbols for the pattern:
- % is a multi-character placeholder
- _ is a single-character placeholder

- SELECT attribute
- FROM table
- WHERE someAttribute LIKE pattern

- 20

---

## 21. Special conditions {#slide-21-special-conditions}

### Content

- Searching for patterns
The LIKE operator allows specifying a pattern rather than a specific value in a WHERE clause
- Special symbols for the pattern:
- % is a multi-character placeholder
- _ is a single-character placeholder

- SELECT name
- FROM track
- WHERE name LIKE 'L%'

- SELECT name
- FROM track
- WHERE name LIKE '%Love%'

- SELECT name
- FROM track
- WHERE name LIKE '%Lo__%'

- 21

---

## 22. Special conditions {#slide-22-special-conditions}

### Content

- Looking for unspecified values
The IS NULL condition will yield results where the value of the attribute isNULL.
A common query  combines this with the logical NOT operator to expressIS NOT NULL, when looking for records that have a value for the attribute specified.

- SELECT *
- FROM customer WHERE State IS NOT NULL

- 22

---

## 23. Recap {#slide-23-recap}

### Content

Recap

Server-side scripting

Scripts can be used to interact with and manipulate the HTML before it is being sent to the client.
Here, the server could run a script to process the HTTP request and assemble an HTML page that contains the correct information to be sent back to the client:(e.g., the requested information, an error message, an authentication request, …)

23

SCRIPT

Server

Client

HTML

### Visual Analysis

# Server-Side Scripting

## Core Concept

Server-side scripting involves executing scripts on the web server to interact with and manipulate HTML before sending it to the client's browser.

## How It Works

The server processes HTTP requests by:
1. Running scripts to handle the incoming request
2. Assembling an HTML page dynamically based on the request
3. Sending the generated HTML back to the client

## Processing Flow

**Client → Server:** HTTP request is sent

**Server processing:** Scripts execute to:
- Process the request
- Generate appropriate content
- Prepare HTML response

**Server → Client:** Complete HTML page is sent

## Use Cases

Server-side scripts can generate pages containing:
- Requested information from databases or files
- Error messages when requests fail or are invalid
- Authentication requests for protected resources
- Dynamically generated content based on user input or session data

## Key Characteristic

All script execution and HTML assembly occurs on the server before transmission, meaning the client receives only the final HTML output, not the script code itself.

---

## 24. PHP {#slide-24-php}

### Content

- Overview
- PHP is a popular server-side scripting language
PHP can be used to create interactive web applications that use databases
- PHP files have the index *.php
PHP is a higher-level language and interpreted at runtime, like Javascript
PHP documents can contain a mix of HTML and code but unlike Javascript, PHP programs will only run when placed on a web server (like the Apache webserver installed on your computers, which has a PHP interpreter module)

- 24

---

## 25. PHP {#slide-25-php}

### Content

- Basic syntax

- 25

- <?php
- // everything in here is PHP code
- echo "Hello World!";
- ?>

- Opening and closingtag for PHP

"echo" is a useful command for generating text outputs on the page

---

## 26. PHP {#slide-26-php}

### Content

- Embedded PHP
Example PHP documentthat has HTML markupand embedded PHP code

- 26

- <!DOCTYPE html>
- <html>
- <body>
- <h1>Welcome</h1> <?php
- // everything in here is PHP code
- echo "<p>Hello World!</p>";
- ?>
- </body>
- </html>

---

## 27. PHP {#slide-27-php}

### Content

- Variables and data types
- Variables in PHP are prefixed with a $ symbol
Variables are dynamically typed (same as in Javascript).

- 27

- <?php
- // everything in here is PHP code
- $output = "Hello World!";
- echo $output;
- ?>

- $output contains a string here

---

## 28. PHP {#slide-28-php}

### Content

- Variables and data types
We can concatenate strings and variable values using the dot (.) operator.(unlike Javascript, where we would use +)
However, due to the $ prefix for variables, the following will also work:

- 28

- <?php
- // everything in here is PHP code
- $output = "Hello World!";
- echo "This is my ".$output. " program.";
- ?>

- echo "This is my $output program.";

---

## 29. PHP {#slide-29-php}

### Content

- Conditional statements and loops
These work more or less exactly like those you already know from Javascript
- Example:

- 29

- <?php
- for ($i = 0; $i < 5; $i++) {
- echo "This is turn: $i <br>";
- }
- ?>

---

## 30. PHP {#slide-30-php}

### Content

- Functions
- Functions in PHP are declared with the function keyword

- 30

- <?php
- function write($text) {
- echo $text;
- }
- $output = "Hello World!";
- write($output);
- ?>

---

## 31. PHP {#slide-31-php}

### Content

- Variable scope
- Variables declared inside functions have local scope
- Variables declared outside functions have global scope
But the scoping is stricter than what we have seen in Javascript:
Global variables cannot be accessed within functionsIf you need a variable value in a function, it needs to be passed as a parameter

- 31

---

## 32. Read {#slide-32-read}

### Content

Connolly and Begg, Database Systems: A Practical Approach to Design, Implementation, and Management, Pearson Ed.
- Chapter 6: SQL data manipulation

- 32

---

## 33. Next Lecture {#slide-33-next-lecture}

### Content

- A few more SQL tricks
- Building web applications with PHP

- 33

---


---

## Processing Metadata

### Slide Classification
- Text slides: 31
- Visual slides: 2
- Optimized percentage (without API): 93.9%

### API Costs
- Input tokens: 66,863
- Output tokens: 14,594
- Total cost: $0.4195 USD

### System
- Generated by: PPTX to Markdown Converter
- Date: 2026-01-11 19:11:09