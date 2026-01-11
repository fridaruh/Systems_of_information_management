# SIM   L8a

**Conversion date:** 2026-01-11
**Original file:** `SIM - L8a.pptx`
**Total slides:** 26

---


## Table of Contents

1. [Systems for Information ManagementLecture 8a](#slide-1-systems-for-information-managementlecture-8a)
2. [Previously](#slide-2-previously)
3. [Today](#slide-3-today)
4. [Working with aggregates](#slide-4-working-with-aggregates)
5. [Working with aggregates](#slide-5-working-with-aggregates)
6. [Working with aggregates](#slide-6-working-with-aggregates)
7. [Value conversion](#slide-7-value-conversion)
8. [Grouping of results](#slide-8-grouping-of-results)
9. [Grouping of results](#slide-9-grouping-of-results)
10. [Grouping of results](#slide-10-grouping-of-results)
11. [Special conditions](#slide-11-special-conditions)
12. [Special conditions](#slide-12-special-conditions)
13. [SELECT revisited](#slide-13-select-revisited)
14. [Multi-table queries](#slide-14-multi-table-queries)
15. [Multi-table queries](#slide-15-multi-table-queries)
16. [Multi-table queries](#slide-16-multi-table-queries)
17. [PHP](#slide-17-php)
18. [PHP – Basic language constructs](#slide-18-php--basic-language-constructs)
19. [PHP – Basic language constructs](#slide-19-php--basic-language-constructs)
20. [PHP – Basic language constructs](#slide-20-php--basic-language-constructs)
21. [PHP – Basic language constructs](#slide-21-php--basic-language-constructs)
22. [PHP – Basic language constructs](#slide-22-php--basic-language-constructs)
23. [PHP – Basic language constructs](#slide-23-php--basic-language-constructs)
24. [PHP – Basic language constructs](#slide-24-php--basic-language-constructs)
25. [PHP – Basic language constructs](#slide-25-php--basic-language-constructs)
26. [Next Lecture](#slide-26-next-lecture)

## 1. Systems for Information ManagementLecture 8a {#slide-1-systems-for-information-managementlecture-8a}

### Content

- Dr Imran U Khan		School of Engineering and Informatics

---

## 2. Previously {#slide-2-previously}

### Content

- Introduction to SQL & server-side scripting with PHP
- SQL data definition: CREATE, DROP, ALTER
- SQL data manipulation: INSERT INTO, SELECT, UPDATE, DELETE
- Naming conventions & disambiguation of attributes from multiple tables
- Queries involving multiple tables using JOIN
- Special conditions: IN, BETWEEN, LIKE
- Ordering of results: ORDER BY
- Server-side scripting revisited & a brief introduction to PHP

- 2

---

## 3. Today {#slide-3-today}

### Content

- SQL and PHP continued
- SQL:
- Aggregate functions: COUNT(), MIN(), MAX(), AVG(), SUM()
- Conversion of values with CAST()
- Grouping of results: GROUP BY
- Special conditions (aggregates): HAVING
- UNION
- PHP Basics
- Control structures: If-then, Loops
- Functions
- Objects

- 3

---

## 4. Working with aggregates {#slide-4-working-with-aggregates}

### Content

- COUNT( )
This will return the number of rows in a relation (to which the given condition applies, if stated)
- Syntax:

- SELECT COUNT(attribute)
- FROM table WHERE condition

- 4

---

## 5. Working with aggregates {#slide-5-working-with-aggregates}

### Content

- MIN( ) and MAX( )
This will return the smallest (or greatest for MAX) values distinct values.
- Syntax:

- SELECT MIN(attribute)
- FROM table
- WHERE condition

- 5

- SELECT MAX(attribute)
- FROM table
- WHERE condition

---

## 6. Working with aggregates {#slide-6-working-with-aggregates}

### Content

- AVG( ) and SUM( )
These will return the average value, or sum, respectively, of the chosen column.
- Syntax:

- 6

- SELECT AVG(attribute)
- FROM table
- WHERE condition

- SELECT SUM(attribute)
- FROM table
- WHERE condition

---

## 7. Value conversion {#slide-7-value-conversion}

### Content

- CAST( )
The cast function converts a value of a certain type into another type.
- Example:

- 7

- SELECT CAST(AVG(total) AS DECIMAL(3,2))
- FROM invoice

---

## 8. Grouping of results {#slide-8-grouping-of-results}

### Content

- GROUP BY
This statement can be used to group results by an attribute and is commonly used in combination with aggregate functions
- Syntax:

- SELECT aggregate, attribute
- FROM table
- WHERE someCondition
- GROUP BY attribute

- 8

- Doesn't have to be the same attribute

---

## 9. Grouping of results {#slide-9-grouping-of-results}

### Content

- GROUP BY
This statement can be used to group aggregate results by another attribute and is commonly used in combination with aggregate functions
- Example: Returns the number of customers per country

- SELECT COUNT(CustomerId) as Amount, Country
- FROM customer
- GROUP BY Country
- ORDER BY Amount DESC

- 9

---

## 10. Grouping of results {#slide-10-grouping-of-results}

### Content

- GROUP BY
This statement can be used to group aggregate results by another attribute and is commonly used in combination with aggregate functions
Example 2: Returns the number of tracks on an album, grouped by albums

- SELECT album.Title, COUNT(track.TrackId) as tracks
- FROM album
- JOIN track
- ON album.AlbumId = track.AlbumId
- GROUP BY album.albumId

- 10

---

## 11. Special conditions {#slide-11-special-conditions}

### Content

- HAVING
- HAVING allows specifying a condition that involves an aggregate
- We need HAVING because WHERE cannot deal with aggregates
- Syntax:

- 11

- SELECT aggregate, attribute
- FROM table
- WHERE someCondition GROUP BY attribute
- HAVING someAggregateCondition

---

## 12. Special conditions {#slide-12-special-conditions}

### Content

- HAVING
Complex example: Select artist name, album title, and the number of tracks on the album, where the mediatype is 1 (MPEG audio) and the album has more than 9 tracks,and display the results grouped by album.

- SELECT artist.Name, album.Title, COUNT(track.TrackId) as tracks
- FROM album
- JOIN track
- ON track.AlbumId = album.AlbumId
- JOIN artist
- ON album.ArtistId = artist.ArtistId
- WHERE MediaTypeId = 1
- GROUP BY album.albumId
- HAVING tracks > 9
- ORDER BY tracks DESC

- 12

---

## 13. SELECT revisited {#slide-13-select-revisited}

### Content

The SELECT statement can come with a range of qualifications and conditions
- Syntax overview:

- SELECT attribute(s)
- FROM table(s)
- WHERE condition(s)
- GROUP BY attribute
- HAVING aggregateCondition
- ORDER BY attribute(s)

- 13

---

## 14. Multi-table queries {#slide-14-multi-table-queries}

### Content

- Quick recap: JOIN operation
The JOIN operation combines attributes from several tables, and connects the tuplesbased on shared attributes (using the ON keyword).
- General syntax:

- SELECT something FROM someTable
- INNER|LEFT|RIGHT JOIN anotherTable
- ON someTable.attribute = anotherTable.attribute

- 14

---

## 15. Multi-table queries {#slide-15-multi-table-queries}

### Content

- UNION [ALL]
UNION combines the results of selecting type-compatible attributes from two or more tables – duplicates will be removed.
UNION ALL allows duplicate values.
- Syntax:

- 15

- SELECT attribute(s) FROM table
- UNION [ALL] SELECT attribute(s) FROM anotherTable

---

## 16. Multi-table queries {#slide-16-multi-table-queries}

### Content

- UNION [ALL]
UNION combines the results of selecting type-compatible attributes from two or more tables – duplicates will be removed.
UNION ALL allows duplicate values.
- Example:

- 16

- SELECT Country FROM customer
- UNION SELECT Country FROM employee

---

## 17. PHP {#slide-17-php}

### Content

- Recap
PHP is a server-side scripting language and its programs need a web server to run.
Apart from a few exceptions, PHP has a similar syntax as Javascript, and the programs share many basic coding conventions.
Variables in PHP are dynamically typed and start with a $ symbol, e.g. $output.
PHP may be embedded in HTML code, using one or more <?php … ?> sections.
Nevertheless, such files must have the".php" index in order for the PHP codeto be correctly interpreted.

- 17

- <!DOCTYPE html>
- <html>
- <body>
- <h1>Welcome</h1> <?php
- // everything in here is PHP code
- $output = "Hello World";
- echo "<p>".$output."</p>";
- ?>
- </body>
- </html>

- helloworld.php

---

## 18. PHP – Basic language constructs {#slide-18-php--basic-language-constructs}

### Content

- Conditional statements and loops
- These basically work like those you already know from Javascript
- For example, an  if-else statement:

- 18

- <?php
- $i = 0;
- if($i < 10) {
- // do something
- }
- else {
- // do something else
- }
- ?>

---

## 19. PHP – Basic language constructs {#slide-19-php--basic-language-constructs}

### Content

- Conditional statements and loops
- This is what a  for-loop looks like in PHP:

- 19

- <?php
- for ($i = 0; $i < 10; $i++) {
- echo "This is turn: $i <br>";
- }
- ?>

---

## 20. PHP – Basic language constructs {#slide-20-php--basic-language-constructs}

### Content

- Conditional statements and loops
- while, and do-while loops

- 20

- <?php
- $i = 0;
- while ($i < 10) {
- echo "This is turn: $i <br>";      $i++;
- }
- ?>

- <?php
- $i = 0;
- do {
- echo "This is turn: $i <br>";      $i++;
- } while ($i < 10);
- ?>

---

## 21. PHP – Basic language constructs {#slide-21-php--basic-language-constructs}

### Content

- Conditional statements and loops
- Here's a new one: foreach
The foreach-loop takes a data array as an input and iterates over each element
- Syntax:

- 21

- <?php
- foreach ($someArray as $oneItemFromArray) {
- // do something
- }
- ?>

---

## 22. PHP – Basic language constructs {#slide-22-php--basic-language-constructs}

### Content

- Conditional statements and loops
- Example

- 22

- <?php
- $myArray = array("John","Peter","Mary","Linda");
- foreach ($myArray as $person) {
- echo "I like ".$person."<br>";
- }
- ?>

---

## 23. PHP – Basic language constructs {#slide-23-php--basic-language-constructs}

### Content

- Functions
- Functions in PHP are declared with the function keyword

- 23

- <?php
- function write($text) {
- echo $text;
- }
- $output = "Hello World!";
- write($output);
- ?>

---

## 24. PHP – Basic language constructs {#slide-24-php--basic-language-constructs}

### Content

- Objects
- PHP supports object-orientation
- Example: A class

- 24

- <?php
- class Person {
- // Data:
- public $name;
- // Methods:
- function setName($n) {
- $this->name = $n;
- }
- }
- ?>

Access modifier: publicThis controls how the data of an object can be accessed (private variables cannot be accessed directly, only through an interface, i.e. a method).

Object operator:  ->This is like the dot operator in Javascript objects. It allows accessing the data or methods of a specific object.

---

## 25. PHP – Basic language constructs {#slide-25-php--basic-language-constructs}

### Content

- Objects - Example

- 25

- <?php
- class Person {
- // Data:
- public $name;
- // Methods:
- function setName($n) {
- $this->name = $n;
- }
- }
- // program continued on the right

- $john = new Person();
- $john->setName("John");
- echo $john->name;
- ?>

- Create new object of type "Person"

- Use a method to change the object state

- Access a public variable directly

---

## 26. Next Lecture {#slide-26-next-lecture}

### Content

- Web-based database applications with PHP, HTML, and SQL
- HTML forms revisited
- Sending and responding to HTTP requests
- Connecting to a database using PHP
- Executing SQL commands from a PHP program

- 26

---


---

## Processing Metadata

### Slide Classification
- Text slides: 26
- Visual slides: 0
- Optimized percentage (without API): 100.0%

### API Costs
- Input tokens: 0
- Output tokens: 0
- Total cost: $0.0000 USD

### System
- Generated by: PPTX to Markdown Converter
- Date: 2026-01-11 19:11:09