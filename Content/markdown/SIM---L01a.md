# SIM   L01a

**Conversion date:** 2026-01-11
**Original file:** `SIM - L01a.pptx`
**Total slides:** 33

---


## Table of Contents

1. [Systems for Information ManagementLecture 1a](#slide-1-systems-for-information-managementlecture-1a)
2. [Module Overview](#slide-2-module-overview)
3. [Technical requirements / Software](#slide-3-technical-requirements--software)
4. [Technical requirements / Attendance](#slide-4-technical-requirements--attendance)
5. [About Myself](#slide-5-about-myself)
6. [Today](#slide-6-today)
7. [Basic Concepts](#slide-7-basic-concepts)
8. [What is a Computer?](#slide-8-what-is-a-computer)
9. [What is a Computer?](#slide-9-what-is-a-computer)
10. [What is a Computer?](#slide-10-what-is-a-computer)
11. [Resources](#slide-11-resources)
12. [Resources](#slide-12-resources)
13. [Resources](#slide-13-resources)
14. [Resources](#slide-14-resources)
15. [Resources](#slide-15-resources)
16. [Resources](#slide-16-resources)
17. [Resources](#slide-17-resources)
18. [Resources](#slide-18-resources)
19. [Resources](#slide-19-resources)
20. [CPU-RAM Interaction](#slide-20-cpu-ram-interaction)
21. [Physical aspects](#slide-21-physical-aspects)
22. [Physical aspects](#slide-22-physical-aspects)
23. [Physical aspects](#slide-23-physical-aspects)
24. [Logical aspects](#slide-24-logical-aspects)
25. [Logical aspects](#slide-25-logical-aspects)
26. [Logical aspects](#slide-26-logical-aspects)
27. [Information processing with Logic Circuits](#slide-27-information-processing-with-logic-circuits)
28. [Information storage with Logic Circuits](#slide-28-information-storage-with-logic-circuits)
29. [Summary](#slide-29-summary)
30. [Summary](#slide-30-summary)
31. [Read](#slide-31-read)
32. [Watch](#slide-32-watch)
33. [Next Lecture](#slide-33-next-lecture)

## 1. Systems for Information ManagementLecture 1a {#slide-1-systems-for-information-managementlecture-1a}

### Content

- Dr Imran U Khan  	School of Engineering and Informatics

---

## 2. Module Overview {#slide-2-module-overview}

### Content

Learn how computer systems work and how their core components are interrelated
- Get to know fundamental Internet and Web Technologies
- Learn how to store and manipulate information in databases
- Get to know basic computer security principles

- Computer organisation

- Hardware & Software

- Client-server communication

- Scripting

- Internet and Web, HTTP

- Database schemas

- Data modelling

- Encryption

- Access Control

- HTML, XML, CSS

- 2

---

## 3. Technical requirements / Software {#slide-3-technical-requirements--software}

### Content

A PC or laptop with a web browser is sufficient to access all teaching content.Get a microphone / web cam if you’d like to participate in class beyond using the chat
Double-check you have a Java Runtime Environment installedhttps://www.oracle.com/java/technologies/javase-jre8-downloads.html
Notepad++ or any other plain-text editing softwareFor simple code exercises with HTML, XML, CSS, Javascript, etc.https://notepad-plus-plus.org/
Mid-term: XAMPPOnly needed later for database / web exerciseshttp://www.sussex.ac.uk/its/services/software/list?filter=exceedondemand&id=436

- 3

---

## 4. Technical requirements / Attendance {#slide-4-technical-requirements--attendance}

### Content

In line with common practice, we will use the Sussex Mobile App to record attendance in all our lectures and labs.You can download it from the Apple AppStore or Google PlayStore on to your phone.Read more about it here: https://student.sussex.ac.uk/mobile-app
If you prefer, the app can also be run in the browser at https://www.sussex.ac.uk/mobile

- 4

---

## 5. About Myself {#slide-5-about-myself}

### Content

- Imran Khan
- School of Engineering and Informatics
- Department of Informatics
- Office hours: 	Appointments by e-mail
- E-mail: 			Imran.khan@sussex.ac.uk

- 5

---

## 6. Today {#slide-6-today}

### Content

- Let’s get started
- Basic concepts of computing
- Examples of computer hardware components and what they do
- The physical and logical perspective on computer systems

- 6

---

## 7. Basic Concepts {#slide-7-basic-concepts}

### Content

What is a computer?

- 7

---

## 8. What is a Computer? {#slide-8-what-is-a-computer}

### Content

- Some ways to talk about computer systems:
- Wires, transistors, capacitors, voltages and currents
- Integrated circuits, logic gates and bit patterns
- Machine code, file systems, transmission protocols and bytes
- Programs, computer languages and data formats
- Applications and user interfaces
- Physical devices: input and output of data
- Networks of computers and the Internet

- 8

---

## 9. What is a Computer? {#slide-9-what-is-a-computer}

### Content

Informally, a computer is an Information Processing System: It processes information by executing lists of instructions.
The processing, storage, and transmission of information are important aspects of what modern computers do.

- 9

---

## 10. What is a Computer? {#slide-10-what-is-a-computer}

### Content

What is a Computer?

More formally, a computer is based on a mathematical model that breaks down general-purpose computation into its basic, elementary steps: The Universal Turing machine (UTM)




Core concepts: A stored program, state register, memory.
For a device to be called a general-purpose computer it must be equivalent in capability to a UTM.

10

### Visual Analysis

# Formal Definition of a Computer

## Mathematical Foundation

A computer is formally based on a mathematical model that decomposes general-purpose computation into elementary steps. This model is the **Universal Turing Machine (UTM)**.

## Core Components

A computer based on the UTM model requires three fundamental concepts:

- **Stored program**: Instructions are stored in memory rather than hardwired
- **State register**: Tracks the current state of computation
- **Memory**: Storage for both data and instructions

## General-Purpose Computer Criterion

For a device to qualify as a **general-purpose computer**, it must meet the following requirement:

- The device must be equivalent in computational capability to a Universal Turing Machine

This equivalence means the device can theoretically compute anything that is computable, given sufficient time and memory resources.

---

## 11. Resources {#slide-11-resources}

### Content

Resources

Physical resources

Physical resources are devices that are part of or connected to a computer

Can you identify some of these resources in the image?

11

### Visual Analysis

# Physical Resources in Information Systems

## Definition

**Physical resources** are devices that are part of or connected to a computer system.

## Key Concept

Physical resources represent the tangible, hardware components that comprise or interface with computing systems. These are the concrete, material elements that enable computer systems to function and interact with users and other systems.

## Examples of Physical Resources

Common physical resources include:

- Input devices (keyboards, mice, scanners, cameras)
- Output devices (monitors, printers, speakers)
- Storage devices (hard drives, SSDs, USB drives, optical drives)
- Processing units (CPUs, GPUs)
- Memory modules (RAM)
- Network devices (network cards, routers, modems)
- Peripheral devices (external drives, game controllers, microphones)

## Significance

Physical resources form the foundation of any computing system and must be managed effectively by the operating system and other software components to ensure proper system operation and resource allocation.

---

## 12. Resources {#slide-12-resources}

### Content

How do resources relate to what computers do?
- Examples:
- Memory  Storage of data short-term or long-term
Central Processor  Processing of data, e.g. calculations, logic, or memory manipulation
- Networks & buses  Transmission of data / control

- 12

---

## 13. Resources {#slide-13-resources}

### Content

Resources

CPU

Physical resources are devices that are part of or connected to a computer

      Examples:

Central Processing Unit
(CPU)

13

### Visual Analysis

# Physical Resources in Computing

## Definition

**Physical resources** are devices that are part of or connected to a computer.

## Example: Central Processing Unit (CPU)

The CPU is a fundamental physical resource that serves as the primary processor of a computer system. It executes instructions and performs calculations necessary for computer operations.

---

## 14. Resources {#slide-14-resources}

### Content

Resources

RAM

Physical resources are devices that are part of or connected to a computer

      Examples:

Random Access Memory
(RAM)

14

### Visual Analysis

# Physical Resources in Computer Systems

## Definition

**Physical resources** are devices that are part of or connected to a computer.

## Example: Random Access Memory (RAM)

RAM (Random Access Memory) is a primary example of a physical resource. It is a hardware component that is part of the computer system and serves as the computer's main working memory for active processes and data.

---

## 15. Resources {#slide-15-resources}

### Content

Resources

Storage

Physical resources are devices that are part of or connected to a computer

      Examples:

Hard-Disk Drive
(HDD)

15

### Visual Analysis

# Storage Resources

## Definition

Physical resources are devices that are part of or connected to a computer.

## Example

**Hard-Disk Drive (HDD)** - A type of physical storage device used in computer systems.

---

## 16. Resources {#slide-16-resources}

### Content

Resources

Central Processing Unit

The CPU is the "brain" of a computer
Handles essential data processing such as numerical computation, as well as logic, control, and input/output operations

16

### Visual Analysis

# Central Processing Unit (CPU)

## Definition

The CPU is the "brain" of a computer.

## Functions

The CPU handles essential data processing operations, including:

- **Numerical computation** - performing mathematical calculations
- **Logic operations** - executing logical decisions and comparisons
- **Control operations** - coordinating and managing other computer components
- **Input/output operations** - managing data transfer between the computer and external devices

---

## 17. Resources {#slide-17-resources}

### Content

Resources

Primary memory

RAM is the "short-term memory" of a computer
Has a fast-track connection to the CPU
Can access data very quickly
Has very high read and write speed
Capacity is limited, though
Cannot hold any data without power (volatile memory)
RAM is also called “Primary memory”

17

### Visual Analysis

# Primary Memory (RAM)

## Definition
RAM (Random Access Memory) serves as the "short-term memory" of a computer and is also called "Primary memory."

## Key Characteristics

### Performance Features
- **Fast CPU connection**: Has a fast-track connection to the CPU
- **Quick data access**: Can access data very quickly
- **High read/write speed**: Provides very high speed for both reading and writing operations

### Limitations
- **Limited capacity**: Storage capacity is restricted compared to other storage types
- **Volatile memory**: Cannot hold any data without power - all data is lost when power is turned off

## Functional Role
RAM acts as the working memory for active programs and data, providing rapid access for the CPU to perform computations and process information in real-time.

---

## 18. Resources {#slide-18-resources}

### Content

Resources

Secondary Memory

The HDD is an example for a device representing a computer’s "long-term memory“, also called “Secondary memory”
A HDD has mechanical parts and is much slower than RAM as a result:
Data access time 1 - 8 ms (RAM: 10-50 ns)
Read and write speeds 20 - 100 MB/s(RAM 5 - 25 GB/s)

Can store large amounts of data
Can hold data even without power (persistent memory)
Bound to be around for a while longer as solid-state disk (SSD) memory is still more expensive in comparison

18

### Visual Analysis

# Secondary Memory

## Hard Disk Drive (HDD) Characteristics

HDD represents a computer's "long-term memory," also referred to as "Secondary memory."

### Physical Properties
- Contains mechanical parts
- Significantly slower than RAM due to mechanical components

### Performance Metrics

**Data Access Time:**
- HDD: 1-8 milliseconds (ms)
- RAM (comparison): 10-50 nanoseconds (ns)

**Read and Write Speeds:**
- HDD: 20-100 MB/s
- RAM (comparison): 5-25 GB/s

### Key Advantages

1. **Large Storage Capacity**: Can store substantial amounts of data
2. **Persistent Memory**: Retains data even without power supply
3. **Cost-Effectiveness**: Remains competitive as solid-state disk (SSD) memory is still more expensive in comparison

### Market Position

HDDs are expected to remain in use for the foreseeable future due to the higher cost of SSD alternatives.

---

## 19. Resources {#slide-19-resources}

### Content

Resources

Virtual Resources

Based on our physical devices, we can specify virtual resources, like files, network connections, memory addresses, or CPU computing cycles.

For example, the storage capacity of a hard disk, or the clock frequency of a CPU, or the bandwidth of a network connection gives a measure of how much resource of a certain type is available

19

### Visual Analysis

# Virtual Resources in Information Systems

## Definition

Virtual resources are abstractions built on top of physical computing devices. They provide a logical view of system resources independent of the underlying hardware implementation.

## Types of Virtual Resources

- **Files**: Logical containers for data storage
- **Network connections**: Abstract communication channels between systems
- **Memory addresses**: Logical references to storage locations
- **CPU computing cycles**: Units of processing time allocation

## Resource Measurement

Physical devices provide quantifiable measures of available virtual resources:

- **Hard disk storage capacity**: Determines the amount of file storage space available
- **CPU clock frequency**: Indicates the number of computing cycles available per unit time
- **Network bandwidth**: Measures the data transfer capacity of network connections

## Relationship Between Physical and Virtual Resources

Virtual resources are derived from and constrained by the capabilities of physical hardware. The physical characteristics (capacity, frequency, bandwidth) define the upper limits of what virtual resources can provide to applications and users.

---

## 20. CPU-RAM Interaction {#slide-20-cpu-ram-interaction}

### Content

How do the CPU and the RAM work together?
We need to store the data and the instructions of our program so that the CPU can access them as needed to run our program, and store any results of the computation, intermediate and final.

- RAM

- CPU

- Program Data

- Program Instructions

- Arithmetic Unit

- Control Unit

- Inputs

- Outputs

- Operating System and other programs

- Free

- 20

---

## 21. Physical aspects {#slide-21-physical-aspects}

### Content

Physical aspects

How do computers work at the fundamental physical level ?

Today’s digital electronic computers contain a huge number of logic circuitsthat are made up from huge quantities of highly miniaturised transistors.
These transistors are operated by electricity.
The voltage of a control signal (high or low) will determine whether a transistor will let a current pass through or not

21

### Visual Analysis

# Physical Fundamentals of Computer Operation

## Core Question
How do computers work at the fundamental physical level?

## Digital Electronic Computer Architecture

### Basic Components
Modern digital electronic computers are built from:
- **Logic circuits**: Fundamental building blocks of computer processing
- **Transistors**: Highly miniaturized electronic components present in huge quantities

### Transistor Operation

**Power Source**: Transistors are operated by electricity

**Control Mechanism**: 
- A control signal's voltage level (high or low) determines transistor behavior
- The voltage determines whether a transistor permits electrical current to pass through or blocks it

**Binary Operation**:
- High voltage = transistor conducts current (ON state)
- Low voltage = transistor blocks current (OFF state)

This binary switching mechanism forms the foundation for digital computation, where information is represented and processed using two-state logic.

---

## 22. Physical aspects {#slide-22-physical-aspects}

### Content

- Transistors
A transistor is a semiconductor, i.e. based on materials that give it dynamic electrical properties. Transistors are often used as electronic switches. Some advantages of transistors:
- Small in size
- Low weight
- Low power consumption
- Less heat emission than vacuum tubes
- Physically robust

---

## 23. Physical aspects {#slide-23-physical-aspects}

### Content

- CMOS
Complementary-symmetrical Metal–Oxide–Semiconductor is a technology used for building digital logic circuits and fast memory.
The word “complementary-symmetrical” refers to a design aspect specific of CMOS technology: The combined use of two different types of transistor.

---

## 24. Logical aspects {#slide-24-logical-aspects}

### Content

How do computers work at the fundamental logical level ?
Multiple transistors of different type can be arranged in logic gates to implement well-known logic functions (e.g., NOT, AND, OR, XOR, etc.)
These logic gates are then used to construct larger arrays of logic circuits that drive the elementary functions of a CPU, forexample.

- 24

---

## 25. Logical aspects {#slide-25-logical-aspects}

### Content

Logical aspects

Example: Inverter logic gate (“NOT”)

A CMOS inverter is in one of two states, so is a binary device (like almost all elements of a digital computer):
Made from a complementary and symmetrical pair of p-type and n-type metal oxide semiconductor field effect transistors (MOSFETs)
The transistors have 3 connections and act as switches 
When “In” is set to high voltage, the (upper) p-type transistor’s channel is in a high-resistance state and the (lower) n-type transistor’s channel is in a low-resistance state, so the output will be ground voltage
Conversely, the output will be high voltage when “In” is set to ground voltage.
This logic gate will always invert the signal received at “In”!

Circuit diagram symbol for a NOT logic gate

Truth table for a NOT logic gate

CMOS Layout of a NOT logic gate

### Visual Analysis

# CMOS Inverter Logic Gate (NOT Gate)

## Core Concept

A CMOS inverter is a fundamental binary digital device that implements a NOT logic gate. It exists in one of two states, functioning as the basic building block of digital computers.

## Physical Construction

**CMOS Structure:**
- Built from a complementary and symmetrical pair of transistors:
  - p-type MOSFET (Metal Oxide Semiconductor Field Effect Transistor)
  - n-type MOSFET
- Each transistor has 3 connections
- Transistors function as switches

## Operating Principles

### High Input State
- Input ("In") receives high voltage
- Upper p-type transistor channel → high-resistance state
- Lower n-type transistor channel → low-resistance state
- **Output:** ground voltage (low)

### Low Input State
- Input ("In") receives ground voltage (low)
- Upper p-type transistor channel → low-resistance state
- Lower n-type transistor channel → high-resistance state
- **Output:** high voltage

## Logic Behavior

**Signal Inversion:** The gate always inverts the signal received at the input. When input is high, output is low; when input is low, output is high.

## Truth Table

| Input (In) | Output |
|------------|--------|
| 0 (Low)    | 1 (High)|
| 1 (High)   | 0 (Low) |

## Key Characteristic

The NOT gate performs logical negation - it produces the opposite of its input value, making it an essential component for implementing more complex digital logic circuits.

---

## 26. Logical aspects {#slide-26-logical-aspects}

### Content

Logical aspects

NAND logic gate

A NAND (“NOT AND”) gate has two inputs (A and B in the diagram) and one output. 
With CMOS, there are two p-type transistors in parallel and two corresponding n-type transistors in series. 
NAND is important for computing systemsbecause it is a “Universal logic gate”.That means NAND circuits can be arranged to reproduce other logic functions.(The other universal logic gate is NOR)
What does the truth table for a NAND gate look like?

### Visual Analysis

# NAND Logic Gate

## Definition
A NAND gate is a "NOT AND" logic gate with two inputs (A and B) and one output.

## CMOS Implementation
The NAND gate is constructed using CMOS technology with:
- Two p-type transistors arranged in parallel
- Two n-type transistors arranged in series (corresponding to the p-type transistors)

## Universal Logic Gate
NAND is a universal logic gate, meaning:
- NAND circuits can be arranged and combined to reproduce any other logic function
- All digital circuits can be built using only NAND gates
- NOR is the other universal logic gate

## Significance for Computing Systems
The universal property of NAND gates makes them critically important for computing systems, as they provide the fundamental building block for constructing all digital logic operations.

## Truth Table
The truth table for a NAND gate operates as the inverse of an AND gate:

| Input A | Input B | Output |
|---------|---------|--------|
| 0       | 0       | 1      |
| 0       | 1       | 1      |
| 1       | 0       | 1      |
| 1       | 1       | 0      |

The output is 0 only when both inputs are 1; otherwise, the output is 1.

---

## 27. Information processing with Logic Circuits {#slide-27-information-processing-with-logic-circuits}

### Content

Information processing with Logic Circuits

How does information processing work with logic circuits, in principle?

Electrical signals (e.g., low and high voltage) control the operation of transistors.
Transistors are arranged to implement logic gates.
Logic gates are combined to create higher-level devices, called logic circuits.
Logic circuits perform operations (manipulate multiple electric signals) in order to performdifferent arithmetic or logic operations.

A logic circuit for adding numbers

27

### Visual Analysis

# Information Processing with Logic Circuits

## Fundamental Principle

Information processing in logic circuits operates through a hierarchical structure, where each level builds upon the previous one to enable computation.

## Architecture Layers

### 1. Electrical Signals
- Electric signals with different voltage levels (low voltage and high voltage) serve as the foundation
- These signals control transistor operation

### 2. Transistors
- Transistors respond to electrical signals
- They are arranged in specific configurations to create logic gates

### 3. Logic Gates
- Built from transistor arrangements
- Implement basic logical operations
- Serve as building blocks for more complex circuits

### 4. Logic Circuits
- Created by combining multiple logic gates
- Represent higher-level functional devices
- Perform operations by manipulating multiple electric signals simultaneously

## Operations Performed

Logic circuits enable two main categories of operations:

- **Arithmetic operations**: Mathematical calculations
- **Logic operations**: Boolean and logical computations

## Practical Example

**Adding numbers**: Logic circuits can be designed specifically to perform addition, demonstrating how the hierarchical structure translates into practical computational functionality.

---

## 28. Information storage with Logic Circuits {#slide-28-information-storage-with-logic-circuits}

### Content

Information storage with Logic Circuits

How does data storage work with logic circuits, in principle?

A flip-flop is a simple circuit that can store and retain binary state information. 
There are different ways to construct a flip flop, the figure on the right shows an example.
The state of this device can be changed by applying a pulse of HIGH voltage on the upper or lower input, respectively, depending on what the current state of the device is. 
The key characteristic of a flip-flop is that it retains the current state even if the latest input pulse returns to LOW / 0. The state will only change againif there is another input pulse. 
This makes a flip-flop a useful circuit for storing information!

### Visual Analysis

# Information Storage with Logic Circuits

## Flip-Flops for Data Storage

A **flip-flop** is a fundamental circuit component that stores and retains binary state information (0 or 1).

## How Flip-Flops Work

### State Changes
- The state of a flip-flop can be changed by applying a pulse of HIGH voltage to one of its inputs
- Which input to use (upper or lower) depends on the current state of the device
- The specific input required varies based on whether the device is currently storing a 0 or 1

### Key Characteristic: State Retention
The defining feature of a flip-flop is **memory persistence**:
- Once an input pulse is applied and the state changes, the flip-flop retains that new state
- The state remains stable even after the input pulse returns to LOW/0
- The state will only change again when another input pulse is applied

### Construction
Multiple circuit designs can implement flip-flop functionality, demonstrating different approaches to achieving the same storage capability.

## Application

This state retention property makes flip-flops essential building blocks for information storage in digital systems. By maintaining their state without continuous power to the input, flip-flops enable:
- Memory circuits
- Data registers
- Sequential logic systems
- Binary information storage

---

## 29. Summary {#slide-29-summary}

### Content

Summary

Ways of talking about a computing system

Different levels of abstraction 
Physical and logical perspectives

29

Transistors

Logic gates

Logic circuits

Integrated circuits

### Visual Analysis

# Computing System Abstraction Levels

## Core Concept

Computing systems can be understood and analyzed at multiple levels of abstraction, ranging from the physical components to logical representations. This layered approach allows different perspectives when working with computer systems.

## Key Perspectives

**Physical Perspective**: The tangible, hardware components and their actual implementation

**Logical Perspective**: The abstract, conceptual representation of how systems function

## Hierarchy of Abstraction Levels

The computing system can be described at four fundamental levels, from lowest to highest:

1. **Transistors** - The basic electronic switches that form the foundation of digital circuits
2. **Logic Gates** - Combinations of transistors that perform basic logical operations (AND, OR, NOT, etc.)
3. **Logic Circuits** - Networks of logic gates that perform more complex operations
4. **Integrated Circuits** - Complete functional units combining multiple logic circuits on a single chip

## Significance

Understanding these different abstraction levels allows professionals to:
- Work at the appropriate level of detail for their task
- Communicate effectively about system components
- Design and troubleshoot at various system layers
- Bridge the gap between physical hardware and logical functionality

---

## 30. Summary {#slide-30-summary}

### Content

Most modern computers are based upon integrated electronic circuits that use transistors to perform different logic and arithmetic operations.
Modern computers are information processing systems that require resources to function.
Physical resources provide the basis for virtual resources that are needed for the processing, storage, or transmission of information.

- 30

---

## 31. Read {#slide-31-read}

### Content

- Brookshear & Brylow
Computer Science: An Overview. Pearson Education, 12th edition, 2015.
- Available online, there are also physical copies in the library
- Chapter 0 (optional), Chapter 1

- 31

---

## 32. Watch {#slide-32-watch}

### Content

Watch

Lecture on Computers and Heuristics by Richard Feynman (1985) 
	https://www.youtube.com/watch?v=EKWGGDXe5MA
"Dumber but faster" – on how computers work internally: from the start, ca. 38 mins.
Search: from 43:30 – 51:30min
Humans and Machines: Subsequent Q&A

32

### Visual Analysis

# Educational Resource: Richard Feynman Lecture on Computers and Heuristics

## Resource Information

**Title:** Computers and Heuristics Lecture by Richard Feynman (1985)

**Source:** https://www.youtube.com/watch?v=EKWGGDXe5MA

## Key Topics and Timestamps

### How Computers Work Internally
- **Start time:** Beginning of lecture (approximately 38 minutes of content)
- **Key concept:** "Dumber but faster" - describes the fundamental nature of computer operation
- Computers perform simple operations at high speed rather than complex intelligent operations

### Search Algorithms
- **Time range:** 43:30 - 51:30 minutes
- Covers search methodologies and approaches
- Discussion of heuristic methods in computational search

### Humans and Machines
- **Section:** Q&A session following main lecture
- Explores the relationship and differences between human cognition and machine computation
- Examines comparative advantages and limitations of each

## Educational Context

This lecture provides foundational understanding of:
- Computer architecture and fundamental operations
- Search algorithms and heuristic approaches
- The philosophical and practical distinctions between human thinking and machine computation

---

## 33. Next Lecture {#slide-33-next-lecture}

### Content

- How software is run on computers
- How data and instructions are stored in memory

- 33

---


---

## Processing Metadata

### Slide Classification
- Text slides: 17
- Visual slides: 16
- Optimized percentage (without API): 51.5%

### API Costs
- Input tokens: 34,776
- Output tokens: 6,930
- Total cost: $0.2083 USD

### System
- Generated by: PPTX to Markdown Converter
- Date: 2026-01-11 19:07:24