# SIM   L02b


## Systems for Information ManagementLecture 2b


- Dr Imran U Khan			School of Engineering and Informatics

---

## Previously


- Information transfer
- How information is transmitted within and between computers
- Buses
- Networks
- The Internet

---

## Today


- Internet and World-wide Web
- HTTP, Hypertext and the World Wide Web
- Web search
- Cloud computing

---

## Recap: Internet Protocols


Recap: Internet Protocols



IP

TCP, UDP

DNS

HTTP

Ethernet


# Internet Protocol Stack

## Protocol Layers

The slide presents the hierarchical structure of Internet protocols organized in layers:

### Physical/Data Link Layer
- **Ethernet**: Handles the physical transmission of data over local networks

### Network Layer
- **IP (Internet Protocol)**: Responsible for addressing and routing packets across networks

### Transport Layer
- **TCP (Transmission Control Protocol)**: Provides reliable, connection-oriented communication with error checking and flow control
- **UDP (User Datagram Protocol)**: Provides faster, connectionless communication without guaranteed delivery

### Application Layer
- **DNS (Domain Name System)**: Translates human-readable domain names into IP addresses
- **HTTP (Hypertext Transfer Protocol)**: Protocol for transmitting web pages and other resources over the Internet

## Protocol Relationships

This layered architecture demonstrates how Internet protocols work together, with each layer building upon the services provided by the layer below it. Lower layers handle more fundamental networking functions, while higher layers provide specific application services.

---

## HTTP (Hypertext Transfer Protocol)


- Overview
- HTTP is a protocol that makes the World-wide Web possible
It is one of the many protocols that operate in the application layer of the TCP/IP protocol suite
Interactions are between a client and a server. The client (e.g. a web browser) makes requests to a server (e.g., a web server).

---

## HTTP (Hypertext Transfer Protocol)


- URLs
Resources can be identified by Uniform Resource Locators (URLs).
- A URL has three basic parts, e.g. forhttp://www.gnu.org/licenses/licenses.html
http is the scheme name, identifying the kind of resource, such as hypertext.
www.gnu.org is the fully-qualified domain name of the host, i.e. the server where the resource is to be found.
/licenses/licenses.html is a path: it specifies to the host where to find the resource. It often maps onto the directory or folder structure of the host computer’s file system.

---

## HTTP (Hypertext Transfer Protocol)


- Communication via HTTP
Clients use the URL’s host information to establish a connection, and the path to send a request to the server. Requests are text strings, e.g.GET /licenses/licenses.html HTTP/1.1
The server should respond with a message that includes a representation of the resource requested. A typical representation is a text document containing hypertext markup code, and possibly linking up further web resources, such as other hypertext pages, or images.

---

## Example


Example




# Example

This slide serves as a section header indicating that example content or case studies related to Information Systems will follow. No specific educational concepts or detailed information are provided on this particular slide.

---

## Example


Example


139.184.32.101

216.120.44.56

139.100.19.84

IP addresses

8.8.8.8



# IP Addresses

## Concept

IP addresses are numerical labels used to identify devices on a network.

## Examples

The slide presents four sample IP addresses:

- 139.184.32.101
- 216.120.44.56
- 139.100.19.84
- 8.8.8.8

## IP Address Format

These examples demonstrate the standard IPv4 address format:
- Four numerical segments separated by periods (dots)
- Each segment ranges from 0 to 255
- Written in dotted-decimal notation

## Notable Example

**8.8.8.8** - This is Google's public DNS (Domain Name System) server, one of the most commonly used DNS servers worldwide.

---

## Example


Example


139.184.32.101

216.120.44.56

139.100.19.84

Resources

8.8.8.8



# IP Addresses and Resource Communication

## Network Communication Example

This example illustrates how multiple devices with different IP addresses communicate with shared resources.

### Device IP Addresses

Three distinct devices are identified by their IP addresses:
- `139.184.32.101`
- `216.120.44.56`
- `139.100.19.84`

### Resource Server

A central resource server is identified by the IP address:
- `8.8.8.8`

**Note:** This is Google's public DNS server address, commonly used as an example of a well-known internet service.

### Communication Pattern

The diagram demonstrates that multiple clients (the three different IP addresses) can simultaneously access or communicate with a single resource server. This represents a typical client-server architecture where:

- Multiple clients initiate connections to a centralized service
- Each client maintains a unique IP address for identification
- The resource server responds to requests from all connected clients
- This architecture is fundamental to internet services, DNS lookups, web servers, and many other network applications

---

## Example


Example


GET URL

139.184.32.101

8.8.8.8

216.120.44.56

139.100.19.84

Host 1 makes request for URL:
http://www.susx.ac.uk/page.html



# DNS Resolution Example

## Scenario Overview
A host (Host 1) is attempting to access a web page by making an HTTP request to:
```
http://www.susx.ac.uk/page.html
```

## Network Components Involved

The example illustrates multiple IP addresses that participate in the DNS resolution and communication process:

- **139.184.32.101** - First IP address in the resolution chain
- **8.8.8.8** - Google's public DNS server (commonly used for domain name resolution)
- **216.120.44.56** - Additional IP address in the process
- **139.100.19.84** - Another IP address involved

## DNS Resolution Process

When a user enters a URL like `www.susx.ac.uk/page.html`, the system must:

1. Translate the human-readable domain name (www.susx.ac.uk) into an IP address
2. Contact DNS servers to perform this resolution
3. Use the resolved IP address to establish a connection with the web server
4. Retrieve the requested resource (page.html)

## Key Concept

This example demonstrates the fundamental role of DNS (Domain Name System) in converting domain names into numerical IP addresses that computers use to communicate over networks. Multiple servers may be involved in resolving a single domain name query.

---

## Example


Example


139.184.32.101

8.8.8.8

216.120.44.56

139.100.19.84

Look up DNS entry of susx.ac.uk

Find out IP of server www

DNS retrieves IP address of the node: 216.120.44.56



# DNS Lookup Example

## Process Overview

This example demonstrates a Domain Name System (DNS) lookup process for resolving a domain name to an IP address.

## DNS Query Sequence

**Domain to resolve:** susx.ac.uk

**Target:** Find the IP address of server www (www.susx.ac.uk)

## IP Addresses Involved

- 139.184.32.101
- 8.8.8.8
- 216.120.44.56
- 139.100.19.84

## Resolution Result

The DNS system successfully retrieves the IP address of the requested node:

**Resolved IP Address:** 216.120.44.56

## Key Concept

DNS (Domain Name System) translates human-readable domain names (like susx.ac.uk) into machine-readable IP addresses (like 216.120.44.56) that computers use to identify and communicate with each other on networks.

---

## Example


Example


139.184.32.101

8.8.8.8

216.120.44.56

139.100.19.84

Request is routed to the Host 2



# Network Routing Example

## IP Address Communication

The slide demonstrates a routing scenario involving four IP addresses:

- **139.184.32.101** (origin)
- **8.8.8.8** (intermediate node)
- **216.120.44.56** (intermediate node)
- **139.100.19.84** (Host 2 - destination)

## Routing Behavior

The request is routed to **Host 2** (139.100.19.84), illustrating how network packets traverse through multiple nodes in a network topology to reach their intended destination. This demonstrates the fundamental concept of packet routing in IP networks, where data travels through intermediate points before arriving at the target host.

---

## Example


Example


139.184.32.101

216.120.44.56

139.100.19.84

8.8.8.8

Identity

Location

URI

URN

URL

Name

Host 2 retrieves the requested resource



# Uniform Resource Identifiers (URIs) and Related Concepts

## Core Concepts

**URI (Uniform Resource Identifier)**: The overarching concept that encompasses methods for identifying resources on the internet.

**URN (Uniform Resource Name)**: A type of URI that provides a persistent name for a resource, independent of its location. Functions as the "identity" or "name" of a resource.

**URL (Uniform Resource Locator)**: A type of URI that specifies both the identity and location of a resource. It tells you where to find something on the network.

## Hierarchical Relationship

```
URI (top level)
├── URN (Name/Identity)
└── URL (Name + Location)
```

## IP Addresses as Locations

The example shows four IP addresses representing different network locations:
- 139.184.32.101
- 216.120.44.56
- 139.100.19.84
- 8.8.8.8 (Google's public DNS server)

These demonstrate how URLs incorporate location information to enable resource retrieval across networks.

## Resource Retrieval Process

The notation "Host 2 retrieves the requested resource" indicates that when a URL is used, it enables a host system to locate and retrieve the specified resource from its network location.

## Key Distinction

- **URN**: Identifies WHAT something is (persistent identity)
- **URL**: Identifies WHERE something is located (address for retrieval)

---

## Example


Example


HTML, JPG

139.184.32.101

216.120.44.56

139.100.19.84

8.8.8.8

Identity

Location

URI

URN

URL

Name

Host 2 sends the resource to the host
that made the request



# URI, URL, URN, and Resource Retrieval

## Resource Identification Concepts

### URI (Uniform Resource Identifier)
The overarching concept for identifying resources. All resource identifiers fall under this category.

### URL (Uniform Resource Locator)
A type of URI that specifies both the **identity** and **location** of a resource.

Components shown in the example:
- Resource types: HTML, JPG
- IP addresses representing locations on the network

### URN (Uniform Resource Name)
A type of URI that provides only the **name/identity** of a resource, without specifying its location.

## IP Addresses in the Example

The following IP addresses are illustrated:
- `139.184.32.101`
- `216.120.44.56`
- `139.100.19.84`
- `8.8.8.8`

These represent different hosts/locations in the network infrastructure.

## Resource Request and Response Process

The example demonstrates a client-server interaction:
1. A host makes a request for a resource (identified by URI/URL)
2. Host 2 (the server) sends the requested resource back to the requesting host
3. The resource can be various file types (HTML, JPG, etc.)

## Key Distinction

**URL = Location + Identity** (where to find it and what it is)
**URN = Identity only** (what it is, but not where to find it)

---

## Example


Example


139.184.32.101

216.120.44.56

139.100.19.84

8.8.8.8

HTML, JPG

Host 1 receives and decodesthe resource



# Network Communication: Resource Retrieval Process

## Final Step in Web Resource Retrieval

**Host 1 receives and decodes the resource**

This represents the concluding step where the requesting computer (Host 1) successfully receives the requested web resources (HTML, JPG files) from the destination server and decodes them for display or use.

## IP Addresses in Communication

The example shows multiple IP addresses involved in the communication process:

- **139.184.32.101** - Source or intermediate node
- **216.120.44.56** - Intermediate node or server
- **139.100.19.84** - Another node in the network path
- **8.8.8.8** - Google's public DNS server

## Resource Types

**HTML, JPG** - Common web resources being transferred:
- HTML: Hypertext Markup Language files containing webpage structure
- JPG: Image files in JPEG format

## Process Overview

After traversing through various network nodes and potentially using DNS resolution (8.8.8.8), the requested resources reach Host 1, which then:
1. Receives the data packets
2. Decodes the content
3. Renders or displays the resources appropriately

---

## Example


Example


HTML

139.184.32.101

216.120.44.56

139.100.19.84

8.8.8.8



# DNS Name Resolution Example

## Process Flow

This example demonstrates how DNS (Domain Name System) resolves a hostname to an IP address.

**Query**: HTML (hostname to be resolved)

## DNS Server Chain

The resolution process involves querying multiple DNS servers in sequence:

1. **139.184.32.101** - First DNS server contacted
2. **216.120.44.56** - Second DNS server in the chain
3. **139.100.19.84** - Third DNS server queried
4. **8.8.8.8** - Final DNS server (Google Public DNS)

## Key Concept

When a hostname needs to be resolved to an IP address, the request may be forwarded through multiple DNS servers until the authoritative answer is found. Each server in the chain either:
- Provides the answer if it has the information cached or is authoritative
- Forwards the query to another DNS server that may have the information

The IP address **8.8.8.8** represents Google's public DNS resolver, commonly used as a recursive DNS server to resolve domain names.

---

## HTML (Hypertext Markup Language)


- Introduction
HTML is a markup language. Markup languages present a way to add meta data to text
HTML is based on the more complex language SGML, the “Standardised General Markup Language”.
HTML is a way of representing documents that helps a web browser to present them to a user effectively, and which allows the user to navigate between related documents.
Web technologies are not as well-defined as TCP or IP: there are a set of specifications which ensure some level of compatibility, but there are few universally accepted standards.

---

## HTML (Hypertext Markup Language)


- Web browsers
“Browsers” are software applications that interpret HTML (and other languages) to display web pages
The first web browser was created in 1990 (by Tim Berners-Lee), and browsers like Mosaic, Netscape Navigator and Internet Explorer were popular in the early years of the Web
- Common browsers today are Chrome, Firefox, Edge, or Safari

---

## HTML (Hypertext Markup Language)


- The world-wide Web (WWW)
While credit is given to Tim Berners-Lee to have “invented” the World-wide Web, what he mainly did was adapt and combine two technologies:
Devise HTML, a markup language that was a simpler and more user-friendly version of SGML
- Embed the concept of hyperlinks in that language
The global Internet and core technologies that enabled the world-wide web existed before 1990, but developments such as URLs and HTTP were specifically made to create the world-wide web.

---

## HTML (Hypertext Markup Language)


How does HTML work?
In HTML, text is combined with tags which describe the document content:e.g. <strong>stuff</strong> means that “stuff” should be shown in a way that indicates that it is important.
Tags are not meant to be used to control the exact appearance of the page, but rather to indicate to a web browser how the page should be rendered (i.e., displayed)
Images, tables and hyperlinks are all included using tags.
HTML standards are controlled by the World Wide Web Consortium (W3C).
However, standards evolve and many browsers are not fully compliant.

---

## HTML (Hypertext Markup Language)


HTML (Hypertext Markup Language)

Example

Open http://www.gnu.org/licenses/licenses.html

In the browser



# HTML (Hypertext Markup Language)

## Practical Example

### Exercise
Open the following URL in a web browser:
```
http://www.gnu.org/licenses/licenses.html
```

This exercise demonstrates how to access and view HTML documents through a browser, illustrating the basic function of HTML as the markup language used to structure web pages.

## Purpose
This example serves to show how HTML documents are accessed and rendered by web browsers, connecting the theoretical concept of HTML to its practical application in displaying web content.

---

## HTML (Hypertext Markup Language)


HTML (Hypertext Markup Language)

Example

In HTML:



# HTML (Hypertext Markup Language)

## Definition
HTML stands for Hypertext Markup Language, the standard markup language used to create and structure content on the web.

## Purpose
HTML provides the fundamental structure and content of web pages, defining elements like headings, paragraphs, links, images, and other content types that browsers interpret and display.

## Key Characteristics
- Markup language using tags to define elements
- Foundation of web page structure
- Works in conjunction with CSS (styling) and JavaScript (interactivity)
- Uses opening and closing tags to wrap content
- Browser-interpreted language

---

## HTML (Hypertext Markup Language)


HTML (Hypertext Markup Language)

Example

In HTML:



# HTML (Hypertext Markup Language)

## Definition
HTML stands for Hypertext Markup Language. It is the standard markup language used to create and structure content on the web.

## Purpose
HTML provides the fundamental building blocks for web pages, allowing developers to define the structure and semantic meaning of web content through a system of tags and elements.

## Key Characteristics
- Uses a tag-based syntax to mark up content
- Forms the backbone of web page structure
- Works in conjunction with CSS (styling) and JavaScript (interactivity)
- Interpreted by web browsers to render web pages

---

## HTML (Hypertext Markup Language)


HTML (Hypertext Markup Language)

Example

In HTML:



# HTML (Hypertext Markup Language)

## Definition
HTML stands for Hypertext Markup Language, which is the standard markup language used to create web pages.

## Key Characteristic
The slide indicates that an HTML example is being presented, suggesting that HTML is demonstrated through practical code examples rather than just theoretical definitions.

## Context
This appears to be part of a series covering web technologies and information systems, with HTML being a fundamental building block of web development and online information presentation.

---

## Web search


How do search engines work?
Search engines are software services that aim to make the information on the World-wide Web more accessible. Some of them might charge money for promoting certain websites over others.
Search engines involve different processes, some of which run in the background
- Web crawling
- Content indexing
- Query support and ranking

---

## Web search


How do search engines work?
The crawler is a program that generates http requests, analyses the web pages returned to extract URLs, and generates more http requests using these URLs
This information is then used to build an index of the web pages or other resources found in relation to their semantic content, so that it is possible to find all pages that contain a given word or content pattern, to which we attribute meaningFor example, a search engine might index certain websites that are associated to word combinations such as “baking recipes”, or “vintage cars”, etc.Today, there are also a few search engines that can process other types of information, such pixel patterns in images (e.g., Google reverse image search)

---

## Web search


How do search engines work?
When a user visit the web page of the search engine to make a query,the software will look up the query words in its index and return some the search results that are indexed against them (web pages).
At the same time, the search engine will rank the candidate web pages in order of ‘citation importance’, for example. However, ranking algorithms are complex, and often not fully transparent. There can also be interference by way of paid advertisements.
More recent extensions to the traditional algorithms for web search can deliver personalised search results, but this also has side effects like the “filter bubble” phenomenon, for example.

---

## Cloud computing


- Basics
Allows computing resources to be shared over the Internet, achieving economies of scale.
Storage, processing and network resources are supplied as a service across the Internet – by a provider to end users who access them through a web browser, or a desktop application.
- Example: Amazon Web Services, which include
- EC2 (Elastic Compute Cloud) – virtual private servers
- S3 (Simple Storage Service) – remote data storage
- CloudFront – distributing data to locations near user
- WorkSpaces – device-independent virtual desktops

---

## Cloud computing


- Potential advantages:
More convenient management and deployment of applications , since not installed on each user’s computer
Improved utilization by running server and storage device instances as virtual machines on a single host
- Rapid scalability and elasticity of resources
- Increased reliability due to multiple redundant sites
- Capital (setup) costs are converted to operational costs

---

## Cloud computing


- Potential disadvantages:
- Greater security risk, since data is stored remotely
- Reduced control over technical trade offs

---

## Summary


HTTP is the protocol used to transmit Hypertext documents that are the foundational resources of the World Wide Web
HTML is a basic markup language and used to outline and encode the structure of web pages
Web search entails a number of processes to find, index, rank different web pages by content. Keywords are commonly used to select web pages from the index in response to user queries.
Cloud computing bundles resources and offers them as a service over the Internet.

---

## Read


- Brookshear & Brylow
Computer Science: An Overview. Pearson Education, 12th edition, 2015.
- Chapter 4.3

---

## Next Lecture


Next Lecture

Structured data representation with XML



# Next Lecture Topic

## Upcoming Content

**Structured data representation with XML**

The next lecture will cover how XML (eXtensible Markup Language) is used to represent structured data in information systems.

---
