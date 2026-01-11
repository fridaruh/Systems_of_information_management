# SIM   L07b


## Systems for Information ManagementLecture 7b


- Dr Imran U Khan		School of Engineering and Informatics

---

## Previously


- SQL & Relational algebra
- Basics of relational algebra
- Basics of SQL for data definition
- Basics of SQL for data manipulation

---

## Today


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

---

## Recap: Relational algebra


Recap: Relational algebra

Relational database systems support different operations on the data in their data tables (which implement properties of relations) that produce relations as a result.
Core relational algebra operations are RESTRICT, PROJECT, and JOIN
Other supported operations include common set operations such as UNION, INTERSECTION, DIFFERENCE, or CARTESIAN PRODUCT.



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

## Recap: SQL basics


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

---

## More selection


- SELECT DISTINCT
This will filter out all duplicates of the selected attributes and so, returndistinct values.
- Syntax:

- SELECT DISTINCT attribute1, attribute2
- FROM table

---

## More selection


- SELECT DISTINCT
This will filter out all duplicates of the selected attributes and so, returndistinct values.
- Example:

- SELECT DISTINCT composer
- FROM track

---

## Connecting expressions


- Logical operators
- SQL supports AND, OR, and NOT
But be wary of the usual caveats of logical expressions.The following query will remove customers from Canada, but not those from the US.

- SELECT FirstName, LastName, Country
- FROM customer
- WHERE country = "Canada" OR country = "USA"

- SELECT FirstName, LastName, Country
- FROM customer
- WHERE NOT country = "Canada" OR country = "USA"

---

## Value enumerations


- IN operator
The IN operator can be used instead of having to specify several interconnected OR statements
The values in brackets can also be supplied by a sub-query

- SELECT FirstName, LastName, Country
- FROM customer
- WHERE country IN ("Canada","USA","Brazil","Germany")

- SELECT FirstName, LastName, Country
- FROM customer
- WHERE country IN (SELECT country FROM someOtherTable)

---

## Value ranges


- BETWEEN operator
The BETWEEN operator is similar to IN, but can be used to define a range of values, such as the numbers between 1 and 100.
- Example:

- SELECT Name, UnitPrice
- FROM track
- WHERE UnitPrice BETWEEN 0 AND 1.50

---

## Multi-table queries


- Naming conventions
Attribute names can be expressed in dot notation (relation.attribute), sois a short form of
Dot notation can be useful to avoid ambiguity when referring to attributes from multiple tables, or if there are multiple queries (later)

- SELECT LastName from customer

- SELECT customer.LastName from customer

---

## Multi-table queries


- Disambiguation of attributes from multiple tables
- Example

- SELECT FirstName, LastName, InvoiceDate
- FROM   customer, invoice
- WHERE  customer.CustomerId = invoice.CustomerId

---

## Query customisation


- Ordering of results
The ORDER BY keyword can be added at the end of a SELECT query,and qualified with the ASC or DESC keywords
- Example:

- SELECT something FROM someTable WHERE condition
- ORDER BY attribute1 [, attribute2] [ASC|DESC]

- SELECT FirstName, LastName, InvoiceDate
- FROM   customer, invoice
- WHERE  customer.CustomerId = invoice.CustomerId
- ORDER BY InvoiceDate DESC

---

## Query customisation


- Use of aliases for tables and attributes/results
We can use the AS keyword to create aliases for tables
- We can also rename (and even concatenate) attributes

- SELECT FirstName, LastName, InvoiceDate
- FROM   customer AS c, invoice AS i
- WHERE  c.CustomerId = i.CustomerId

- SELECT CONCAT(FirstName, " ", LastName) AS Name, InvoiceDate
- FROM   customer AS c, invoice AS i
- WHERE  c.CustomerId = i.CustomerId

---

## Multi-table queries


- JOIN operations
The JOIN operation combines attributes from several tables, and connects the tuplesbased on shared attributes (using the ON keyword).
- General syntax:

- SELECT something FROM someTable
- INNER|LEFT|RIGHT JOIN anotherTable
- ON someTable.attribute = anotherTable.attribute

---

## Multi-table queries


- INNER JOIN
The INNER JOIN keyword will select only those tuples where the connecting attribute value appears in both relations:
- Example:

- SELECT total FROM invoice
- INNER JOIN customer
- ON customer.CustomerId = invoice.CustomerId

---

## Multi-table queries


- JOINS LEFT AND RIGHT
In addition to INNER JOIN, MySQL also supports left and right joins of tables. Other implementations of SQL will also do FULL JOINs (the Cartesian Product of two tables).
A LEFT JOIN will return all tuples on the left and those with a matching attribute on the right.
A RIGHT JOIN will return all tuples on the right and those with a matching attribute on the left

---

## Special conditions


- WHERE EXISTS
This allows attaching a sub-query to a WHERE clause, which will return TRUE for every record obtained by the subquery.
- Syntax:

- SELECT attribute
- FROM table
- WHERE EXISTS (SELECT something FROM someTable WHERE condition)

---

## Special conditions


- WHERE EXISTS
This allows attaching a sub-query to a WHERE clause, which will return TRUE for every record obtained by the subquery.
- Example:

- SELECT total FROM invoice WHERE EXISTS
- (SELECT CustomerId FROM customer WHERE 						customer.CustomerId = invoice.CustomerId
- AND customer.Company IS NOT NULL)

---

## Special conditions


- Searching for patterns
The LIKE operator allows specifying a pattern rather than a specific value in a WHERE clause
- Special symbols for the pattern:
- % is a multi-character placeholder
- _ is a single-character placeholder

- SELECT attribute
- FROM table
- WHERE someAttribute LIKE pattern

---

## Special conditions


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

---

## Special conditions


- Looking for unspecified values
The IS NULL condition will yield results where the value of the attribute isNULL.
A common query  combines this with the logical NOT operator to expressIS NOT NULL, when looking for records that have a value for the attribute specified.

- SELECT *
- FROM customer WHERE State IS NOT NULL

---

## Recap


Recap

Server-side scripting

Scripts can be used to interact with and manipulate the HTML before it is being sent to the client.
Here, the server could run a script to process the HTTP request and assemble an HTML page that contains the correct information to be sent back to the client:(e.g., the requested information, an error message, an authentication request, …)


SCRIPT

Server

Client

HTML


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

## PHP


- Overview
- PHP is a popular server-side scripting language
PHP can be used to create interactive web applications that use databases
- PHP files have the index *.php
PHP is a higher-level language and interpreted at runtime, like Javascript
PHP documents can contain a mix of HTML and code but unlike Javascript, PHP programs will only run when placed on a web server (like the Apache webserver installed on your computers, which has a PHP interpreter module)

---

## PHP


- Basic syntax

- <?php
- // everything in here is PHP code
- echo "Hello World!";
- ?>

- Opening and closingtag for PHP

"echo" is a useful command for generating text outputs on the page

---

## PHP


- Embedded PHP
Example PHP documentthat has HTML markupand embedded PHP code

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

## PHP


- Variables and data types
- Variables in PHP are prefixed with a $ symbol
Variables are dynamically typed (same as in Javascript).

- <?php
- // everything in here is PHP code
- $output = "Hello World!";
- echo $output;
- ?>

- $output contains a string here

---

## PHP


- Variables and data types
We can concatenate strings and variable values using the dot (.) operator.(unlike Javascript, where we would use +)
However, due to the $ prefix for variables, the following will also work:

- <?php
- // everything in here is PHP code
- $output = "Hello World!";
- echo "This is my ".$output. " program.";
- ?>

- echo "This is my $output program.";

---

## PHP


- Conditional statements and loops
These work more or less exactly like those you already know from Javascript
- Example:

- <?php
- for ($i = 0; $i < 5; $i++) {
- echo "This is turn: $i <br>";
- }
- ?>

---

## PHP


- Functions
- Functions in PHP are declared with the function keyword

- <?php
- function write($text) {
- echo $text;
- }
- $output = "Hello World!";
- write($output);
- ?>

---

## PHP


- Variable scope
- Variables declared inside functions have local scope
- Variables declared outside functions have global scope
But the scoping is stricter than what we have seen in Javascript:
Global variables cannot be accessed within functionsIf you need a variable value in a function, it needs to be passed as a parameter

---

## Read


Connolly and Begg, Database Systems: A Practical Approach to Design, Implementation, and Management, Pearson Ed.
- Chapter 6: SQL data manipulation

---

## Next Lecture


- A few more SQL tricks
- Building web applications with PHP

---
