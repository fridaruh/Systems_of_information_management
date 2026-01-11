# SIM   L05a


## Systems for Information Management


- Dr. Imran Khan			School of Engineering and Informatics

---

## Previously


- Computing Basics, Content description, Programming
- Computer systems
- Networks and the Internet
- HTML, XML
- Client-side scripting

---

## Today


- Data & Databases
- Introduction & a few basic concepts
- Definition & Examples
- Overview of basic database operations
- Database management systems and their characteristics
- Advantages of databases over files

---

## Data


- We are getting swamped by data
Databases are all around us and the amount of data produced and collected is constantly growing
Photos, videos (~100m photos are shared on the Web every day)
- Communication data (e.g., 5m tweets and 300b e-mails per day)
- IoT (Internet of things), sensors, mobile phones
A lot of data is being produced not directly by humans, but by machines!
Google’s web database is estimated to have a size of….

- 10 Exabyte

---

## Data


- We are getting swamped by data
- 10 Exabyte are 10 million Terabyte
- 1000 Gigabytes = 1 Terabyte
- 1000 Terabytes = 1 Petabyte
- 1000 Petabytes = 1 Exabyte
- 1000 Exabytes = 1 Zettabyte

- 1,000 copies of the Encyclopedia
- Britannica

20 million 4-drawer filing cabinets full of text.

5 Exabyte equal to all information produced by humans since the dawn of time until 2002.

In 2018, global data was estimated to have reached 33 Zettabytes, growing exponentially

---

## Databases


What is a database?

- “a usually large collection of data organized especially for
- rapid search and retrieval (as by a computer ) ”
- (Merriam-Webster Dictionary)
- “a shared collection of logically related data, and a
description of this data, designed to meet the information needs of an organization”
- (Connolly & Begg: “Database Systems”)

---

## Databases


What is a database?

- “a shared collection of logically related data, and a
description of this data, designed to meet the information needs of an organization”
- (Connolly & Begg: “Database Systems”)

- Multiple users access the data

- The data is structured, and this structure is well-defined

There is a design process that models requirements to determine the way in which the data needs to be structured and made accessible

---

## Database Modelling


- Entities and their relationships
“Relational” database management systems (RDBMS) are the most ubiquitous and mature type of database technology available today, although there are other kinds of database systems for specific purposes (e.g., NoSQL).
The design of a relational database is usually based on the modelling of an organisation’s entities, those entities’ attributes, and the relationships between different entities.
The resulting Entity-Relationship (ER) models are a common type of data model
Data models provide an input for practical database design, where the conceptual structure then needs to be mapped to appropriate data structures (e.g., relational data tables)

- We are going to talk more about this tomorrow

---

## Database Examples


- Examples
- A Human Resources department maintaining a database of employees
- A bank keeping data about customers, accounts and balances
An online retailer managing product stock, sales, and transactions; as well as customer accounts, purchases, and marketing preferences
- Scientific databases, such as those that store DNA sequences
The University keeps all students records and their marks in a database!

---

## Database Operations


- Basic database operations
- Data structure creation
- Define and specify the structural elements of a database
- Create and populate these data structures
- Data manipulation
- Create, read, update, delete data
- Find specific data (query)
- Parse and filter data for different purposes (reporting)

- Database operations are handled by a database management system

---

## “a software system that enables users to define, create, maintain, and control access to the database”
(Connolly & Begg: “Database Systems”)


What is a Database Management System?
The DBMS provides its functionality not just to users directly, but clients more generally (other software) and mediates access to the data
Examples of well-known DBMS brands: Microsoft SQL Server, IBM DB2, MySQL, Oracle Database, PostgreSQL

- Database Management

---

## Database System


- Actual Data

- DatabaseDefinition

- “Data dictionary”, or “Catalogue”

- DBMS
- Handle
- queries and provide views
- Data access control
- Dataconsistency enforcement

- Client
- CreateReadUpdateDelete

- Overview of a database system

---

## Why not just use files?

File systems provide direct physical access to data
Advantages
Simple
Cheap (already available)
Reliable


- Comparison to file storage

- Disadvantages
- Data duplication possible, which may lead to inconsistencies
- No enforcement of consistency rules
- Many incompatible file formats
- Poor performance for updates in large files
- Poor performance of search
- Access happens at file level, not record level
- No support for concurrent transactions

---

## Comparison to file storage


- Databases have many advantages
- Database systems provide data access through a logical interface
- Some of the advantages
- We can represent complex relationships between data
- Data is kept separate from structure
- Better control of data redundancy
- Avoidance of consistency problems
- More flexible access for multiple clients
- Better security and access control
- Better handling of “big” data

- Disadvantages
- Databases require additional hardware and software
- Databases can be complex to set up
- Some applications work faster with files
Databases can incur significant running cost (although this may be offset by the efficiency gains of logical data access)
Greater vulnerability to failure (although this is compensated through other technologies, such as replication and fail-over clusters)

---

## Read


Connolly and Begg, Database Systems: A Practical Approach to Design, Implementation, and Management, Pearson Ed.
- 1.1 Introduction
- 1.2 Traditional File-Based Systems
- 1.3 Database Approach
- 1.6 Advantages and Disadvantages of DBMSs

---

## Next Lecture


- Overview of the database environment
- Data independence
- Database languages
- Conceptual database modelling

---
