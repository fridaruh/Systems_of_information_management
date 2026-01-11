# SIM   L04b

**Conversion date:** 2026-01-11
**Original file:** `SIM - L04b.pptx`
**Total slides:** 22

---


## Table of Contents

1. [Systems for Information Management](#slide-1-systems-for-information-management)
2. [Previously](#slide-2-previously)
3. [Today](#slide-3-today)
4. [Object-Orientation](#slide-4-object-orientation)
5. [Object-Orientation](#slide-5-object-orientation)
6. [Objects and Classes](#slide-6-objects-and-classes)
7. [Objects and Classes](#slide-7-objects-and-classes)
8. [Objects and Classes](#slide-8-objects-and-classes)
9. [Objects and Classes](#slide-9-objects-and-classes)
10. [Objects and Classes](#slide-10-objects-and-classes)
11. [Objects and Classes](#slide-11-objects-and-classes)
12. [Objects and Classes](#slide-12-objects-and-classes)
13. [Objects and Classes](#slide-13-objects-and-classes)
14. [Objects and Classes](#slide-14-objects-and-classes)
15. [Objects and Classes](#slide-15-objects-and-classes)
16. [Objects and Classes](#slide-16-objects-and-classes)
17. [Objects and Classes](#slide-17-objects-and-classes)
18. [Objects and Classes](#slide-18-objects-and-classes)
19. [Objects and Classes](#slide-19-objects-and-classes)
20. [Objects and Classes](#slide-20-objects-and-classes)
21. [Practice](#slide-21-practice)
22. [Next Lectures](#slide-22-next-lectures)

## 1. Systems for Information Management {#slide-1-systems-for-information-management}

### Content

- Dr Imran U Khan		School of Engineering and Informatics

---

## 2. Previously {#slide-2-previously}

### Content

- More basic programming concepts
- Functions
- Events

- <script type=“text/javascript”>
- some_instruction;
- myFunction();
- another_instruction;
...
- function myFunction() {
- // do stuff
- return something;
- }
- </script>
...
- <button onclick=“myFunction()”><button>
...

---

## 3. Today {#slide-3-today}

### Content

- More basic programming concepts
- Discussion of previous lab exercises:
- Fibonacci numbers
- Two-dimensional arrays
- Object orientation
- Objects in Javascript and how to use them

---

## 4. Object-Orientation {#slide-4-object-orientation}

### Content

Object-Orientation

The object-oriented paradigm models the world as sets of objects that each have particular attributes and exhibit certain behaviour.
Example: A gift shop

Real-world 
problem domain

Abstract
Conceptualisation

Computer Model

Product

Customer

Calendar

Landscapes Calendar

Cats Calendar

T-Shirt

Price

Shopping Basket

is a

is a

has

is a

buys

goes into

Product {
    price
    name
    set_price(p)
}

ShoppingBasket {
    itemCount
    Product items[]
...
}

is a

### Visual Analysis

# Object-Oriented Paradigm

## Core Definition

The object-oriented paradigm models the world as sets of objects that each have:
- **Attributes**: Particular characteristics or properties
- **Behaviour**: Specific actions or methods they can perform

## Conceptual Process

The object-oriented approach follows three stages:

1. **Real-world problem domain** - The actual business or system being modeled
2. **Abstract Conceptualisation** - Identifying entities and their relationships
3. **Computer Model** - Implementation in code

## Example: Gift Shop System

### Domain Entities and Relationships

**Product Types:**
- Calendar (general category)
  - Landscapes Calendar (specific type)
  - Cats Calendar (specific type)
- T-Shirt

**Core Concepts:**
- Product (parent class with Price attribute)
- Customer
- Shopping Basket

**Relationships:**
- Calendar "is a" Product
- Landscapes Calendar "is a" Calendar
- Cats Calendar "is a" Calendar
- T-Shirt "is a" Product
- Customer "buys" Product
- Product "goes into" Shopping Basket
- Product "has" Price

### Code Implementation

```
Product {
    price
    name
    set_price(p)
}

ShoppingBasket {
    itemCount
    Product items[]
    ...
}
```

## Key Concepts Illustrated

- **Inheritance**: Using "is a" relationships to create hierarchies (e.g., Calendar is a Product)
- **Attributes**: Data stored within objects (price, name, itemCount)
- **Methods**: Functions that operate on objects (set_price)
- **Composition**: Objects containing other objects (ShoppingBasket contains Product items array)
- **Association**: Relationships between objects (Customer buys Product)

---

## 5. Object-Orientation {#slide-5-object-orientation}

### Content

The object-oriented paradigm models the world as sets of objects that each have particular attributes and exhibit certain behaviour.
Unfortunately, the terminology used by practitioners across different OO-languages can be confusing.
- Here some terms and phrases you may come across:
- Class		: 	“blueprint of an object”, “abstract object description”, “model”
Object 	: 	“model of a thing”, “instance of a class”, “instance”
- Attributes 	: 	 “fields”, “data”, “variables”, “values”, “state”
- Behaviour	:	 “methods”, “functions”, “procedures”, “routines”

---

## 6. Objects and Classes {#slide-6-objects-and-classes}

### Content

Objects and Classes

What is the difference between a class and an object?

A class is an abstract description of an object – like a template or a blueprint.
A class describes all objects that are “of the same kind” yet may differ across specific instances.

For example, we may have a class that describes a car in terms of the number of wheels, seats, windscreen, steering wheel, brand, colour, etc. that it has.
Specific instances of “car” represent the different objects that we can create using the class as a building plan, so there could be a red Ford and a blue Mercedes, or a green three-wheeled Reliant Robin!

Image: Wikimedia Commons

### Visual Analysis

# Objects and Classes

## Core Distinction

**Class**: An abstract description of an object that serves as a template or blueprint. It describes all objects that are "of the same kind" while allowing them to differ across specific instances.

**Object**: A specific instance created from a class, with concrete values for the properties defined in the class.

## Key Concept

A class defines the structure and characteristics that all objects of that type will possess, but each object can have different values for those characteristics.

## Example: Car Class

A car class describes vehicles in terms of:
- Number of wheels
- Number of seats
- Windscreen
- Steering wheel
- Brand
- Colour

### Specific Object Instances

Using the car class as a building plan, different objects can be created:
- A red Ford
- A blue Mercedes
- A green three-wheeled Reliant Robin

Each object is an instance of the car class but has different specific values for the properties defined by the class (different colors, brands, and even different numbers of wheels).

---

## 7. Objects and Classes {#slide-7-objects-and-classes}

### Content

- Anatomy of a class: Overview

- Class

- Data

- Methods

Each class has components that represent data. These model the attributes of the objects that will be created from this class.

A class often also has methods to model its behaviour and to retrieve or modify its data in a controlled fashion.

---

## 8. Objects and Classes {#slide-8-objects-and-classes}

### Content

- Anatomy of a class: Overview

- Class

- Data

- Methods

- var someClass = {
- // data (variables)
- data1: value,
data2: value,     ...
- // methods
- behaviour1: function() { },
- behaviour2: function() { }
...
- };

---

## 9. Objects and Classes {#slide-9-objects-and-classes}

### Content

- Anatomy of a class: Overview

- Class

- Data

- Methods

- var customer = {
- name: "John",
- age: 40,
- getName: function() {
- return this.age;
- },
- changeName: function(x) {
- this.name = x;
- }
- };

“this” refers to the object as owner of the element.

- “dot” notation

---

## 10. Objects and Classes {#slide-10-objects-and-classes}

### Content

- Anatomy of a class: Data and Methods

- Customer

- var name
- var age
- …

The choice of data variables reflects the characteristics of the object in the context of the problem that we want to solve in our program.

- getName()
- changeName(n)
- …

The choice of methods reflects the behaviours that an object needs to model.

---

## 11. Objects and Classes {#slide-11-objects-and-classes}

### Content

Another example: We want to create many different stars to draw on screen.
How can we characterise a star shape in an abstract fashion?

---

## 12. Objects and Classes {#slide-12-objects-and-classes}

### Content

- Example: Star object

- Star

- Color col
- Position pos
- int points
- int size

- Abstraction

- Instances of “Star” (Objects)

- Class “Star”

A class is an abstract description of an object and its behaviour.

- getColour()
- setColor(int)
- getPosition()
- setPosition(int,int)
- getPoints()
- setPoints(int)

---

## 13. Objects and Classes {#slide-13-objects-and-classes}

### Content

- Example: Star object

- Star

- Instances of “Star” (Objects)

- Class “Star”

- Instantiation

An object is a concrete instance of a class.

- Color col
- Position pos
- int points
- int size

- getColour()
- setColor(int)
- getPosition()
- setPosition(int,int)
- getPoints()
- setPoints(int)

---

## 14. Objects and Classes {#slide-14-objects-and-classes}

### Content

- Example: Star object

- redStar

- Color: RED
- Position: x=75, y=100
- points = 5
- size = 3

- Instances of “Star” (Objects)

- Class “Star”

- Instantiation

- redStar = new Star();
- redStar.setColor(RED);
- redStar.setPoints(5);
- …

- Once instantiated, each object maintains it’s
own set of characteristics (Object state).

- getColour()
- setColor(int)
- getPosition()
- setPosition(int,int)
- getPoints()
- setPoints(int)

---

## 15. Objects and Classes {#slide-15-objects-and-classes}

### Content

- Object state

- greenStar

- Color: GREEN
- Position x=225, y=100
- points = 7
- size = 5

Once instantiated, each object has a state of its own.
The state of an object is determined by its data, i.e. the current values of its members.

- yellowStar

- Color: YELLOW
- Position x=150, y=100
- points = 4
- size = 2

- redStar

- Color: RED
- Position x=75, y=100
- points = 5
- size = 3

---

## 16. Objects and Classes {#slide-16-objects-and-classes}

### Content

- Creating objects
Individual objects can be created by declaring a variable name and then defining data members and methods directly in the subsequent code block

- var customer = {
- lastname: "Jones",
- firstname:"Tom",
- age:25,
- getName : function() {
- return this.lastname + " " + this.firstname;
}	...
- };

- Curly braces. Note the ”;” after the closing bace

- Elements separated by comma

---

## 17. Objects and Classes {#slide-17-objects-and-classes}

### Content

- Creating objects
Individual objects can ALSO be created by using the Javascript new keyword with the generic Object constructor function

- var customer = new Object();
- customer.lastname = "Jones";
- customer.firstname = "Tom";
- customer.age = "25";
- customer.getName = function () {
- return this.firstname + " " + this.lastname;
- };

- Individual instructions – these end with “;”

Curly braces when defining a function in this way. Note the ”;” after the closing brace

---

## 18. Objects and Classes {#slide-18-objects-and-classes}

### Content

- Object constructor
A more flexible way of creating objects is to define a function that implements a specific constructor
- To create an instance:

- function Customer(lastname, firstname, age) {
- this.lastname = lastname;
- this.firstname = firstname;
- this.age = age;
- this.getName = function () {
- return this.firstname + " " + this.lastname;
- };
- }

- Class constructors tend to becapitalised

- var cust1 = new Customer("Jones", "Tom", 25);

---

## 19. Objects and Classes {#slide-19-objects-and-classes}

### Content

- Accessing objects
We use the object name with the dot notation to access object properties and functions
Alternatively, we can also use [ ] after the object name, with the field name in ""
Methods are also called after the dot, and need to use the parameter brackets

- cust1.getName();

- cust1.age;

- cust1["age"];

---

## 20. Objects and Classes {#slide-20-objects-and-classes}

### Content

- Predefined objects in Javascript
There are a range of predefined objects that we can readily use in programsyou already know Array()
- Others are String(), Number(), Boolean()
- Find more in the JS reference documentation

---

## 21. Practice {#slide-21-practice}

### Content

- Creating classes and objects
Write a Javascript program that creates a constructor for a class “Person”, to be used in the context of managing users of a public library.
Define suitable data variables for this class – what are attributes of a person?
Define methods to implement model what a person can do in a library
- Create different “person” objects and let them do things
If you explored the use of <form> <input> and <label> fields, create elements on your HTML page to access the methods to let your objects do things, like borrow or return books, for example.

---

## 22. Next Lectures {#slide-22-next-lectures}

### Content

Next Lectures

XAMPP installation
Relational databases

22

### Visual Analysis

# Upcoming Topics

## XAMPP Installation
XAMPP is a software package that will be covered in the next lecture. It provides a local development environment for web applications.

## Relational Databases
The course will continue with an examination of relational databases, covering:
- Database structure and organization
- Relationships between data tables
- Database management concepts

---


---

## Processing Metadata

### Slide Classification
- Text slides: 19
- Visual slides: 3
- Optimized percentage (without API): 86.4%

### API Costs
- Input tokens: 107,137
- Output tokens: 23,824
- Total cost: $0.6788 USD

### System
- Generated by: PPTX to Markdown Converter
- Date: 2026-01-11 19:15:36