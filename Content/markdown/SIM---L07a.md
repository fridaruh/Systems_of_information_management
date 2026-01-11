# SIM   L07a

**Conversion date:** 2026-01-11
**Original file:** `SIM - L07a.pptx`
**Total slides:** 34

---


## Table of Contents

1. [Systems for Information ManagementLecture 7](#slide-1-systems-for-information-managementlecture-7)
2. [Previously](#slide-2-previously)
3. [Today](#slide-3-today)
4. [Relational algebra](#slide-4-relational-algebra)
5. [Relational algebra](#slide-5-relational-algebra)
6. [Relational algebra](#slide-6-relational-algebra)
7. [Relational algebra](#slide-7-relational-algebra)
8. [Relational algebra](#slide-8-relational-algebra)
9. [Relational algebra](#slide-9-relational-algebra)
10. [Set operations](#slide-10-set-operations)
11. [Set operations](#slide-11-set-operations)
12. [Set operations](#slide-12-set-operations)
13. [Set operations](#slide-13-set-operations)
14. [Set operations](#slide-14-set-operations)
15. [SQL](#slide-15-sql)
16. [SQL for data definition](#slide-16-sql-for-data-definition)
17. [SQL for data definition](#slide-17-sql-for-data-definition)
18. [SQL for data definition](#slide-18-sql-for-data-definition)
19. [SQL for data definition](#slide-19-sql-for-data-definition)
20. [SQL for data definition](#slide-20-sql-for-data-definition)
21. [SQL for data definition](#slide-21-sql-for-data-definition)
22. [SQL for data definition](#slide-22-sql-for-data-definition)
23. [SQL for data manipulation](#slide-23-sql-for-data-manipulation)
24. [SQL for data manipulation](#slide-24-sql-for-data-manipulation)
25. [SQL for data manipulation](#slide-25-sql-for-data-manipulation)
26. [SQL for data manipulation](#slide-26-sql-for-data-manipulation)
27. [SQL for data manipulation](#slide-27-sql-for-data-manipulation)
28. [SQL for data manipulation](#slide-28-sql-for-data-manipulation)
29. [SQL for data manipulation](#slide-29-sql-for-data-manipulation)
30. [SQL for data manipulation](#slide-30-sql-for-data-manipulation)
31. [SQL for data manipulation](#slide-31-sql-for-data-manipulation)
32. [SQL for data manipulation](#slide-32-sql-for-data-manipulation)
33. [Read](#slide-33-read)
34. [Next Lecture](#slide-34-next-lecture)

## 1. Systems for Information ManagementLecture 7 {#slide-1-systems-for-information-managementlecture-7}

### Content

- Dr Imran U Khan		School of Engineering and Informatics

---

## 2. Previously {#slide-2-previously}

### Content

- Database basics modelling
- Database architecture and schema
- Conceptual modelling (ERM)
- Logical modelling (Relations)

---

## 3. Today {#slide-3-today}

### Content

- SQL & Relational algebra
- Basics of relational algebra
- Basics of SQL for data definition
- Basics of SQL for data manipulation

---

## 4. Relational algebra {#slide-4-relational-algebra}

### Content

- Overview
A set of operations which satisfy the relational closure property i.e., the output from any operation on relation(s) should be another relation.
This means that the output from one operation can be the input to another relation … making it possible to write complex nested queries.
All relational database systems must support the relational operations of RESTRICT, PROJECT and JOIN.
Most do also support all traditional set operations such as UNION, INTERSECT, DIFFERENCE and CARTESIAN PRODUCT

---

## 5. Relational algebra {#slide-5-relational-algebra}

### Content

Relational algebra

SELECTION (also called RESTRICTION)

Returns a relation that contains the selected attributes (columns) of all tuples from a specified relation satisfying a specified condition (if any).

Base relation: S

Derived relation: S WHERE SURNAME = “Smith”

### Visual Analysis

# Relational Algebra: Selection Operation

## Definition

**Selection** (also called **Restriction**) is a relational algebra operation that returns a relation containing the selected attributes (columns) of all tuples from a specified relation that satisfy a specified condition.

## Key Characteristics

- Operates on a single base relation
- Filters tuples (rows) based on a condition
- Produces a derived relation as output
- Preserves the same attributes as the base relation

## Syntax Pattern

```
<Derived Relation> = <Base Relation> WHERE <Condition>
```

## Example

**Base relation:** S

**Operation:** Apply selection with condition `SURNAME = "Smith"`

**Derived relation:** S WHERE SURNAME = "Smith"

This operation returns only those tuples from relation S where the SURNAME attribute has the value "Smith".

## Important Note

The selection operation filters rows (tuples) based on conditions, not columns. Despite the text mentioning "selected attributes," the primary function of SELECTION is to filter tuples that meet the specified condition while retaining all original attributes of those tuples.

---

## 6. Relational algebra {#slide-6-relational-algebra}

### Content

Relational algebra

PROJECTION

Returns a relation that contains all tuples that represent a vertical subset of S, extracting the values of specified attributes and eliminating duplicates.

Base relation: S

Derived relation: S[CAND, DOB]

Derived relation: S[COURSE]

### Visual Analysis

# Relational Algebra: Projection Operation

## Definition

**Projection** is a relational algebra operation that returns a relation containing all tuples that represent a vertical subset of a base relation. The operation:

- Extracts the values of specified attributes (columns)
- Eliminates duplicate tuples from the result
- Produces a derived relation with fewer columns than the original

## Operation Characteristics

The projection operation performs vertical subsetting, meaning it selects specific columns from a relation while retaining all rows (after removing duplicates).

## Notation

The projection operation is denoted using square brackets:
- Format: `S[attribute1, attribute2, ...]`
- Where `S` is the base relation
- Attributes listed are those to be included in the result

## Examples

### Example 1: Multi-attribute Projection
**Base relation:** S

**Derived relation:** S[CAND, DOB]

This projection extracts only the CAND (candidate) and DOB (date of birth) attributes from relation S, returning a relation with just these two columns.

### Example 2: Single-attribute Projection
**Base relation:** S

**Derived relation:** S[COURSE]

This projection extracts only the COURSE attribute from relation S, returning a relation with a single column containing all unique course values.

## Key Properties

- **Duplicate elimination**: If multiple tuples have identical values for the projected attributes, only one copy appears in the result
- **Reduced arity**: The resulting relation has fewer or equal attributes compared to the original
- **Preserved tuple semantics**: Each tuple in the result represents valid data from the original relation

---

## 7. Relational algebra {#slide-7-relational-algebra}

### Content

- JOIN
Returns a relation consisting of all possible tuples that are a combination of two tuples, one from each of the specified relations, such that the two tuples contributing to any given combination have a common value for (a) shared attribute(s) of the two relations.

---

## 8. Relational algebra {#slide-8-relational-algebra}

### Content

Relational algebra

JOIN - Example

Base relation: S

Base relation: C

Derived relation: S JOIN C

### Visual Analysis

# JOIN Operation in Relational Algebra

## Concept

JOIN is a relational algebra operation that combines tuples from two base relations based on a common attribute or related attributes.

## Structure

The JOIN operation takes two base relations as input and produces a derived relation as output:

**Base relation: S** → Input relation 1
**Base relation: C** → Input relation 2
**Derived relation: S JOIN C** → Result of combining S and C

## Purpose

JOIN operations combine data from multiple tables by matching rows based on related columns, enabling queries that span multiple relations in a relational database.

## General Form

```
Relation1 JOIN Relation2
```

The specific join condition and type of join (natural join, equijoin, theta join) would determine which tuples from S and C are combined and how they appear in the result.

---

## 9. Relational algebra {#slide-9-relational-algebra}

### Content

Relational algebra

JOIN - Example

Base relation: S

Base relation: C

Derived relation: S JOIN C

### Visual Analysis

# JOIN Operation in Relational Algebra

## Definition
JOIN is a relational algebra operation that combines tuples from two base relations based on a related attribute between them.

## Operation Structure
The JOIN operation takes two base relations as input and produces a derived relation as output:
- **Base relation S**: First input relation
- **Base relation C**: Second input relation  
- **Derived relation: S JOIN C**: Result of combining the two relations

## Purpose
JOIN allows combining data from multiple tables by matching rows that share common attribute values, enabling retrieval of related information stored across different relations.

## Notation
The operation is expressed as:
```
S JOIN C
```

This produces a new relation containing attributes from both S and C, with tuples formed by matching related records from each relation.

---

## 10. Set operations {#slide-10-set-operations}

### Content

- Overview
Union: returns a relation that contains all tuples appearing in either or both of two type-compatible input relations.
Intersection: returns a relation that contains those tuples appearing in both type-compatible relations
Difference: returns a relation that contains those tuples appearing in the first but not in the second of two type-compatible relations
Cartesian Product: returns a relation that concatenates all tuples across two relations

---

## 11. Set operations {#slide-11-set-operations}

### Content

Set operations

Example: Union

Base relation: Informatics students

Base relation: UG students

Derived relation: Informatics students ⋃ UG students

### Visual Analysis

# Set Operations: Union

## Union Operation

The union operation combines two relations by including all tuples (rows) that appear in either relation, eliminating duplicates.

**Notation:** ⋃

## Example

**Operation:** Informatics students ⋃ UG students

**Input Relations:**
- Base relation 1: Informatics students
- Base relation 2: UG students

**Output Relation:**
- Derived relation: Contains all students who are either Informatics students OR undergraduate (UG) students OR both

## Key Characteristics

- Results in a single relation containing all distinct tuples from both input relations
- Duplicate tuples are automatically removed
- Both relations must have compatible schemas (same number of attributes with compatible data types)
- The resulting relation includes students from both categories without repetition

---

## 12. Set operations {#slide-12-set-operations}

### Content

Set operations

Example: Intersection

Base relation: Informatics students

Base relation: UG students

Derived relation: Informatics students ⋂ UG students

### Visual Analysis

# Set Operations: Intersection

## Concept

**Intersection** is a set operation that produces a derived relation containing only the elements (tuples) that exist in **both** base relations.

## Operation Notation

**Informatics students ⋂ UG students**

The intersection symbol (⋂) represents the operation that combines two relations.

## Example Breakdown

### Base Relations
1. **Informatics students** - relation containing all students enrolled in Informatics
2. **UG students** - relation containing all undergraduate students

### Derived Relation
**Informatics students ⋂ UG students** - produces a new relation containing only students who are:
- Enrolled in Informatics **AND**
- Classified as undergraduate students

## Key Properties

- Both base relations must be **union-compatible** (same structure/schema)
- The result contains only tuples that appear in both input relations
- Order of operands does not matter: A ⋂ B = B ⋂ A (commutative property)
- The resulting relation size is always less than or equal to the smaller base relation

## Practical Application

This operation is useful for:
- Finding common members across different groups
- Identifying overlap between datasets
- Filtering data based on multiple criteria
- Creating more specific subsets from broader categories

---

## 13. Set operations {#slide-13-set-operations}

### Content

Set operations

Example: Difference

Base relation: Informatics students

Base relation: UG students

Derived relation: Informatics students \ UG students

### Visual Analysis

# Set Difference Operation

## Concept

The **difference operation** (denoted by `\`) is a set operation that returns elements present in the first relation but not in the second relation.

## Syntax

```
Relation A \ Relation B
```

This produces a derived relation containing all tuples from Relation A that are not in Relation B.

## Example

**Base Relation 1:** Informatics students
- Contains all students enrolled in Informatics programs

**Base Relation 2:** UG students (Undergraduate students)
- Contains all undergraduate students

**Derived Relation:** Informatics students \ UG students
- **Result:** All Informatics students who are NOT undergraduate students
- This would include postgraduate students (Master's, PhD) and any other non-undergraduate Informatics students

## Key Characteristics

- The difference operation is **not commutative**: A \ B ≠ B \ A
- Only tuples from the first relation that have no matching tuple in the second relation are included
- Both relations must be union-compatible (same number of attributes with compatible domains)

---

## 14. Set operations {#slide-14-set-operations}

### Content

Set operations

Example: Cartesian product

Base relation: Students

Base relation: Schools

Derived relation:

Students × Schools

### Visual Analysis

# Set Operations: Cartesian Product

## Definition

The Cartesian product is a set operation that combines two base relations by creating all possible pairings between tuples from the first relation with tuples from the second relation.

## Operation Notation

**Students × Schools**

This notation represents the Cartesian product operation between the Students relation and the Schools relation.

## Result Structure

When performing a Cartesian product:
- Each tuple (row) from the Students relation is paired with every tuple from the Schools relation
- If Students has *m* tuples and Schools has *n* tuples, the resulting relation will have *m × n* tuples
- The resulting relation contains all attributes from both base relations combined

## Example Components

**Base Relation 1:** Students
- Contains student data

**Base Relation 2:** Schools  
- Contains school data

**Derived Relation:** Students × Schools
- Contains all possible combinations of student-school pairs
- Combines attributes from both Students and Schools relations

## Practical Implications

The Cartesian product often produces a large result set that may include many meaningless combinations. In practice, it is typically used as an intermediate step that is then filtered with selection conditions to obtain meaningful relationships between entities.

---

## 15. SQL {#slide-15-sql}

### Content

- Overview
The structured query language (SQL) is the quasi-standard for performing DDL as well as DML operations in relational databases.
- As such, SQL facilitates relational algebra operations
SQL has DDL commands for creating, changing, and deleting relations and domains
SQL has DML commands that correspond to the fundamental operations on data in a database (CRUD)

- Operations on data
- Create:	  INSERT INTO
- Read:	  SELECT
- Update:	  UPDATE
- Delete:	  DELETE

- Commands for schema creation / updates:
- Create relation or domain:    CREATE
- Change relation or domain:  ALTER
- Delete relation or domain:     DROP

Note that basic SQL keywords are not case-sensitive, e.g. “CREATE” is the same as “create”.

---

## 16. SQL for data definition {#slide-16-sql-for-data-definition}

### Content

- Create / Delete a database: CREATE / DROP DATABASE
- Syntax:
- Example:

- CREATE DATABASE name

- DROP DATABASE [IF EXISTS] name

- CREATE DATABASE dvdcollection

---

## 17. SQL for data definition {#slide-17-sql-for-data-definition}

### Content

- Create a relation (table): CREATE
- Syntax:

CREATE TABLE tableName (	attributeName domain [constraint],	attributeName domain [constraint],	[otherConstraints] )

---

## 18. SQL for data definition {#slide-18-sql-for-data-definition}

### Content

SQL for data definition

Create a relation (table): CREATE

Example:

CREATE TABLE films(
	title VARCHAR(60) PRIMARY KEY,
	year YEAR NOT NULL,
	runtime INT NOT NULL
 )

### Visual Analysis

# SQL Data Definition - CREATE TABLE

## Core Concept

SQL provides Data Definition Language (DDL) commands to create and define database structures. The `CREATE TABLE` statement is used to define a new relation (table) in a database.

## CREATE TABLE Syntax

The basic structure for creating a table includes:
- Table name
- Column definitions with data types
- Constraints (optional)

## Example: Creating a Films Table

```sql
CREATE TABLE films(
    title VARCHAR(60) PRIMARY KEY,
    year YEAR NOT NULL,
    runtime INT NOT NULL
)
```

## Components Explained

### Column Definitions

- **title**: Variable character field with maximum length of 60 characters
- **year**: YEAR data type for storing year values
- **runtime**: Integer field for storing numeric values (likely minutes)

### Constraints Applied

- **PRIMARY KEY**: Applied to `title` field
  - Ensures uniqueness for each film title
  - Automatically creates an index
  - Cannot contain NULL values

- **NOT NULL**: Applied to `year` and `runtime` fields
  - Requires values to be provided for these columns
  - Prevents empty/null entries

## Key Principles

- Each column must have a defined data type
- Constraints enforce data integrity rules
- Primary keys uniquely identify each row in the table
- NOT NULL constraints ensure required data is always present

---

## 19. SQL for data definition {#slide-19-sql-for-data-definition}

### Content

- Delete a relation (table): DROP TABLE
- Example:

- DROP TABLE IF EXISTS films

---

## 20. SQL for data definition {#slide-20-sql-for-data-definition}

### Content

SQL for data definition

Create a relation (table) – composite primary key variant

Example:

CREATE TABLE films(
	title VARCHAR(60),
	year YEAR,
	runtime INT NOT NULL,
	PRIMARY KEY (title, year)
 )

### Visual Analysis

# SQL Data Definition: Composite Primary Keys

## Creating Tables with Composite Primary Keys

A composite primary key uses multiple columns combined to uniquely identify each row in a table, rather than a single column.

## Syntax

```sql
CREATE TABLE table_name(
    column1 datatype,
    column2 datatype,
    column3 datatype,
    PRIMARY KEY (column1, column2)
)
```

## Example: Films Table

```sql
CREATE TABLE films(
    title VARCHAR(60),
    year YEAR,
    runtime INT NOT NULL,
    PRIMARY KEY (title, year)
)
```

### Table Structure

| Column | Data Type | Constraints |
|--------|-----------|-------------|
| title | VARCHAR(60) | Part of primary key |
| year | YEAR | Part of primary key |
| runtime | INT | NOT NULL |

### Key Concepts

**Composite Primary Key Components:**
- `title` and `year` together form the primary key
- This combination must be unique for each row
- Allows the same film title in different years (e.g., remakes)
- Both columns are implicitly NOT NULL as part of the primary key

**Use Case:**
This design accommodates scenarios where:
- Multiple films can have the same title
- The same film title released in different years are treated as distinct entries
- The combination of title and release year uniquely identifies each film

---

## 21. SQL for data definition {#slide-21-sql-for-data-definition}

### Content

- Modify a relation (table): ALTER TABLE
- Syntax:

- ALTER TABLE tableName	ADD/DROP/MODIFY [attributeName] [constraint]

---

## 22. SQL for data definition {#slide-22-sql-for-data-definition}

### Content

SQL for data definition

Modify a relation (table): ALTER TABLE

Example:

ALTER TABLE films	ADD COLUMN director VARCHAR(40);

### Visual Analysis

# SQL Data Definition: ALTER TABLE Command

## Modifying Database Relations

The `ALTER TABLE` statement is used to modify the structure of existing tables (relations) in a database after they have been created.

## Adding Columns to Existing Tables

### Syntax
```sql
ALTER TABLE table_name ADD COLUMN column_name data_type;
```

### Example

```sql
ALTER TABLE films ADD COLUMN director VARCHAR(40);
```

This command:
- Modifies the existing `films` table
- Adds a new column named `director`
- Sets the data type to `VARCHAR(40)`, allowing text strings up to 40 characters in length

## Key Concepts

- **ALTER TABLE**: DDL (Data Definition Language) command for modifying table structure
- **ADD COLUMN**: Specific operation to insert a new column into an existing table
- **VARCHAR(40)**: Variable-length character data type with maximum length of 40 characters
- The operation affects the table schema without deleting existing data
- New column will be added to all existing rows (typically with NULL values unless a default is specified)

---

## 23. SQL for data manipulation {#slide-23-sql-for-data-manipulation}

### Content

- Create data: INSERT INTO
This will create a new tuple in the stated relation.
- Syntax:

- INSERT INTO tableName [ ( attribute1, attribute2,…) ]
- VALUES (value1, value2, …)

We can leave out the list of attribute names when specifying values for all defined attributes of a relation, otherwise we need to state where each value goes.

---

## 24. SQL for data manipulation {#slide-24-sql-for-data-manipulation}

### Content

SQL for data manipulation

Create data: INSERT INTO

Example:

INSERT INTO films ( title, year, runtime )
	VALUES ("Bladerunner", "1982" , 117)

### Visual Analysis

# SQL Data Manipulation - INSERT Statement

## Creating New Data Records

The `INSERT INTO` statement is used to add new rows of data into a database table.

## Basic Syntax

```sql
INSERT INTO table_name ( column1, column2, column3 )
VALUES ( value1, value2, value3 )
```

## Components

- **INSERT INTO**: SQL command to create new data
- **table_name**: The target table where data will be inserted
- **column names**: Specified columns that will receive values (in parentheses)
- **VALUES**: Keyword followed by the actual data to insert
- **values**: Data corresponding to each column (in parentheses, in the same order)

## Example Implementation

```sql
INSERT INTO films ( title, year, runtime )
VALUES ("Bladerunner", "1982", 117)
```

This statement:
- Inserts a new record into the `films` table
- Populates three specific columns: `title`, `year`, and `runtime`
- Assigns the values:
  - title: "Bladerunner" (string)
  - year: "1982" (string)
  - runtime: 117 (numeric value in minutes)

## Key Principles

- Column names and values must correspond in order and quantity
- String values are enclosed in quotation marks
- Numeric values do not require quotation marks
- All specified columns will receive the provided values

---

## 25. SQL for data manipulation {#slide-25-sql-for-data-manipulation}

### Content

SQL for data manipulation

Create data: INSERT INTO

Inserting multiple records with a single statement:

INSERT INTO films ( title, year, runtime )
	VALUES	("The Fifth Element", "1997", 126),
		("TRON", "1982", 96),
		("Stargate", "1994", 116)

### Visual Analysis

# SQL Data Manipulation: INSERT INTO

## Multiple Record Insertion

SQL allows inserting multiple records into a table with a single INSERT statement, improving efficiency over individual inserts.

### Syntax Structure

```sql
INSERT INTO table_name ( column1, column2, column3 )
VALUES  (value1a, value2a, value3a),
        (value1b, value2b, value3b),
        (value1c, value2c, value3c)
```

### Practical Example

```sql
INSERT INTO films ( title, year, runtime )
VALUES  ("The Fifth Element", "1997", 126),
        ("TRON", "1982", 96),
        ("Stargate", "1994", 116)
```

This statement:
- Targets the `films` table
- Specifies three columns: `title`, `year`, and `runtime`
- Inserts three film records in one operation
- Each row in the VALUES clause represents one complete record

### Key Components

- **Table name**: `films` - the target table for data insertion
- **Column list**: Explicitly defines which columns receive data
- **VALUES clause**: Contains comma-separated tuples, each representing one record
- **Data types**: Mix of text strings (in quotes) and numeric values (runtime without quotes)

### Benefits

- Reduces database round trips
- More efficient than multiple single-row INSERT statements
- Cleaner, more maintainable code
- Better performance for bulk data insertion

---

## 26. SQL for data manipulation {#slide-26-sql-for-data-manipulation}

### Content

- Read data: SELECT
SELECT returns a derived relation.
- Syntax:

- SELECT	attributes(s)
- FROM		one or more tables [WHERE	some condition applies]

---

## 27. SQL for data manipulation {#slide-27-sql-for-data-manipulation}

### Content

- Read data: SELECT
- Example:

- SELECT * FROM films

Wildcard selector: This will return all defined attributesof the relation

- No WHERE condition

---

## 28. SQL for data manipulation {#slide-28-sql-for-data-manipulation}

### Content

- Read data: SELECT
- Another example:

- SELECT title
- FROM films
- WHERE runtime < 100

- We can do arithmetic on number types (like INT)

---

## 29. SQL for data manipulation {#slide-29-sql-for-data-manipulation}

### Content

- Update (modify) data: UPDATE
Update allows us to make changes to one or more existing records (add values / modify values).
- Syntax:

- UPDATE	tableName
SET		attribute1 = value1, attribute2 = value2,… [WHERE	some condition applies]

---

## 30. SQL for data manipulation {#slide-30-sql-for-data-manipulation}

### Content

SQL for data manipulation

Update (modify) data: UPDATE

Example:

UPDATE	films
 SET		director = "Ridley Scott" WHERE		title = "Bladerunner" AND year = 1982

We can concatenate conditional expressions using logic operators

### Visual Analysis

# SQL UPDATE Statement

## Purpose
The UPDATE statement modifies existing data in database tables.

## Basic Syntax
```sql
UPDATE table_name
SET column = value
WHERE condition
```

## Example: Updating a Film Record
```sql
UPDATE films
SET director = "Ridley Scott"
WHERE title = "Bladerunner" AND year = 1982
```

This statement:
- Targets the `films` table
- Changes the `director` column to "Ridley Scott"
- Only affects records matching both conditions: title is "Bladerunner" AND year is 1982

## Conditional Expressions with Logic Operators

Multiple conditions can be combined using logical operators to create more precise WHERE clauses:

- **AND**: Both conditions must be true
- **OR**: At least one condition must be true
- **NOT**: Negates a condition

The example demonstrates using AND to ensure only the specific 1982 film "Bladerunner" is updated, not any other films with similar titles or years.

## Key Considerations

- The WHERE clause is critical—without it, all records in the table would be updated
- Multiple conditions allow precise targeting of specific records
- Logic operators enable complex filtering logic for data manipulation

---

## 31. SQL for data manipulation {#slide-31-sql-for-data-manipulation}

### Content

- Delete data: DELETE
DELETE removes one or more records from a table.
- Syntax:

- DELETE FROM	tableName
- [WHERE some condition applies]

Make sure to always state a WHERE clause unless you wishto delete all records in a table!

---

## 32. SQL for data manipulation {#slide-32-sql-for-data-manipulation}

### Content

- Delete data: DELETE
- Example

- DELETE FROM	films
- WHERE year < 2000

Make sure you understand what effect your WHERE clause will have on the selection of records to delete (Also when updating).

---

## 33. Read {#slide-33-read}

### Content

Connolly and Begg, Database Systems: A Practical Approach to Design, Implementation, and Management, Pearson Ed.
- Chapter 5.1: The relational algebra
- Chapter 6: SQL data manipulation
- Chapter 7: SQL data definition

---

## 34. Next Lecture {#slide-34-next-lecture}

### Content

- More sophisticated SQL queries
- Introduction to server-side scripting with PHP

- 34

---


---

## Processing Metadata

### Slide Classification
- Text slides: 20
- Visual slides: 14
- Optimized percentage (without API): 58.8%

### API Costs
- Input tokens: 58,776
- Output tokens: 12,779
- Total cost: $0.3680 USD

### System
- Generated by: PPTX to Markdown Converter
- Date: 2026-01-11 19:10:13