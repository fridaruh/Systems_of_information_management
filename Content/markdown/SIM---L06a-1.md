# SIM   L06a (1)

**Conversion date:** 2026-01-11
**Original file:** `SIM - L06a (1).pptx`
**Total slides:** 25

---


## Table of Contents

1. [Systems for Information ManagementLecture 6a](#slide-1-systems-for-information-managementlecture-6a)
2. [Previously](#slide-2-previously)
3. [Today](#slide-3-today)
4. [Recap](#slide-4-recap)
5. [Recap](#slide-5-recap)
6. [Relations](#slide-6-relations)
7. [Candidate keys](#slide-7-candidate-keys)
8. [Candidate keys](#slide-8-candidate-keys)
9. [Domains](#slide-9-domains)
10. [Mapping of conceptual to relational model](#slide-10-mapping-of-conceptual-to-relational-model)
11. [Mapping of conceptual to relational model](#slide-11-mapping-of-conceptual-to-relational-model)
12. [Weak and strong entities](#slide-12-weak-and-strong-entities)
13. [Weak and strong entities](#slide-13-weak-and-strong-entities)
14. [Associative entities](#slide-14-associative-entities)
15. [Associative entities](#slide-15-associative-entities)
16. [Associative entities](#slide-16-associative-entities)
17. [Attributes](#slide-17-attributes)
18. [Attributes](#slide-18-attributes)
19. [Attributes](#slide-19-attributes)
20. [Attributes](#slide-20-attributes)
21. [Relationships](#slide-21-relationships)
22. [Relationships](#slide-22-relationships)
23. [Relationships](#slide-23-relationships)
24. [Read](#slide-24-read)
25. [Next Lecture](#slide-25-next-lecture)

## 1. Systems for Information ManagementLecture 6a {#slide-1-systems-for-information-managementlecture-6a}

### Content

- Dr Imran U Khan		School of Engineering and Informatics

---

## 2. Previously {#slide-2-previously}

### Content

- Data, Databases, and some modelling
- Introduction to databases & DBMS
- Database architecture & roles
- Data independence
- Database languages
- Conceptual database modelling

- 2

---

## 3. Today {#slide-3-today}

### Content

- More database modelling
- Recap and brief overview of database models and -mapping
- Relations and candidate keys
- Attribute domains
- Transition from conceptual (ERM) to relational (Data tables)
- Further modelling aspects
- Entities: weak , associative , and strong entities
- Attributes: simple , composite , derived , and multi-valued attributes
- Relationships: participation constraints , recursive relationships

- 3

---

## 4. Recap {#slide-4-recap}

### Content

- Conceptual model / schema
We begin the modelling process by representing the data requirements of the organisation in a conceptual schema, based on entity types, attributes, and relationship types.This is a conceptual model – it does not describe how the data will be stored.

- Student

- Name

- Candidatenumber

- Course

- studies

- Title

- Code

- 1

- n

- 4

---

## 5. Recap {#slide-5-recap}

### Content

Recap

Relational model / schema

The conceptual schema is then mapped to a relational schema, and the entities, attributes, and relationships represented as two-dimensional data tables.

Students

Courses

Each table has a name

Columns

Rows

Some information may be shared between tables

5

### Visual Analysis

# Relational Model and Schema

## Conceptual to Relational Schema Mapping

The conceptual schema is transformed into a relational schema, where database entities, attributes, and relationships are represented as two-dimensional data tables.

## Structure of Relational Tables

### Table Components

- **Table Name**: Each table has a unique identifier (e.g., Students, Courses)
- **Columns**: Represent attributes or fields of the entity
- **Rows**: Represent individual records or instances of the entity

### Data Relationships

Information can be shared between tables, enabling relationships between different entities. This sharing typically occurs through common fields (foreign keys) that link related data across tables.

## Example Entities

- **Students** table: Contains student-related information
- **Courses** table: Contains course-related information

These tables can be connected through shared information to represent relationships such as student enrollments in courses.

---

## 6. Relations {#slide-6-relations}

### Content

Relations

Basic anatomy of a data table

The way a user sees the data in a database is as a set of data tables. These tables are also called relations.

This is a relation (students)

These are attributes of the relation

These are records (also called tuples)

The cardinality of a relation corresponds to the number of distinct tuples in that relation.

This is different from the cardinality of a relationship!

The number of attributes in a relation is called the degree of that relation.

6

### Visual Analysis

# Relations in Databases

## Definition
In a database, a **relation** is a data table as seen by the user. Relations are the fundamental structure for organizing data.

## Components of a Relation

### Attributes
The columns of a relation, representing the properties or characteristics of the data being stored.

### Records (Tuples)
The rows of a relation, representing individual instances or entries of data. Each tuple contains values for all attributes in the relation.

## Key Measurements

### Cardinality of a Relation
The total number of distinct tuples (rows) in a relation.

**Important distinction:** The cardinality of a relation is different from the cardinality of a relationship (which refers to the numerical relationship between entities in an entity-relationship model).

### Degree of a Relation
The number of attributes (columns) in a relation.

## Example Structure
Using a "students" relation as an example:
- The relation name: students
- Contains multiple attributes (columns defining student properties)
- Contains multiple records/tuples (individual student entries)
- Cardinality = count of student records
- Degree = count of attribute columns

---

## 7. Candidate keys {#slide-7-candidate-keys}

### Content

- Keys revisited
We already introduced the concept of primary keys and foreign keys informally.
Formally, a candidate key C for a relation R is a subset of the attributes of R such that
No two distinct tuples of R have the same value of C (uniqueness)
No proper subset of C has the uniqueness property (irreducibility).
Every relation must have at least one candidate key. This could be the set of all attributes but most often it’s just one or two attributes.
If a candidate key involves more than one attribute, that makes it a composite key.
One candidate key is the primary key and other candidate keys may be alternate keys.
A foreign key is a subset of attributes which matches a candidate key (usually the primary key) in another relation.

- No duplicate tuples in R

- Keys must be lean

- 7

---

## 8. Candidate keys {#slide-8-candidate-keys}

### Content

Candidate keys

Keys revisited

A relation normally has a primary key, and relationships are encoded by sharing that key with other relations.

Students

Courses

What are candidate keys in these relations?

Which would you choose as primary keys?

What are foreign keys here?

8

### Visual Analysis

# Candidate Keys

## Core Concepts

### Keys in Relational Databases

Relations (tables) typically have a **primary key** that uniquely identifies each record. Relationships between relations are established by sharing these keys with other relations.

### Candidate Keys

A **candidate key** is an attribute or minimal set of attributes that can uniquely identify each tuple (row) in a relation. Key characteristics:
- Must uniquely identify every record
- Must be minimal (no unnecessary attributes)
- A relation can have multiple candidate keys
- One candidate key is chosen as the primary key

## Key Analysis Questions

When examining the Students and Courses relations, three fundamental questions must be addressed:

1. **What are the candidate keys?** - Identify all possible attributes or attribute combinations that could uniquely identify records

2. **Which candidate key should be chosen as the primary key?** - Select the most appropriate candidate key based on:
   - Simplicity
   - Stability (unlikely to change)
   - Meaningfulness to the domain
   - Size/efficiency

3. **What are the foreign keys?** - Identify attributes that reference primary keys in other relations, establishing relationships between tables

## Relationship Encoding

Foreign keys serve as the mechanism for encoding relationships between relations. A foreign key in one table references the primary key of another table, creating a link between related data.

---

## 9. Domains {#slide-9-domains}

### Content

Domains

Attributes have domains

The value of an attribute corresponds to a pre-defined domain for that attribute.
Domains may be standard built-in types such as INTEGER and FLOAT
Domains may also be user-defined e.g., COLOUR = {Red, Green, Blue, Orange, Yellow}
The relational approach constrains each attribute to being an atomic value. That means values cannot be lists or tuples!

This could possibly be split into separate attributes

Not an atomic value!

9

### Visual Analysis

# Attribute Domains in Relational Databases

## Definition

Attributes have domains - the value of an attribute must correspond to a pre-defined domain for that attribute.

## Types of Domains

### Built-in Standard Types
- INTEGER
- FLOAT

### User-Defined Types
Custom domains can be created with specific allowed values.

**Example:**
```
COLOUR = {Red, Green, Blue, Orange, Yellow}
```

## Atomic Value Constraint

The relational approach enforces that each attribute must contain an atomic value.

### What This Means
- Values cannot be lists
- Values cannot be tuples
- Each attribute must hold a single, indivisible value

### Design Implication
If you need to store multiple related values, they should be split into separate attributes rather than stored as a list or tuple in a single attribute.

---

## 10. Mapping of conceptual to relational model {#slide-10-mapping-of-conceptual-to-relational-model}

### Content

- How to get your data model into the database
It is not possible to store a conceptual ER model in the database
We need to map the conceptual schema to a relational schema whilst trying not to lose any of the information that has been modelled
- Some basic rule-of-thumb guidelines to start:
- Create a relation for each entity type (table)
- Create relation attributes for each proper atomic entity attribute (columns)
- Define the domain for each attribute
- Determine candidate keys for each relation

- 10

---

## 11. Mapping of conceptual to relational model {#slide-11-mapping-of-conceptual-to-relational-model}

### Content

- Example

- Student

- Name

- Candidatenumber

- Course

- studies

- Title

- Code

- 1

- n

- STUDENT (
- Name: char(80),
- CandidateNumber: int(6),
- Course: courseCode NOT NULL,
- PRIMARY KEY (CandidateNumber)
- FOREIGN KEY (Course) REF COURSE.Code
- )

- COURSE (
- Title: char(50),
- Code: courseCode,
- PRIMARY KEY (Code)
- )

- 11

---

## 12. Weak and strong entities {#slide-12-weak-and-strong-entities}

### Content

Weak and strong entities

What’s the difference?

Strong entities are independent of others – they are described by their own attributes
Weak entities can only exist in the context of other entities – they are dependent.Here, the weak entity needs a strong entity to define an attribute, it cannot exist without it. Weak entities normally don’t have primary keys. The key in a weak entity is called “discriminator”.

Strong entity

Weak entity – depends on Person

“Discriminator”

12

### Visual Analysis

# Weak and Strong Entities

## Strong Entities

Strong entities are **independent** of other entities in a database. They possess the following characteristics:

- Can exist on their own without depending on other entities
- Described completely by their own attributes
- Have their own primary keys that uniquely identify each instance

## Weak Entities

Weak entities are **dependent** entities that cannot exist independently. Key characteristics include:

- Can only exist in the context of other entities (specifically, strong entities)
- Depend on a strong entity to be fully defined
- Cannot exist without their associated strong entity
- Do not have traditional primary keys

## Discriminator

In weak entities, the key attribute is called a **discriminator** (also known as a partial key). This distinguishes it from a standard primary key because:

- It only provides partial identification
- It must be combined with the strong entity's key to uniquely identify the weak entity instance

## Relationship Between Strong and Weak Entities

A weak entity requires a strong entity for its definition. The weak entity's existence is entirely dependent on the strong entity to which it is related.

**Example conceptual relationship:**
- Strong entity: Person
- Weak entity: A dependent entity that relies on Person (such as a dependent family member or a person's credentials)
- The weak entity cannot exist in the database without its corresponding Person record

---

## 13. Weak and strong entities {#slide-13-weak-and-strong-entities}

### Content

Weak and strong entities

In the relational schema, we need to resolve Many-Many relationships

We already mentioned this briefly in the previous lecture. It is not possible to represent n:m relationships effectively using two relations alone.
Try to set up a relationship between student and course where a student could take many courses and the other way around. For example:

Duplicate PK!

What if we used a composite key instead?!

Redundancy!

Students

Courses

13

### Visual Analysis

# Weak and Strong Entities

## Resolving Many-Many Relationships in Relational Schema

Many-to-many (n:m) relationships cannot be represented effectively using only two relations in a relational database. This is a fundamental constraint that must be addressed in database design.

## Problem Illustration: Student-Course Relationship

Consider a scenario where:
- A student can take many courses
- A course can have many students

### Issues with Direct Implementation

**Problem 1: Duplicate Primary Key**
When attempting to store multiple courses for a student (or multiple students for a course) in a single table, the primary key constraint is violated because the same key value would need to appear multiple times.

**Problem 2: Data Redundancy with Composite Keys**
If a composite key approach is attempted (combining student and course identifiers), significant data redundancy occurs. Student information must be repeated for each course they take, and course information must be repeated for each enrolled student.

## Resolution Required

The structural problems with both approaches demonstrate why many-to-many relationships require an intermediate solution (typically a junction/bridge table) to properly model the relationship in a relational database without violating normalization principles or creating data integrity issues.

---

## 14. Associative entities {#slide-14-associative-entities}

### Content

Associative entities

In the relational schema, we need to resolve Many-Many relationships

The solution lies in using an additional weak entity (also called associative entity)
In the relational mapping, a relation is “inserted” between the two relations that have an n:m relationship

Courses

Students

Enrolment

Foreign keys

many

many

14

### Visual Analysis

# Associative Entities

## Definition and Purpose

**Associative entities** (also called weak entities) are database structures used to resolve many-to-many (M:N) relationships in relational schemas.

## The Problem

In relational databases, many-to-many relationships cannot be directly implemented between two entities. A resolution mechanism is required.

## The Solution

An additional relation is inserted between the two entities that have an n:m relationship. This intermediate relation serves as a bridge connecting the two original entities.

## Implementation in Relational Mapping

The associative entity creates a new relation that contains:
- Foreign keys referencing both original entities
- Any additional attributes specific to the relationship itself

## Example: Students and Courses

**Scenario:** Students can enroll in many courses, and courses can have many students enrolled.

**Original entities:**
- Students (many)
- Courses (many)

**Associative entity:**
- Enrolment

**Structure:**
- The Enrolment entity contains foreign keys referencing both Students and Courses
- This breaks the many-to-many relationship into two one-to-many relationships:
  - One Student can have many Enrolments
  - One Course can have many Enrolments

This approach allows the relational database to properly model the many-to-many relationship while maintaining referential integrity.

---

## 15. Associative entities {#slide-15-associative-entities}

### Content

- In the relational schema, we need to resolve Many-Many relationships
When a weak entity is used, it is mandatory for it to participate in the relationships that identify the attributes required for a record to exist (more on this later).

- 15

- Student

- Name

- Candidatenumber

- Course

- Title

- Code

- takes

- Enrolment

- offers

- n

- n

- 1

- 1

- Weak (associative) entity

- “Identifying”relationships

---

## 16. Associative entities {#slide-16-associative-entities}

### Content

- In the relational schema, we need to resolve Many-Many relationships
In ERM, there is a dedicated associative entity that implements this idea, and there is also a dedicated symbol used in the diagram for it.

- 16

- Student

- Name

- Candidatenumber

- Course

- Title

- Code

- Enrolment

- n

- n

- 1

- 1

- “Associative entity”

---

## 17. Attributes {#slide-17-attributes}

### Content

Attributes

Simple vs composite attributes

Simple attributes can’t be decomposed up any further
Alternatively, the requirements may not demand a finer granularity is necessary

Students

This might be intentional design, or not!

17

### Visual Analysis

# Simple vs Composite Attributes

## Definition

**Simple attributes** are attributes that cannot be decomposed any further into smaller meaningful components.

## Key Considerations

- Simple attributes represent atomic data elements that are treated as indivisible units
- The decision to use simple attributes may be driven by requirements that do not demand finer granularity
- Whether an attribute is considered simple can be an intentional design choice based on the system's needs

## Design Implications

The simplicity of an attribute may result from:

1. **Intentional design decision** - deliberately choosing not to break down an attribute because the system doesn't need more detailed information
2. **Unintentional oversight** - the design may not have considered whether further decomposition would be beneficial

## Context

This concept relates to the distinction between simple and composite attributes in data modeling, where composite attributes can be broken down into sub-attributes (e.g., a "Name" attribute could be decomposed into "FirstName" and "LastName"), while simple attributes remain indivisible.

---

## 18. Attributes {#slide-18-attributes}

### Content

Attributes

Simple vs composite attributes

Composite attributes are translated as component attributes in the relational model






Composite attributes are not directly specifiedin the relation, but their components are!

Students

Student

Name

Candidatenumber

Firstname

Lastname

18

### Visual Analysis

# Composite Attributes in the Relational Model

## Definition

**Composite attributes** are attributes that can be divided into smaller sub-parts, each representing a more basic attribute with independent meaning.

## Translation to Relational Model

When converting from conceptual models (like ER diagrams) to the relational model:

- Composite attributes are **not specified directly** in relations
- Instead, their **component attributes** are specified individually
- Each component becomes a separate column in the table

## Example: Student Name

A composite attribute `Name` can be broken down into:
- `Firstname`
- `Lastname`

### Relational Schema Implementation

**Students** relation structure:
- `Candidatenumber` (identifier)
- `Firstname` (component of Name)
- `Lastname` (component of Name)

The composite attribute "Name" does not appear as a single column. Instead, the table contains separate columns for its components: Firstname and Lastname.

## Contrast with Simple Attributes

**Simple attributes** cannot be divided into smaller meaningful parts and are stored directly as single columns in the relation.

---

## 19. Attributes {#slide-19-attributes}

### Content

Attributes

Derived attributes

In the conceptual model derived attributes are those whose value is the result of performing some computation over other attribute values, for example:
Derived attributes do not appear in the relation

19

Course

Spacesleft

Coursecode

title

Courses

Student count

### Visual Analysis

# Derived Attributes

## Definition

Derived attributes are attributes whose values are calculated by performing computations over other attribute values, rather than being stored directly.

## Key Principle

**Derived attributes do not appear in the relation** (i.e., they are not stored in the database tables)

## Example: Course Management

### Scenario Components

- **Course** entity with attributes:
  - Coursecode
  - Title
  - Student count

- **Derived Attribute**: `Spacesleft`

### How it Works

`Spacesleft` is computed by subtracting the current student count from the maximum course capacity, rather than being stored as a separate field in the Courses table.

## Rationale

Derived attributes are excluded from physical database relations because:
- Their values can be calculated on-demand from existing data
- Storing them would create data redundancy
- Maintaining synchronized derived values adds complexity and potential for inconsistency
- They appear in conceptual models to document business logic but are implemented through queries or application code

---

## 20. Attributes {#slide-20-attributes}

### Content

Attributes

Multi-valued attributes

Multiple values for attributes? That’s not allowed in a relation!
Hence, multi-valued attributes require an extra relation to be defined
Example:

20

Person

Person_emails

Person

Emails

Name

Person_id

### Visual Analysis

# Multi-valued Attributes in Relational Databases

## Core Concept

Multi-valued attributes cannot be stored directly in a relation. Relations in relational databases require atomic (single) values in each field, not multiple values.

## Solution: Separate Relation

Multi-valued attributes require an extra relation to be defined. This involves creating a separate table to store the multiple values.

## Example Implementation

### Original Entity
**Person** with a multi-valued email attribute

### Normalized Structure

**Person Table:**
- Person_id
- Name

**Person_emails Table:**
- Person_id
- Emails

The Person_emails table serves as a bridge to store multiple email addresses for each person. Each email becomes a separate row in the Person_emails table, linked to the corresponding Person_id.

## Key Principle

This approach follows database normalization rules, ensuring that each attribute contains only a single value while still allowing entities to have multiple values for certain attributes through a one-to-many relationship.

---

## 21. Relationships {#slide-21-relationships}

### Content

- Participation constraints
- Entities “participate“ in relationships, and sometimes participation is total, e.g.:

- 21

- Student

- Name

- Candidatenumber

- Course

- studies

- Title

- Code

- 1

- n

- STUDENT (
- Name: char(80),
- CandidateNumber: int(6),
- course_id: courseCode NOT NULL,
- PRIMARY KEY (CandidateNumber)
- FOREIGN KEY (course_id) REF COURSE.Code
- )

- COURSE (
- Title: char(50),
- Code: courseCode,
- PRIMARY KEY (Code)
- )

course_id must not be “NULL” when a student “studies” on a course

---

## 22. Relationships {#slide-22-relationships}

### Content

- Participation constraints
Entities “participate“ in relationships, and for some participation is partial, e.g.:

- 22

- Student

- Name

- Candidatenumber

- Course

- studies

- Title

- Code

- 1

- n

- STUDENT (
- Name: char(80),
- CandidateNumber: int(6),
- course_id: courseCode NOT NULL,
- PRIMARY KEY (CandidateNumber)
- FOREIGN KEY (course_id) REF COURSE.Code
- )

- COURSE (
- Title: char(50),
- Code: courseCode,
- PRIMARY KEY (Code)
- )

Not every COURSE entity needs to participate in studies in order to exist

---

## 23. Relationships {#slide-23-relationships}

### Content

- Recursive relationships
An entity participates in more than one relationship type, usually if instances of the entity can have different “roles”
In the relational schema, this can be mapped using either one or two relations:
- Add an “assessor_id” to the student relation.or
Create a “Peer Assessment” relation that matches “assessor_id” and “cand_no”.

- 23

- Student

- peer-assesses

- assessor

- assessed

---

## 24. Read {#slide-24-read}

### Content

Connolly and Begg, Database Systems: A Practical Approach to Design, Implementation, and Management, Pearson Ed.
- Chapter 4 – The relational model
- Chapter 12 – ER modelling
- 12.4 Strong and Weak Entity Types
- 12.5 Attributes on Relationships
- 12.6 Structural Constraints
- 12.7 Problems with ER Models

- 24

---

## 25. Next Lecture {#slide-25-next-lecture}

### Content

Next Lecture

Normalisation of database relations
1NF, 2NF, 3NF

25

### Visual Analysis

# Database Normalisation Preview

## Upcoming Topics

The next lecture will cover **Normalisation of database relations**, which includes three key normal forms:

### Normal Forms to be Covered

- **1NF** (First Normal Form)
- **2NF** (Second Normal Form)  
- **3NF** (Third Normal Form)

## Context

Normalisation is a systematic approach to organizing data in databases to reduce redundancy and improve data integrity. These three normal forms represent progressive levels of database optimization, each building upon the previous form to create more efficient and maintainable database structures.

---


---

## Processing Metadata

### Slide Classification
- Text slides: 13
- Visual slides: 12
- Optimized percentage (without API): 52.0%

### API Costs
- Input tokens: 101,851
- Output tokens: 22,672
- Total cost: $0.6456 USD

### System
- Generated by: PPTX to Markdown Converter
- Date: 2026-01-11 19:15:03