# SIM   L02a


## Systems for Information ManagementLecture 2a


- Dr Imran U Khan			School of Engineering and Informatics

---

## Previously


- Introduction to computer systems
- Basic concepts of computing: Information processing and information storage
- Hardware: Physical computer components
- Physical and logical aspects of computer systems
- Software: Binary data representation and processing

---

## Today


- Information transfer
- How information is transmitted within and between computers
- Buses
- Networks
- The Internet

---

## Transfer of information


- Relevance
Different computer components need to communicate with each othere.g., CPU and primary memory, display, external devices such as printers
Computer resources are not limited to local machines - we can scale resources across networks of computers and related devicese.g., Cloud computing, or network-attached storage
The digital transfer of information has become essential part of many workflowse.g., Information search and retrieval through databases and websites, or e-mail

---

## Buses


Buses

What is a bus?

A bus is a collection of conductors, eachtransmitting a different signal betweendifferent parts of a computer.

Named after busbars in electrical equipment.

Often made from copper:insulated flexible wires or lines ofcopper printed onto a circuit board.



# Buses in Computer Systems

## Definition

A **bus** is a collection of conductors, with each conductor transmitting a different signal between different parts of a computer.

## Etymology

The term "bus" is derived from **busbars** in electrical equipment, reflecting its function as a shared electrical pathway.

## Physical Implementation

Buses are commonly constructed from **copper** in two main forms:

- **Insulated flexible wires** - discrete conductors bundled together
- **Copper traces printed onto circuit boards** - lines of copper integrated into PCB design

## Function

Each individual conductor within the bus carries a distinct signal, enabling parallel data transmission and communication between different computer components.

---

## Buses


Buses

Purpose

We need buses to transferinformation between themajor components ofa computer system

This includes internal components (e.g., CPU, GPU, RAM) as well as external devices(e.g., keyboard, mouse, external drives)



# Buses in Computer Systems

## Definition and Purpose

Buses are pathways used to transfer information between the major components of a computer system.

## What Buses Connect

Buses facilitate communication between two categories of components:

### Internal Components
- CPU (Central Processing Unit)
- GPU (Graphics Processing Unit)
- RAM (Random Access Memory)

### External Devices
- Keyboard
- Mouse
- External drives

## Function

Buses serve as the communication infrastructure that enables data exchange throughout the computer system, allowing both internal hardware components and external peripheral devices to interact with each other and with the processor.

---

## Buses


Buses

Example

The image shows a partial snapshot of a PC mainboard, whichis the printed circuit board (PCB) that has connectors for the core internal components of a PC, such the CPU, RAM, and various interfaces for data storage and transmission devices
You can see the data linesconnecting the CPU (on the right)with the RAM (the banks on the left)



# Buses in Computer Systems

## PC Mainboard (Motherboard) Architecture

A PC mainboard is the printed circuit board (PCB) that serves as the central platform connecting core internal components of a computer.

### Core Components Connected by the Mainboard

- **CPU (Central Processing Unit)** - The processor
- **RAM (Random Access Memory)** - System memory
- **Data storage interfaces** - Connections for hard drives, SSDs
- **Transmission device interfaces** - Network cards, USB ports, etc.

## Bus Systems

Buses are the data lines that interconnect different components on the mainboard, enabling communication between them.

### Example: CPU-RAM Connection

The mainboard contains physical data lines (buses) that connect:
- The CPU socket (processor location)
- The RAM banks (memory slots)

This bus connection allows the CPU to read from and write to system memory, which is essential for program execution and data processing.

## Function of Buses

Buses serve as communication pathways that transfer:
- Data between components
- Control signals
- Memory addresses
- Power distribution

The physical traces on the PCB act as these buses, forming the infrastructure for all internal computer communication.

---

## Buses


Buses

What kinds of buses are there?

A parallel bus can send information across multiple data lines at a time and is normally shared by several devices.

Arbitration is required, as only one device can be “bus master” (occupy the bus) ata time

Synchronisation is also an issue – we needto make sure the data sent across the various lines arrive in the correct sequence


A parallel bus that extends beyond the main board by way of ribbon cable.


# Buses in Computer Systems

## Types of Buses

### Parallel Bus

A parallel bus is a communication pathway that can transmit information across multiple data lines simultaneously.

**Key Characteristics:**

- **Shared Resource**: Normally shared by several devices
- **Multiple Data Lines**: Sends data across multiple lines at the same time

## Technical Challenges in Parallel Bus Systems

### Arbitration

- Only one device can function as the "bus master" at any given time
- The bus master is the device that occupies and controls the bus
- Arbitration mechanisms are required to manage which device has control

### Synchronization

- Ensures data sent across various parallel lines arrives in the correct sequence
- Critical for maintaining data integrity
- Necessary because different data lines may have slight timing variations

## Physical Implementation

Parallel buses can extend beyond the main circuit board through the use of ribbon cables, allowing connection to external or peripheral devices.

---

## Buses


Buses

What kinds of buses are there?

A serial bus uses fewer data lines and can transmit data at higher frequency than a parallel bus,which can yield a higher net transfer rate.
Using fewer wires also makes them more practical for connecting external devices

Data are sent as “packets”, which include error checking and correction information.


Plug connectors for theUSB 3 Serial bus


# Buses in Information Systems

## Serial vs. Parallel Buses

### Serial Bus Characteristics
- Uses fewer data lines compared to parallel buses
- Can transmit data at higher frequencies
- Achieves higher net transfer rates despite using fewer lines
- More practical for connecting external devices due to reduced wire count

### Parallel Bus Characteristics
- Uses more data lines
- Lower frequency transmission
- Lower net transfer rate compared to serial buses

## Data Transmission in Serial Buses

### Packet-Based Communication
Data transmission occurs using packets that contain:
- The actual data being transmitted
- Error checking information
- Error correction information

This packet structure ensures data integrity during transmission.

## USB 3 Standard

USB 3 is an example of a serial bus technology that uses plug connectors for device connectivity.

---

## Networks


Networks

Scale

Networks connect computer systems:
Local Area Network (LAN) at home, or at a company/university
Metropolitan Area Network (MAN) size of a city
Wide Area Network (WAN) up to global scale, e.g. the networks that make up the Internet



# Network Scale Classification

## Core Concept

Networks connect computer systems and are classified based on their geographic scale and coverage area.

## Network Types by Scale

### Local Area Network (LAN)
- Smallest scale network
- Coverage: Single location (home, office, university campus, or company facility)
- Connects devices within a limited geographic area

### Metropolitan Area Network (MAN)
- Mid-scale network
- Coverage: City-sized area
- Spans across a metropolitan region

### Wide Area Network (WAN)
- Largest scale network
- Coverage: Regional to global scale
- Example: The Internet is composed of interconnected WANs
- Can span countries or continents

## Hierarchical Relationship

The networks form a hierarchy based on coverage area:
- LAN (smallest) → MAN (medium) → WAN (largest)
- Smaller networks can be components of larger networks
- Multiple LANs may connect to form a MAN
- Multiple MANs and LANs interconnect to form WANs

---

## Networks


Networks

Topology

Networks can be distinguished by their topology, for example


# Network Topology

## Definition

Network topology refers to the arrangement or layout pattern of interconnected devices (nodes) in a computer network. It defines how different nodes are placed and interconnected within a network.

## Key Concept

Networks can be distinguished and classified based on their topology, which determines:
- How devices are connected to each other
- The paths through which data flows
- The network's physical or logical structure

## Common Network Topologies

Networks are organized using various topological configurations, each with distinct characteristics affecting:
- Performance
- Scalability
- Fault tolerance
- Cost
- Ease of maintenance

---

## Networks


Networks

Physical data transmission and connectivity

Networks may use a variety of connection technologies , sometimes within the same network:

Transmission via copper wires

Wireless transmission

Optical signals via glass fibres


A home broadband router with a wireless networktransmitter

Ethernet connectors

Glass fibre cable


# Networks: Physical Data Transmission and Connectivity

## Connection Technologies in Networks

Networks utilize multiple types of connection technologies, often coexisting within the same network infrastructure:

### 1. Transmission via Copper Wires
- Uses electrical signals to transmit data through copper cables
- Commonly implemented through Ethernet connectors
- Traditional and widely deployed technology for wired networking

### 2. Wireless Transmission
- Enables data transfer without physical cables
- Implemented through devices such as wireless network transmitters
- Often integrated into home broadband routers
- Provides mobility and flexible connectivity

### 3. Optical Signals via Glass Fibres
- Uses light pulses transmitted through glass fibre cables
- Provides high-speed, high-bandwidth data transmission
- Less susceptible to electromagnetic interference compared to copper
- Enables long-distance data transfer with minimal signal loss

## Key Infrastructure Components

**Ethernet Connectors**: Physical interfaces that enable copper wire-based network connections

**Wireless Network Transmitter**: Device component that broadcasts and receives wireless signals, frequently built into home broadband routers

**Glass Fibre Cable**: Physical medium composed of thin glass strands used for optical signal transmission

## Hybrid Network Design

Modern networks commonly employ a combination of these technologies to optimize for different requirements such as cost, distance, bandwidth, and mobility needs.

---

## Networks


Networks

Network interfaces and devices

The network interface (NI) connects a network node (e.g. computer or printer) to the computer network.

Most computers today have a network interface included on their mainboard; those that don’t usea network interface card (NIC - image) or a wireless transmitter/receiver


A network interface card


# Network Interfaces and Devices

## Network Interface (NI)

A network interface connects a network node to the computer network. Network nodes include devices such as:
- Computers
- Printers

## Implementation Methods

### Integrated Network Interface
Most modern computers have a network interface built directly into their mainboard (motherboard).

### External Network Interface Options
For computers without integrated network interfaces, two primary options exist:

1. **Network Interface Card (NIC)**
   - A physical expansion card installed in the computer
   - Provides wired network connectivity

2. **Wireless Transmitter/Receiver**
   - Enables wireless network connectivity
   - Alternative to wired NIC solutions

## Key Terminology

- **NI (Network Interface)**: The general term for any device that connects a node to a network
- **NIC (Network Interface Card)**: A specific type of network interface implemented as an expansion card for wired connections

---

## Networks


Networks

Network interfaces and devices

A switch connects different computers (nodes) on the same network

The switch will examine the packets passing through, learns the addresses of the nodes, and forwards data packets to their correct destination

A professional switch in the 19" form factor


# Network Switches

## Definition and Function

A **switch** is a network device that connects different computers (nodes) on the same network.

## How Switches Operate

The switch performs three key functions:

1. **Examines packets** - Analyzes data packets passing through the device
2. **Learns addresses** - Identifies and remembers the addresses of connected nodes
3. **Forwards packets** - Directs data packets to their correct destination based on learned addresses

## Physical Form Factor

Switches are available in professional configurations, including the 19" rack-mountable form factor, which is a standard size for mounting equipment in server racks and network cabinets.

## Key Characteristics

- Operates at the data link layer (Layer 2) of the network
- Provides dedicated bandwidth between connected devices
- Intelligently routes traffic only to the intended recipient, unlike hubs which broadcast to all ports
- Creates a more efficient network by reducing unnecessary traffic

---

## Networks


Networks

Network interfaces and devices

A router connects different networks, such as a LAN and a WAN

Can translate network protocol addresses between the networks, and also filter out packets

A home broadband router


# Routers in Network Architecture

## Definition and Primary Function

A **router** is a network device that connects different types of networks together, such as:
- Local Area Networks (LANs)
- Wide Area Networks (WANs)

## Key Capabilities

### Protocol Address Translation
- Routers can translate network protocol addresses between different networks
- This enables communication between networks that may use different addressing schemes

### Packet Filtering
- Routers have the ability to filter out packets
- This provides basic security and traffic management by controlling which data packets are allowed to pass between networks

## Practical Application

### Home Broadband Router
Home broadband routers represent a common implementation of router technology, typically:
- Connecting a home LAN to the Internet (WAN)
- Providing network address translation (NAT)
- Often including additional features like wireless access points and firewalls

---

## Networks


Networks

Ethernet

The most common form of wired network technology today

The design dates back to 1973, and has its originat Xerox PARC



# Ethernet

## Definition
Ethernet is the most common form of wired network technology in use today.

## Historical Background
- Design originated in 1973
- Developed at Xerox PARC (Palo Alto Research Center)

## Significance
Ethernet has maintained its position as the dominant wired networking standard for several decades, demonstrating its robustness and adaptability to evolving networking needs.

---

## Networks


Networks

Example


Internet


# Networks

## Network Example

A network consists of multiple interconnected devices that can communicate with each other and share resources.

### Network Structure

The example illustrates a typical network configuration where multiple devices (computers, laptops, and other networked devices) connect to the Internet through a central network infrastructure. This demonstrates:

- **Local Area Network (LAN)**: Multiple devices within a localized area connected together
- **Internet Connectivity**: The local network connects to the broader Internet infrastructure
- **Network Topology**: Devices arranged in a way that allows them to communicate both with each other locally and with external resources via the Internet

### Key Network Components

- **End Devices**: Individual computers and devices that use network services
- **Network Infrastructure**: Equipment that facilitates connections between devices
- **Internet Gateway**: Point of connection between the local network and the Internet

This configuration represents a common networking scenario found in homes, offices, and educational institutions where multiple devices need both local connectivity and Internet access.

---

## The Internet


The Internet

A network of networks

The Internet combines a growing number of networks, which transmit data packets between each other.
The packets reach their destinations after a series of ‘hops’ between communicating machines.



# The Internet

## Core Definition

The Internet is a **network of networks** - a global system that interconnects multiple individual networks together.

## Data Transmission Architecture

### Packet-Based Communication

- Data is transmitted across the Internet in the form of **data packets**
- These packets are discrete units of information that travel independently through the network

### Packet Routing Process

Packets reach their intended destinations through a **series of 'hops'**:
- Each hop represents a transfer between communicating machines (routers, servers, switches)
- Packets don't travel in a single direct path
- Instead, they jump from one network node to another until reaching the final destination

## Network Interconnection

The Internet operates by:
- Combining a growing number of individual networks
- Enabling these networks to transmit packets between each other
- Creating a distributed system where no single path is required for communication

---

## The Internet


The Internet

Internet exchanges

Independent networks make peering arrangements to exchange traffic, via Internet exchanges or direct, private interconnections.


# Internet Exchanges

## Core Concept

**Internet Exchanges** are connection points where independent networks establish peering arrangements to exchange traffic with each other.

## How Networks Interconnect

Independent networks on the Internet can exchange traffic through two main methods:

1. **Internet Exchanges (IXs)** - Centralized facilities where multiple networks connect and peer
2. **Direct Private Interconnections** - Point-to-point connections established directly between two networks

## Peering Arrangements

**Peering** refers to agreements between networks to exchange traffic. These arrangements enable:

- Traffic flow between different autonomous networks
- Distributed architecture of the Internet
- Efficient routing of data across network boundaries
- Cost-effective data exchange without intermediate carriers

## Significance

Internet exchanges are critical infrastructure that:
- Enable the decentralized structure of the Internet
- Allow independent networks to maintain autonomy while interconnecting
- Facilitate efficient data routing across the global Internet
- Reduce reliance on transit providers for inter-network communication

---

## The Internet


- Internet protocols
Protocols are important for the orderly transmission of information across a network – they represent the standard “languages” and conventions with which information is communicated
Different protocols are used for different purposes. The “Internet protocol suite” is also referred to as “TCP/IP”,  naming two of its fundamental protocols
A few examples of common network protocols that are used on the Internet are
- IP
- TCP
- ICMP
- UDP

---

## The Internet


The Internet

Network communication

The complexity of networks is controlled through abstraction
One standard approach is the Open Systems Interconnection Model (OSI),
The OSI model provides a logical network abstractions in the form of layers,where lower level layers implementfunctions used at higher-level layers
TCP/IP implements some of these layers



# Network Communication and Abstraction

## Managing Network Complexity

Network complexity is controlled through **abstraction** - breaking down complex systems into manageable, logical components.

## Open Systems Interconnection (OSI) Model

The OSI model is a standard approach for organizing network functionality.

### Key Characteristics

- Provides logical network abstractions organized into **layers**
- Uses a hierarchical structure where each layer builds upon the one below it
- Lower-level layers implement functions that are used by higher-level layers
- This layered approach simplifies network design and troubleshooting

## TCP/IP Protocol Suite

TCP/IP (Transmission Control Protocol/Internet Protocol) is a practical implementation that incorporates some of the OSI model layers. It serves as the foundation for Internet communications.

### Relationship to OSI

- TCP/IP implements a subset of the OSI layers
- Demonstrates the practical application of layered network architecture
- Enables standardized communication across the Internet

---

## The Internet


- Internet protocol (IP, Internet Layer)
Wraps data into packets and sends them off in the right order
Is an unreliable protocol (not because it does not work well, but because if there is an error, it is not reported back to the sender or the recipient).
Is connectionless : packets are launched towards their recipient without establishing a connection first.
Packets can arrive in any order, and may be lost, duplicated or corrupted.
Current version is IPv4, but we are now moving to IPv6.
Key task: making decisions about how to route packets through the network
How does the IP protocol know where to send the information?

---

## The Internet


- Internet addresses
Nodes on the Internet become identifiable through numerical addresses, also known as IP addresses.
A data packet carries the destination address in its header, and routers move those packets accordingly.
With IPv4, addresses are 32 bits wide. So, we can have 4.3 billion nodes, in principle. Since this is no longer enough, the new IPv6 offers 128 bit addresses.
Addresses assigned by Internet Corporation for Assigned Names and Numbers (ICANN).
- Addresses are written in “dotted decimal” notation, e.g. 139.184.24.3

---

## The Internet


- Transmission Control Protocol (TCP, Transport Layer)
Accepts data in the form supplied by an application program (such as a web server or email client) and breaks it into packets which can be given to the Internet protocol (IP) for transmission.
Reassembles packets received over the Internet into a form suitable to give to applications programs.
Can control the flow of data to slow down transmission if the receiver can’t keep up, for example.

---

## The Internet


- Transmission Control Protocol (TCP, Transport Layer)
Is a reliable protocol: checks that all packets have arrived and are correct. Will ask for retransmission if there is a problem.
Uses connections : gets acknowledgement from recipient before sending data.
Puts reliability above speed: so not always good for streaming video or audio data. (Connectionless alternatives such as UDP exist for higher speed at the expense of reliability).
Uses port numbers to establish connections between specific programs running on different computers.Which common TCP ports do you know?

---

## The Internet


- Domain names and IP addresses
Nodes on the Internet are identifiable through IP addresses.
Since IP addresses are not easy to read or remember, we use alphanumerical domain names, e.g. www.sussex.ac.uk
Domain names also use a dot notation to specify the location of the host within a hierarchy of higher-level domains, decreasing in size when read from the right:www is the name of the server hosting the University website within the domain sussex, which lives under the domain ac (academic institutions), under the country’s top-level domain uk.
The domain name has to be translated into a numerical address before a packet can be sent.How can we find out the IP address matching www.sussex.ac.uk?

---

## The Internet


- Domain Name System (DNS)
The translation between domain names and IP addresses is achieved by sending a request to a name server. Name servers maintain a continuously updated, distributed database, which maps alphanumerical domain names to numerical IP addresses.
Name servers form the domain name system; the process of obtaining the IP address is called DNS lookup
DNS allows a single physical computer to support many domains, because we can map different domain names to the same IP address.The web servers of Internet service providers make use of this fact to save money by hosting the websites of many of their customers on the same physical infrastructure

---

## Summary


Buses and Networks are technologies for transmitting information between computing components and devices
- There are parallel and serial buses, which have different properties
- Ethernet is the most common network technology today
Switches and routers are common network appliances that facilitate the transfer of information within and between networks
- The Internet is a growing collection of interconnected networks
The complexity of physical network communication is mapped to layered models
Protocols ensure orderly communication across networks / the Internet, e.g. TCP/IP
We use the domain name system to translate between IP addresses, which uniquely identify hosts on the Internet, and domain names

---

## Read


- Brookshear & Brylow
Computer Science: An Overview. Pearson Education, 12th edition, 2015.
- Available online, there are also physical copies in the library
- Chapter 4.1, 4.2, 4.4

---

## Next Lecture


- The world-wide web and HTTP
- HTML

---
