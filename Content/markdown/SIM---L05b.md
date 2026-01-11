# SIM   L05b


## Systems for Information Management


- Dr Imran Khan		School of Engineering and Informatics

---

## Previously


- Data & Databases
- Introduction & a few basic concepts
- Definition & Examples
- Overview of basic database operations
- Database architecture
- Database management systems and their characteristics
- Advantages of databases over files

---

## Today


- The database environment
- The different roles in a database environment
- Database architecture
- Data independence
- Database languages
- Conceptual database modelling

---

## Quick recap


Quick recap

Core characteristics of the database approach

We separate the data and the client(s) using that data with a logical layer (the DBMS) that controls and mediates data access and manipulation
The structure of the data (also called the schema) is defined in a data dictionary


# Database Approach: Core Characteristics

## Separation of Concerns through Layered Architecture

The database approach implements a three-tier separation:
- **Data layer**: The actual data storage
- **DBMS (Database Management System)**: A logical intermediary layer
- **Client layer**: Applications and users accessing the data

## Role of the DBMS

The DBMS acts as a mediator that:
- Controls access to the data
- Manages data manipulation operations
- Provides an abstraction layer between clients and physical data storage

This separation means clients don't interact directly with the data, but rather go through the DBMS.

## Schema and Data Dictionary

**Schema**: The formal structure and organization of the data

**Data Dictionary**: A centralized repository where the schema is defined and stored

The data dictionary contains metadata that describes:
- What data exists in the database
- How the data is organized
- Rules and constraints governing the data
- Relationships between different data elements

---

## Database environment roles


The roles refer to different activities and perspectives on a database
- Designer
Creates data models and maps these to the internal structure of the database system
- Administrator
Technical implementation of the design; Configures access permissions; Day-to-day operation of the database system
- Application developer
Develops software clients that provide an interface for end users to access the data in a database through the DBMS, and that abstracts from the technical details
- End user
Uses a client to access and manipulate data, usually for a specific purpose, and is often deliberately ignorant of the underlying data structures, access controls, etc.

---

## Database architecture


Database architecture

Three-Level ANSI-SPARC Architecture

Image: Connolly & Begg, p.85

End user perspective

Organisational perspective: Entities, attributes, relationships, permissions, etc.

The internal data structures that map the conceptual level and how these are stored, encrypted, etc.


# Three-Level ANSI-SPARC Database Architecture

## Overview
The ANSI-SPARC architecture defines a standardized framework for database systems consisting of three distinct levels of data abstraction.

## The Three Levels

### External Level (End User Perspective)
- Represents how individual users or user groups view the database
- Defines user-specific views of the data
- Different users can have different external views of the same database
- Provides data independence by hiding complexity from end users

### Conceptual Level (Organisational Perspective)
- Represents the logical structure of the entire database for the organization
- Defines:
  - **Entities**: The objects or concepts stored in the database
  - **Attributes**: The properties or characteristics of entities
  - **Relationships**: How entities are connected to each other
  - **Permissions**: Access control and security rules
- Provides a unified view of all data in the database
- Independent of how data is physically stored

### Internal Level (Physical Storage Perspective)
- Represents the physical implementation of the database
- Defines:
  - Internal data structures used to store data
  - Mapping between conceptual schema and physical storage
  - Storage mechanisms (how data is physically stored)
  - Encryption methods for data security
  - Indexing and access paths
  - Compression techniques
- Closest to physical storage hardware

## Purpose and Benefits
- **Data Independence**: Changes at one level do not affect other levels
- **Abstraction**: Each level provides appropriate detail for its audience
- **Flexibility**: Multiple user views can coexist without conflicts
- **Security**: Different access levels can be enforced at different layers

---

## Database schemas


Database schemas

Schemas describe a database

The database schema is the overall description of the database
In practice, there are different sub-schemas (at different levels in the architecture), which together constitute the database schema

Image: Connolly & Begg, p.88


# Database Schemas

## Definition

A **database schema** is the overall description of a database. It defines the structure, organization, and constraints of the data within the database system.

## Schema Composition

In practice, a complete database schema consists of multiple sub-schemas operating at different levels within the database architecture. These sub-schemas work together to form the complete database schema.

## Architectural Levels

Database schemas exist at different levels of the database architecture:

- **External schemas**: Define how different users or applications view the data
- **Conceptual schema**: Provides the logical structure of the entire database
- **Internal schema**: Describes the physical storage and access methods

These layered sub-schemas collectively constitute the overall database schema, allowing for:
- Data independence between levels
- Multiple user views of the same data
- Separation of logical and physical data organization

---

## Data Independence


- Managing change
As opposed to the actual data, we normally do not expect the database schema to change much once it has been designed and implemented.
If there is a change, then data independence means that higher-level schemas are supposed to remain unaffected by changes in lower-level schemas.This is important because client applications depend on the logical layout of the DB.
Logical data independence:Changes at the conceptual level do not (adversely) affect existing external schemas(e.g., when adding or removing new entities, attributes, etc.)
Physical data independence:Changes at the internal (physical) level do not affect the conceptual (logical) level(e.g., changing the way the data is physically stored).

---

## Database languages


Which languages are required?
A Data Definition Language (DDL) to create and modify the database schema
A Data Manipulation Language (DML) to query the data in the database

- Image: Connolly & Begg, p.88

---

## Database languages


- Data Definition Language (DDL)
- Notation for setting up the database schema
Example: Create a table that is then stored in a data dictionary, together with additional parameters such as constraints, or access permissions.
- The data dictionary contains metadata (i.e., information about data structures)

- CREATE table bank-accounts (
- name		char(100),
- account-number	char(12),
- balance		float
- );

---

## Database languages


- Data Manipulation Language (DML)
- Language for accessing and manipulating the data, such as
- creating new records,
- reading specific data
- updating records,
- deleting records)

- SELECT name
- FROM customers
- WHERE country = “France”;

---

## Database languages


- SQL
The structured query language (SQL) is the quasi-standard for performing DDL and DML operations in relational databases.
SQL statements are terminated with a semi-colon (Similar to program instructions in Javascript).
However, implementations of the language can differ slightly between vendors.
The examples shown on the previous two slides were both SQL statements.

---

## Database modelling


- Database design requires models
The data requirements of the organisation drive the development of the conceptual schema (entities, attributes, relationships). This is independent of how the data will be stored physically.

- Student

- Name

- Candidatenumber

- Course

- studies

- Title

- Level

---

## Database modelling


Database modelling

Database design requires different kinds of models

The conceptual schema is then mapped to a relational model, where the data and the relationships are represented as tables.

Students

Courses

Enrolment


# Database Modelling

## Database Design Models

Database design requires different kinds of models to represent data structures and relationships effectively.

## Conceptual to Relational Mapping

The conceptual schema serves as the foundation for database design. This conceptual schema is then mapped to a relational model, which represents both data and relationships using tables.

## Relational Model Structure

In the relational model:
- Data entities are represented as tables
- Relationships between entities are also represented as tables

### Example: Educational Database

Three key tables in an educational database system:

1. **Students** - stores student information
2. **Courses** - stores course information
3. **Enrolment** - represents the relationship between students and courses (which students are enrolled in which courses)

This demonstrates a many-to-many relationship pattern, where:
- Multiple students can enroll in multiple courses
- The Enrolment table acts as a junction/bridge table connecting Students and Courses

---

## Database modelling


Database modelling

Example of a simplerelational model

Image: Connolly & Begg, p.153


# Database Modelling - Relational Model Example

## Overview
This content presents a simple relational database model example, demonstrating how data is organized in a relational database structure.

## Key Concept
**Relational Model**: A database structure that organizes data into tables (relations) with rows and columns, where relationships between different tables are established through common attributes.

## Structure of a Simple Relational Model

The example illustrates fundamental components:

### Tables (Relations)
- Data is stored in tables, each representing an entity type
- Each table has a unique name
- Tables consist of rows (records/tuples) and columns (attributes/fields)

### Attributes
- Columns in a table that define the properties of the entity
- Each attribute has a specific data type

### Primary Keys
- Unique identifiers for records within a table
- Ensure each row can be distinctly identified

### Foreign Keys
- Attributes in one table that reference the primary key of another table
- Establish relationships between tables
- Enable data integrity and linking of related information

## Significance
This simple model demonstrates the foundational principle of relational databases: organizing data into structured tables with defined relationships, which allows for efficient data storage, retrieval, and maintenance while minimizing redundancy.

**Reference**: Connolly & Begg, p.153

---

## Database modelling


- Conceptual modelling with an ERM
The Entity-Relationship-Model (ERM) is a type of data model that considers an organisation as a collection of entities and relationships
Entities are distinguishable objects, elements, things.
Entities can be further described with attributes.
Relationships describe associations between entities.

---

## Database modelling


- Conceptual modelling with an ERM
To create an ER model, we need to start at the problem and find out what the organisational realities and requirements are:
What are the entities in the organisation?
Which relationships exist between the entities?
What information do we want to store about these entities and their relationships?
What rules and constraints can we identify?
For what purposes do we want to use the database?

---

## Database modelling


- Conceptual modelling: Example
Let’s say the University wants to create a database that stores information about the students, the courses, the taught modules, and the teaching staff.
The development of a conceptual model will be driven by the organisational requirements: For example, what are the kinds of queries our database should support?

Find out which staff memberteaches a particular module, for time-tabling purposes.

Find out which students have a poor attendance record, and who the teaching staff are who are responsible for the related modules.

Find out the postal address of a candidate to send them their graduation certificate.

Assign new staff to a school and a department.

Find out which modules a particular student is enrolled in.

Find out how many students are enrolled in the “Medieval English Literature” module.

---

## Database modelling


- Conceptual modelling: Example
The conceptual model needs to reflect the reality of the entities in the organisation, their specific attributes, how they are interrelated, and what the constraints are.
- So, for example:
A student has a name, which consists of one or more given names, and a last name. A student also has a registration number, and a candidate number, and is registered for a course, in a particular year of study. A course can have many students but a student can only be registered for one course full time, and can only be in one specific year of study.
Each course has a number modules. Some of these are core modules, others are options. Students are registered against the modules they need to pass in order to progress in their course.
Modules have a member of staff who is the assessment convenor. This person usually also teaches the module, but there may be other staff members involved in teaching delivery.
Staff members work in a department, which is part of a school. They may teach more than one module in an academic year.

---

## Entity-Relationship Modelling


- Entity
An object that can be distinguished from other objects (like an object in OOP)
An entity is described by a set of attributes (like the data of an object)
- Examples:
- The student “Jacob Smith”
- The course “Medieval English Literature”

---

## Entity-Relationship Modelling


- Entity Type
- A collection of similar entities (e.g., all employees)
All entities in an entity type have the same set of attributes.
Each entity type has a key, (i.e., one or more attributes that uniquely identify and distinguish an entity from others)
Always expressed as a noun.
- Examples:
- Student
- Course

---

## Entity-Relationship Modelling


- Entity-Relationship Diagrams
- ER diagrams are graphical representations of an ER model
- Entity Types are drawn as rectangles
- Attributes are drawn using ovals
- The attribute(s) that make up the unique key are underlined

- Student

- Name

- Candidatenumber

- Student

- Name

- Candidatenumber

- Course

- Title

- Level

---

## Entity-Relationship Modelling


- Relationships and Relationship types
A relationship is an association between two or more entities(e.g., “Jacob Smith” “studies” “Medieval English Literature”)
- Usually expressed as a verb
- Relationships may have attributes
- Relationship types are collections of similar relationships (”studies”)
Drawn as a diamond shape (Chen notation) oras a straight directed line (Crow’s foot notation)

- Student

- Name

- Candidatenumber

- Course

- studies

- Title

- Level

---

## Entity-Relationship Modelling


- Cardinality of relationships
- 1-1
- 1 - Many
- Many - Many
- Example in Crow’s foot notation

---

## Entity-Relationship Modelling


- Cardinality of relationships
- 1-1
- 1 - Many
- Many - Many

- 1

- n

- n

- n

---

## Entity-Relationship Modelling


- Student

- Name

- Candidatenumber

- Course

- studies

- Title

- Level

- Cardinality of relationships

- n

---

## Entity-Relationship Modelling


- About keys
A primary key (PK) is an attribute that can be used to uniquely identify a particular entity.
Where there is a 1-n relationship between different entity types, a reference can be made to entities on the “1” side by using the value of their primary key.  If a key is used to relate to another entity in this way, this key is called a foreign key (FK) (because it was defined somewhere else, and its value will match a primary key there).

- Candidatenumber
- Name
- Title

- Student

- Title
- Level

- Course

- studies

-

---

## Entity-Relationship Modelling


- About keys
If we have a many-to-many relationship, we can resolve this by introducing another entity whose purpose it is to connect the two entities.

- Candidatenumber
- Name

- Student

- Title
- Level

- Course

- studies

-

-

- This doesn’t work

---

## Entity-Relationship Modelling


- About keys
If we have a many-to-many relationship, we can resolve this by introducing another entity whose purpose it is to connect the two entities.

- Candidatenumber
- Name

- Student

- Title
- Level

- Course

- Enrolment ID
- Title
- CandidateNumber

- Enrolment

- 1

-

-

- has

- makes

---

## Read


Connolly and Begg, Database Systems: A Practical Approach to Design, Implementation, and Management, Pearson Ed.
- 1.4 Roles in the Database Environment
- 2.1 The Three-Level ANSI-SPARC Architecture
- 2.2 Database Languages
- 2.3 Data Models and Conceptual Modelling
- 12.1, 12.2, 12.3  Basics of ER Modelling

---

## Next Lectures


Next Lectures

The relational model
SQL query language



# Upcoming Topics in Information Systems Course

## Future Lecture Topics

The course will continue with the following subjects:

### The Relational Model
- Foundational database model for organizing and structuring data
- Study of how data is represented in tables (relations)
- Understanding of relationships between data entities

### SQL Query Language
- Structured Query Language for database operations
- Techniques for retrieving, manipulating, and managing data in relational databases
- Writing queries to interact with database systems

---
