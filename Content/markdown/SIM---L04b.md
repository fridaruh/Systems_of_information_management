# SIM   L04b


## Systems for Information Management


- Dr Imran U Khan		School of Engineering and Informatics

---

## Previously


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

## Today


- More basic programming concepts
- Discussion of previous lab exercises:
- Fibonacci numbers
- Two-dimensional arrays
- Object orientation
- Objects in Javascript and how to use them

---

## Object-Orientation


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

## Object-Orientation


The object-oriented paradigm models the world as sets of objects that each have particular attributes and exhibit certain behaviour.
Unfortunately, the terminology used by practitioners across different OO-languages can be confusing.
- Here some terms and phrases you may come across:
- Class		: 	“blueprint of an object”, “abstract object description”, “model”
Object 	: 	“model of a thing”, “instance of a class”, “instance”
- Attributes 	: 	 “fields”, “data”, “variables”, “values”, “state”
- Behaviour	:	 “methods”, “functions”, “procedures”, “routines”

---

## Objects and Classes


Objects and Classes

What is the difference between a class and an object?

A class is an abstract description of an object – like a template or a blueprint.
A class describes all objects that are “of the same kind” yet may differ across specific instances.

For example, we may have a class that describes a car in terms of the number of wheels, seats, windscreen, steering wheel, brand, colour, etc. that it has.
Specific instances of “car” represent the different objects that we can create using the class as a building plan, so there could be a red Ford and a blue Mercedes, or a green three-wheeled Reliant Robin!

Image: Wikimedia Commons


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

## Objects and Classes


- Anatomy of a class: Overview

- Class

- Data

- Methods

Each class has components that represent data. These model the attributes of the objects that will be created from this class.

A class often also has methods to model its behaviour and to retrieve or modify its data in a controlled fashion.

---

## Objects and Classes


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

## Objects and Classes


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

## Objects and Classes


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

## Objects and Classes


Another example: We want to create many different stars to draw on screen.
How can we characterise a star shape in an abstract fashion?

---

## Objects and Classes


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

## Objects and Classes


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

## Objects and Classes


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

## Objects and Classes


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

## Objects and Classes


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

## Objects and Classes


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

## Objects and Classes


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

## Objects and Classes


- Accessing objects
We use the object name with the dot notation to access object properties and functions
Alternatively, we can also use [ ] after the object name, with the field name in ""
Methods are also called after the dot, and need to use the parameter brackets

- cust1.getName();

- cust1.age;

- cust1["age"];

---

## Objects and Classes


- Predefined objects in Javascript
There are a range of predefined objects that we can readily use in programsyou already know Array()
- Others are String(), Number(), Boolean()
- Find more in the JS reference documentation

---

## Practice


- Creating classes and objects
Write a Javascript program that creates a constructor for a class “Person”, to be used in the context of managing users of a public library.
Define suitable data variables for this class – what are attributes of a person?
Define methods to implement model what a person can do in a library
- Create different “person” objects and let them do things
If you explored the use of <form> <input> and <label> fields, create elements on your HTML page to access the methods to let your objects do things, like borrow or return books, for example.

---

## Next Lectures


Next Lectures

XAMPP installation
Relational databases



# Upcoming Topics

## XAMPP Installation
XAMPP is a software package that will be covered in the next lecture. It provides a local development environment for web applications.

## Relational Databases
The course will continue with an examination of relational databases, covering:
- Database structure and organization
- Relationships between data tables
- Database management concepts

---
