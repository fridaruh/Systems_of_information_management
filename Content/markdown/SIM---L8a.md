# SIM   L8a


## Systems for Information ManagementLecture 8a


- Dr Imran U Khan		School of Engineering and Informatics

---

## Previously


- Introduction to SQL & server-side scripting with PHP
- SQL data definition: CREATE, DROP, ALTER
- SQL data manipulation: INSERT INTO, SELECT, UPDATE, DELETE
- Naming conventions & disambiguation of attributes from multiple tables
- Queries involving multiple tables using JOIN
- Special conditions: IN, BETWEEN, LIKE
- Ordering of results: ORDER BY
- Server-side scripting revisited & a brief introduction to PHP

---

## Today


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

---

## Working with aggregates


- COUNT( )
This will return the number of rows in a relation (to which the given condition applies, if stated)
- Syntax:

- SELECT COUNT(attribute)
- FROM table WHERE condition

---

## Working with aggregates


- MIN( ) and MAX( )
This will return the smallest (or greatest for MAX) values distinct values.
- Syntax:

- SELECT MIN(attribute)
- FROM table
- WHERE condition

- SELECT MAX(attribute)
- FROM table
- WHERE condition

---

## Working with aggregates


- AVG( ) and SUM( )
These will return the average value, or sum, respectively, of the chosen column.
- Syntax:

- SELECT AVG(attribute)
- FROM table
- WHERE condition

- SELECT SUM(attribute)
- FROM table
- WHERE condition

---

## Value conversion


- CAST( )
The cast function converts a value of a certain type into another type.
- Example:

- SELECT CAST(AVG(total) AS DECIMAL(3,2))
- FROM invoice

---

## Grouping of results


- GROUP BY
This statement can be used to group results by an attribute and is commonly used in combination with aggregate functions
- Syntax:

- SELECT aggregate, attribute
- FROM table
- WHERE someCondition
- GROUP BY attribute

- Doesn't have to be the same attribute

---

## Grouping of results


- GROUP BY
This statement can be used to group aggregate results by another attribute and is commonly used in combination with aggregate functions
- Example: Returns the number of customers per country

- SELECT COUNT(CustomerId) as Amount, Country
- FROM customer
- GROUP BY Country
- ORDER BY Amount DESC

---

## Grouping of results


- GROUP BY
This statement can be used to group aggregate results by another attribute and is commonly used in combination with aggregate functions
Example 2: Returns the number of tracks on an album, grouped by albums

- SELECT album.Title, COUNT(track.TrackId) as tracks
- FROM album
- JOIN track
- ON album.AlbumId = track.AlbumId
- GROUP BY album.albumId

---

## Special conditions


- HAVING
- HAVING allows specifying a condition that involves an aggregate
- We need HAVING because WHERE cannot deal with aggregates
- Syntax:

- SELECT aggregate, attribute
- FROM table
- WHERE someCondition GROUP BY attribute
- HAVING someAggregateCondition

---

## Special conditions


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

---

## SELECT revisited


The SELECT statement can come with a range of qualifications and conditions
- Syntax overview:

- SELECT attribute(s)
- FROM table(s)
- WHERE condition(s)
- GROUP BY attribute
- HAVING aggregateCondition
- ORDER BY attribute(s)

---

## Multi-table queries


- Quick recap: JOIN operation
The JOIN operation combines attributes from several tables, and connects the tuplesbased on shared attributes (using the ON keyword).
- General syntax:

- SELECT something FROM someTable
- INNER|LEFT|RIGHT JOIN anotherTable
- ON someTable.attribute = anotherTable.attribute

---

## Multi-table queries


- UNION [ALL]
UNION combines the results of selecting type-compatible attributes from two or more tables – duplicates will be removed.
UNION ALL allows duplicate values.
- Syntax:

- SELECT attribute(s) FROM table
- UNION [ALL] SELECT attribute(s) FROM anotherTable

---

## Multi-table queries


- UNION [ALL]
UNION combines the results of selecting type-compatible attributes from two or more tables – duplicates will be removed.
UNION ALL allows duplicate values.
- Example:

- SELECT Country FROM customer
- UNION SELECT Country FROM employee

---

## PHP


- Recap
PHP is a server-side scripting language and its programs need a web server to run.
Apart from a few exceptions, PHP has a similar syntax as Javascript, and the programs share many basic coding conventions.
Variables in PHP are dynamically typed and start with a $ symbol, e.g. $output.
PHP may be embedded in HTML code, using one or more <?php … ?> sections.
Nevertheless, such files must have the".php" index in order for the PHP codeto be correctly interpreted.

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

## PHP – Basic language constructs


- Conditional statements and loops
- These basically work like those you already know from Javascript
- For example, an  if-else statement:

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

## PHP – Basic language constructs


- Conditional statements and loops
- This is what a  for-loop looks like in PHP:

- <?php
- for ($i = 0; $i < 10; $i++) {
- echo "This is turn: $i <br>";
- }
- ?>

---

## PHP – Basic language constructs


- Conditional statements and loops
- while, and do-while loops

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

## PHP – Basic language constructs


- Conditional statements and loops
- Here's a new one: foreach
The foreach-loop takes a data array as an input and iterates over each element
- Syntax:

- <?php
- foreach ($someArray as $oneItemFromArray) {
- // do something
- }
- ?>

---

## PHP – Basic language constructs


- Conditional statements and loops
- Example

- <?php
- $myArray = array("John","Peter","Mary","Linda");
- foreach ($myArray as $person) {
- echo "I like ".$person."<br>";
- }
- ?>

---

## PHP – Basic language constructs


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

## PHP – Basic language constructs


- Objects
- PHP supports object-orientation
- Example: A class

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

## PHP – Basic language constructs


- Objects - Example

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

## Next Lecture


- Web-based database applications with PHP, HTML, and SQL
- HTML forms revisited
- Sending and responding to HTTP requests
- Connecting to a database using PHP
- Executing SQL commands from a PHP program

---
