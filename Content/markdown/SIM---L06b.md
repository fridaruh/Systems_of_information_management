# SIM   L06b


## Systems for Information ManagementLecture 6b


- Dr Imran U Khan		School of Engineering and Informatics

---

## Previously


- More database modelling
- The relational model
- Mapping the conceptual (ERM) to the relational model (Data tables)
- Further modelling aspects
- Relations and candidate keys
- Attribute domains
- Entities: weak , associative , and strong entities
- Attributes: simple , composite , derived , and multi-valued attributes
- Relationships: participation constraints , recursive relationships

---

## Today


- Normalisation
How to create data structures that avoid redundancies and enable data independence through normalisation
- 1st – 3rd normal form
- Basic modelling tips
- Non-normalised databases

---

## Recap


Recap

Database modelling

We learnt that database modelling involves creating a conceptual model and then mapping this into a logical (relational) model – our database tables.
We know the basics of how to map entities & attributes, and how to model relations between entities by using keys and associative entities, for example. But how do we know which attributes need to go into which tables, and how many tables we need? And how can we check for redundancies in our model?


# Database Modelling Process

## Two-Stage Modelling Approach

Database modelling consists of two main phases:

1. **Conceptual Model Creation**: Developing an abstract representation of the data and relationships
2. **Logical Model Mapping**: Converting the conceptual model into a relational database structure with specific tables

## Core Mapping Techniques

### Basic Elements
- **Entities** are mapped to database tables
- **Attributes** become columns within those tables
- **Relations between entities** are represented through:
  - Primary keys
  - Foreign keys
  - Associative entities (for many-to-many relationships)

## Key Design Challenges

### Attribute Distribution
- Determining which attributes belong in which tables
- Ensuring proper data organization across the database structure

### Table Quantity
- Deciding the optimal number of tables needed
- Balancing normalization with practical usability

### Redundancy Detection
- Identifying and eliminating duplicate data storage
- Checking for inefficiencies in the database model
- Ensuring data integrity through proper table structure

---

## Normalisation


What is normalisation?
- Normalisation is a design methodology for creating relational schemas
Starting from an initial set of relations (our first mapping attempt), we analyse the dependencies between relations and especially the attributes specified within them and optimise the relational schema, to reduce redundancy, and avoid anomalies.

---

## Normalisation


What can happen if we don’t normalise a database?
- Redundancy
If the same data is stored in multiple places, this can lead to inconsistencies when the data needs to be updated.
Database size may be unduly high because more data gets physically stored than would be necessary.
Performance may be poor if what could be simple data operations need to be performed multiple times, and according to complex rules.
- Anomalies
There can be various problems when we try and insert data into, update data in, or delete data from a non-normalised database. For example, deleting a record in one data table may lead to certain attributes being lost completely, even though they may still be needed by other relations.

---

## Normalisation


Normalisation

How does normalisation work?

Normalisation is a multi-stage process of restructuring the relational schema to produce intermediate database states that are called “Normal Forms”
Normalisation changes a relational schema to conform with one or more normal forms. First normal form (1NF) is the most important. Achieving 2NF and 3NF is common.
Each normalisation step will make the data less redundant and more independent but will also increase the number of relations specified in the database.


# Normalisation

## Definition and Purpose

Normalisation is a multi-stage process of restructuring the relational schema to produce intermediate database states called "Normal Forms".

## How Normalisation Works

- Changes a relational schema to conform with one or more normal forms
- Progresses through sequential normal forms, each with stricter requirements
- First Normal Form (1NF) is the most important foundational level
- Achieving Second Normal Form (2NF) and Third Normal Form (3NF) is common practice in database design

## Effects of Normalisation

**Benefits:**
- Reduces data redundancy at each step
- Increases data independence
- Improves data integrity

**Trade-offs:**
- Increases the number of relations (tables) specified in the database
- Each normalisation step adds more structural complexity through additional tables

---

## Normalisation


- 1NF
- Fixes the most important issues
- Activities:
- Create relations for all entities
Identify candidate keys for all entities so that records can be uniquely identified
- Attributes should describe the key attribute
- Rule: Attributes must have atomic values only

---

## Normalisation


- 1. Move multi-value
- group to a new relation

- 2. Copy original key attribute
- to new relation

- 3. Remaining
- attributes
- left in the original relation

- Start:
- 1NF:

---

## Normalisation


- 2NF
This normal form resolves partial dependencies when a relation has a composite key
- Requires 1NF as input
Rule: Every attribute in a relation must describe the key attribute in its entirety (not just one part of the key)
Common case: check if the attributes in an associative entity depend on all key attributes defined for the entity

---

## Normalisation


- 1NF:
- 2NF:

- 1. Move part-key dependencies to a new relation

- 2. Copy relevant key part
- to new relation

- 3: Remaining
- attributes left
- in original relation

---

## Normalisation


- 3NF
- The third normal form is about eliminating transitive dependencies
- Requires 2NF as input
Rule 1: There must be no redundancy such that one attribute depends on another within the same entity, even though both may describe the primary key attribute
Rule 2: Clean-up. Remove any attributes that are derived or composites (these should not have been translated in the first place)

---

## Normalisation


- 2NF
- 3NF

- 1: Move non-key
- dependencies to a new relation)

- 2: Copy identity attribute to the
- new relation

- 3. Remaining attributes left in original relation

- 3: Remove any derived attributes

---

## Modelling tips


How to reduce the need for extensive normalisation (and save time)
- Identify entity types by searching for nouns and noun phrases
Assume that all entities are strong and check if any are weak afterwards
- Avoid redundancy by not duplicating attributes between relations, if possible
Check if an attribute may qualify as an entity but only create an entity if:
It is more than a label, which means it has further non-key attributes or relationships
- It is the “many” in a many-to-one relationship
Assume that all relationships have partial participation and check for total afterwards
It is normal that your initially specified set of entities, attributes, and relationships may change throughout the modelling process – expect it to happen.

---

## Non-normalised databases


- NoSQL (not-only SQL)
One aim of database design is to deliver best-possible performance, and we sometimes need to balance functionality and efficiency to determine the optimal level of structural complexity to impose on the database. (E.g., the number of relations)
The relational approach has many obvious benefits but can be difficult to use when we need to handle large volumes of data that change a lot and are difficult to structure.
Non-relational, NoSQL database approaches involve the use of graphs, or less restrictive schemas such as associative arrays that store key-value pairs, for example.
This can be useful if there is significant computational power outside of the database system and if the data is mainly read and not updated or deleted in the database

---

## Read


Connolly and Begg, Database Systems: A Practical Approach to Design, Implementation, and Management, Pearson Ed.
- Chapter 14: Normalisation up to 3NF
- Chapter 16: Conceptual schema design methodology
- Chapter 17: Logical (relational) schema design methodology

---

## Next Lectures


The SQL query language (You will be getting a preview in the lab)
- Relational algebra

---
