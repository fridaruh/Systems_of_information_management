# SIM   L8b

**Conversion date:** 2026-01-11
**Original file:** `SIM - L8b.pptx`
**Total slides:** 22

---


## Table of Contents

1. [Systems for Information ManagementLecture 8b](#slide-1-systems-for-information-managementlecture-8b)
2. [Previously](#slide-2-previously)
3. [Today](#slide-3-today)
4. [Connecting to a database using PHP](#slide-4-connecting-to-a-database-using-php)
5. [Database security](#slide-5-database-security)
6. [Database security](#slide-6-database-security)
7. [Database security](#slide-7-database-security)
8. [Database security](#slide-8-database-security)
9. [Database security](#slide-9-database-security)
10. [Connecting to a database using PHP](#slide-10-connecting-to-a-database-using-php)
11. [Connecting to a database using PHP](#slide-11-connecting-to-a-database-using-php)
12. [Running SQL commands from a PHP program](#slide-12-running-sql-commands-from-a-php-program)
13. [Running SQL commands from a PHP program](#slide-13-running-sql-commands-from-a-php-program)
14. [Sending information to a database](#slide-14-sending-information-to-a-database)
15. [PHP and HTML](#slide-15-php-and-html)
16. [HTML forms revisited](#slide-16-html-forms-revisited)
17. [Sending and responding to HTTP requests](#slide-17-sending-and-responding-to-http-requests)
18. [Sending and responding to HTTP requests](#slide-18-sending-and-responding-to-http-requests)
19. [Sending and responding to HTTP requests](#slide-19-sending-and-responding-to-http-requests)
20. [Summary](#slide-20-summary)
21. [Beyond this module: An outlook](#slide-21-beyond-this-module-an-outlook)
22. [Next Lecture](#slide-22-next-lecture)

## 1. Systems for Information ManagementLecture 8b {#slide-1-systems-for-information-managementlecture-8b}

### Content

- Dr Imran U Khan		School of Engineering and Informatics

---

## 2. Previously {#slide-2-previously}

### Content

- SQL & PHP
- SQL for data definition and data manipulation
- PHP for server-side scripting

- 2

---

## 3. Today {#slide-3-today}

### Content

- Web applications with SQL and PHP
- Connecting to a database using PHP
- Database security
- Executing SQL commands from a PHP program
- HTML forms revisited
- Sending and responding to HTTP requests

- 3

---

## 4. Connecting to a database using PHP {#slide-4-connecting-to-a-database-using-php}

### Content

- Overview
Like many other programming languages, PHP has specific built-in functions and objects that allow connecting and interacting with databases.
A database server maintains a list of user accounts that have certain permissions concerning what the user can and cannot do on the server(e.g., access databases, create schemas, read data, change data, etc.)
We usually need four pieces of information to connect to and use a database:
- The server name or IP address
A user name that has been set up on the server
- A password for the user
- The name of the database that we want to access

- 4

---

## 5. Database security {#slide-5-database-security}

### Content

Database security

User accounts overview

5

Existing users

Click here to create a new user

### Visual Analysis

# Database Security: User Accounts Overview

## User Account Management

Database security involves managing user accounts to control access to database resources. A user account management system typically provides two core functions:

### Key Functions

1. **Viewing Existing Users**
   - Ability to see a list of current database users
   - Review who has access to the database system

2. **Creating New Users**
   - Functionality to add new user accounts to the database
   - Interface for initiating the user creation process

## Security Implications

User account management is a fundamental aspect of database security because it:
- Controls who can access the database
- Enables implementation of authentication mechanisms
- Forms the basis for authorization and permission systems
- Allows tracking and auditing of database activities by user

---

## 6. Database security {#slide-6-database-security}

### Content

Database security

Choosing a user name and password

6

1) Type your user name

2) Type and repeat password

3) Scroll to bottom and press "Go"

### Visual Analysis

# Database Security

## User Authentication Process

### Creating User Credentials

The process of establishing secure database access involves three steps:

1. **Enter User Name** - Define a unique identifier for the user account
2. **Set Password** - Enter and confirm the password by typing it twice to ensure accuracy
3. **Submit Credentials** - Navigate to the bottom of the form and activate the "Go" button to complete registration

### Purpose

This procedure establishes the fundamental authentication mechanism for database security, ensuring that only authorized users with valid credentials can access the database system. The password repetition step helps prevent typographical errors during initial account setup.

---

## 7. Database security {#slide-7-database-security}

### Content

Database security

User privileges

We could just assign global privileges to the user, allowingaccess to all data-bases on the server.
But doing that would not be good practice.
Let's pick a specific database instead.

7

Click "Database"

### Visual Analysis

# Database Security: User Privileges

## Privilege Scope Considerations

### Global Privileges
Global privileges grant a user access to all databases on the server. This represents the broadest level of access control.

### Best Practice: Database-Specific Privileges
Assigning global privileges is **not recommended** as a security practice. Instead, privileges should be assigned at the database level.

## Principle of Least Privilege
Rather than granting blanket access across all databases, access control should be restricted to specific databases that a user needs to work with. This limits potential security risks and follows the principle of least privilege.

## Implementation Approach
When configuring user access, the recommended method is to:
1. Avoid global privilege assignment
2. Select a specific database for the user
3. Grant privileges only for that targeted database

This granular approach to privilege management enhances database security by limiting the scope of user access to only what is necessary.

---

## 8. Database security {#slide-8-database-security}

### Content

Database security

User privileges

8

Select "chinook" and click "Go"

### Visual Analysis

# Database Security - User Privileges

## Context
The task involves working with the "chinook" database, which is selected from available database options.

## Key Concepts

### User Privileges
User privileges are permissions granted to database users that control what operations they can perform on database objects. These privileges are fundamental to database security and access control.

### Database Selection
The instruction to "Select 'chinook' and click 'Go'" indicates the process of:
- Choosing a specific database from multiple available databases
- Navigating to that database's management interface to configure or review user privileges

## Purpose
This operation allows administrators to:
- Manage who can access specific databases
- Configure granular permissions for different users
- Implement security policies at the database level
- Control operations like SELECT, INSERT, UPDATE, DELETE, and administrative functions

---

## 9. Database security {#slide-9-database-security}

### Content

Database security

User privileges

The user cannow use SQL for datamanipulationwith the data-base "chinook"

9

Select "Data" and click "Go"

### Visual Analysis

# Database Security - User Privileges

## User Access Rights

Once a user has been granted appropriate privileges, they can perform SQL operations for data manipulation within the database.

## Example Context

**Database**: chinook

**Action Required**: Navigate to the "Data" section and click "Go" to access data manipulation capabilities

## SQL Data Manipulation

After privileges are established, users can execute SQL commands to:
- Query data (SELECT)
- Insert new records (INSERT)
- Update existing records (UPDATE)
- Delete records (DELETE)

The privilege system controls which of these operations a specific user can perform on the chinook database.

---

## 10. Connecting to a database using PHP {#slide-10-connecting-to-a-database-using-php}

### Content

- How to connect to the MySQL server using PHP
PHP offers dedicated functions to interact with MySQL and other databases
- To connect to MySQL, use either the built-in function mysqli_connect()
An alternative way to connect is by creating either a mysqli or a PDO object, using a constructor:
Information about the connection attempt is stored in the variable $c in this example

- 10

- $c = mysqli_connect(serverName, userName, password, databaseName);

- $c = new mysqli(serverName, userName, password, databaseName);

---

## 11. Connecting to a database using PHP {#slide-11-connecting-to-a-database-using-php}

### Content

- How to connect to the MySQL server using PHP
- Full connection example:

- 11

- <?php
- // Basic information
- $server = "localhost";
- $user = "your_username";
- $pw = "your_password";
- $db = "chinook";
- // Create connection
- $c = new mysqli($server, $user, $pw, $db)
- // alternative: $c = mysqli_connect($server, $user, $pw, $db)
or die("There was a problem!");	// execute this line on error
- echo "Connected successfully<br><br>";
- ?>

---

## 12. Running SQL commands from a PHP program {#slide-12-running-sql-commands-from-a-php-program}

### Content

How to access the data and store it in a variable
SQL statements are basically just text and can be passed together with the connection $c as parameters to a built-in function such as mysqli_query() to retrieve the data.
If instead you created a mysqli object in $c, a handy query() method can be used:
We are going to use the object-based notation from now on.

- $sql = "SELECT Name FROM artist";
- $result = mysqli_query($c, $sql);

- 12

- $sql = "SELECT Name FROM artist";
- $result = $c->query($sql);

---

## 13. Running SQL commands from a PHP program {#slide-13-running-sql-commands-from-a-php-program}

### Content

- Iterating over the result set
Now that our data sits in the $result variable (an associative array that contains the data rows), all we need to do is access the data items and print them out.

- 13

// check more than 0 rows have been returned  if ($result->num_rows > 0) {
- // output data of each row
- while($row = $result->fetch_assoc()) {
- echo $row["Name"]."<br>";
- }
- }
- else {
- echo "No data found";
- }

The num_rows() method will return the number of data rows returned.

fetch_assoc() obtains the next data row as an associative array, where we can index the attributes by name.

---

## 14. Sending information to a database {#slide-14-sending-information-to-a-database}

### Content

We can access the database through our PHP program, but it's not interactive yet
In interactive web applications, we need to be able to send requests to a database dynamically.For example:
To display different content on a web page, depending on the user's choice
To load data from a database to integrate into the web page
- To execute specific queries, initiated by the user

- 14

We can use HTML elements to do this!

---

## 15. PHP and HTML {#slide-15-php-and-html}

### Content

- Overview
PHP documents can integrate HTML markup.
We can use HTML forms to enter information.
We can then submit thisinformation through a HTTP request to be processed by a PHP program onthe webserver.

- 15

- <?php
// We can place a program here that will pick up any data sent
- // Anything below is just HTML
- ?>
- <!DOCTYPE html>
- <html>
- <body>
- <form action="this.php" method="POST">
- <input type="text" name="inf">
- <input type="submit">
- </form>
- </body>
- </html>

- this.php

---

## 16. HTML forms revisited {#slide-16-html-forms-revisited}

### Content

- The basics
- Forms in HTML are enclosed by <form> </form>
In between those tags, we can use all kinds of form field elements, such as <input> , <select> , <textarea>, ...
<form> has two attributes that are important for the interaction with PHP programs:
action: this is the URL where the information will be sent when the form is submitted.
method: This is the HTTP request method used. Relevant values are GET and POST.
GET will attach the information to the URL called, i.e. the values will visible in the URL
POST will submit the information as part of the HTTP header information (hidden from URL)

- 16

---

## 17. Sending and responding to HTTP requests {#slide-17-sending-and-responding-to-http-requests}

### Content

How PHP picks up the information that is sent through a form
If a PHP document is the target of a form action, then the program can access the information through specific variables. Which one will depend on the method used.
- GET requests will be stored in an array called $_GET
- POST requests will be stored in an array called $_POST
The individual form fields submitted are differentiated by their "name" attribute, which can be used as an index on the arrays above (e.g., $_POST["name"], $_POST["age"])
The PHP program can also check if $_REQUEST exists, to determine if it was called normally (e.g., by someone typing the address in the URL bar) or through a form.

- 17

---

## 18. Sending and responding to HTTP requests {#slide-18-sending-and-responding-to-http-requests}

### Content

- Overview

- 18

- <?php
// if the form was submitted, print the information from the field named "inf"
- if($_REQUEST) {
- echo "You submitted: ".$_POST["inf"];
- }
- ?>
- <!DOCTYPE html>
- <html>
- <body>
- <form action="this.php" method="POST">
- <input type="text" name="inf">
- <input type="submit">
- </form>
- </body>
- </html>

- this.php

- PHP part

- HTML part

If there was a request sent through the form, the data from the input field "inf"
will be in the $_POST array.

---

## 19. Sending and responding to HTTP requests {#slide-19-sending-and-responding-to-http-requests}

### Content

- Example
Let's create a simple web application that allows us to select an artist by name and display all the albums we have in store for that artist, using the chinook database.
- Requirements:
We need am HTML form that has a drop-down menu and a submit button.
The drop-down menu options should be populated from the database.
Upon selecting an artist, retrieve the albums from the database and display as a list.
Make it so that results are displayed by clicking the submit-button or when the user makes a selection in the drop-down menu.

- 19

---

## 20. Summary {#slide-20-summary}

### Content

HTML, CSS, Javascript, PHP, and MySQL are examples of core technologies for creating interactive, web-based database applications.
Programs can send HTTP requests to interact with databases on the Internet.
Server-side scripts can connect to databases and assemble web page content dynamically, to include database information, for example.
Client-side scripts can be used to enhance the interactivity of web applications at the user/client end.

- 20

---

## 21. Beyond this module: An outlook {#slide-21-beyond-this-module-an-outlook}

### Content

- A few things also worth knowing about databases
Databases may not necessarily sit on a single server but be distributed across multiple servers as a "cloud" database. To the client, such details will usually be hidden by the DBMS, so that everything appears to be in one place.
Most databases on the Web are relational but not all. Especially in "big data" applications, you may find object-oriented, document-based, or graph-based databases that are not extensively normalised and have simpler schemas. (Remember what we said about NoSQL in lecture 8b)For example, take a look at MongoDB.
There are other programming languages that can use databases, including Python, which is especially relevant in a machine learning context.

- 21

---

## 22. Next Lecture {#slide-22-next-lecture}

### Content

- Security

- 22

---


---

## Processing Metadata

### Slide Classification
- Text slides: 17
- Visual slides: 5
- Optimized percentage (without API): 77.3%

### API Costs
- Input tokens: 39,722
- Output tokens: 7,763
- Total cost: $0.2356 USD

### System
- Generated by: PPTX to Markdown Converter
- Date: 2026-01-11 19:07:55