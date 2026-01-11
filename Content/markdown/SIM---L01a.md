# Systems for Information Management - Lecture 1a

## Module Overview

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

## Technical Requirements

### Software

A PC or laptop with a web browser is sufficient to access all teaching content. Get a microphone / web cam if you'd like to participate in class beyond using the chat.

- Double-check you have a Java Runtime Environment installed: https://www.oracle.com/java/technologies/javase-jre8-downloads.html
- Notepad++ or any other plain-text editing software for simple code exercises with HTML, XML, CSS, Javascript, etc.: https://notepad-plus-plus.org/
- Mid-term: XAMPP (only needed later for database / web exercises): http://www.sussex.ac.uk/its/services/software/list?filter=exceedondemand&id=436

### Attendance

In line with common practice, we will use the Sussex Mobile App to record attendance in all our lectures and labs. You can download it from the Apple AppStore or Google PlayStore on to your phone. Read more about it here: https://student.sussex.ac.uk/mobile-app

If you prefer, the app can also be run in the browser at https://www.sussex.ac.uk/mobile

## Today's Topics

- Let's get started
- Basic concepts of computing
- Examples of computer hardware components and what they do
- The physical and logical perspective on computer systems

## Basic Concepts

### What is a Computer?

Some ways to talk about computer systems:
- Wires, transistors, capacitors, voltages and currents
- Integrated circuits, logic gates and bit patterns
- Machine code, file systems, transmission protocols and bytes
- Programs, computer languages and data formats
- Applications and user interfaces
- Physical devices: input and output of data
- Networks of computers and the Internet

Informally, a computer is an Information Processing System: It processes information by executing lists of instructions.

The processing, storage, and transmission of information are important aspects of what modern computers do.

More formally, a computer is based on a mathematical model that breaks down general-purpose computation into its basic, elementary steps: The Universal Turing machine (UTM)

Core concepts: A stored program, state register, memory.

For a device to be called a general-purpose computer it must be equivalent in capability to a UTM.

## Resources

### Physical Resources

Physical resources are devices that are part of or connected to a computer.

Examples of physical resources include:
- Input devices (keyboards, mice, scanners, cameras)
- Output devices (monitors, printers, speakers)
- Storage devices (hard drives, SSDs, USB drives, optical drives)
- Processing units (CPUs, GPUs)
- Memory modules (RAM)
- Network devices (network cards, routers, modems)
- Peripheral devices (external drives, game controllers, microphones)

Physical resources form the foundation of any computing system and must be managed effectively by the operating system and other software components to ensure proper system operation and resource allocation.

### How Resources Relate to Computer Functions

Examples:
- Memory: Storage of data short-term or long-term
- Central Processor: Processing of data, e.g. calculations, logic, or memory manipulation
- Networks & buses: Transmission of data / control

### Central Processing Unit (CPU)

The CPU is the "brain" of a computer.

Functions:
- **Numerical computation** - performing mathematical calculations
- **Logic operations** - executing logical decisions and comparisons
- **Control operations** - coordinating and managing other computer components
- **Input/output operations** - managing data transfer between the computer and external devices

### Primary Memory (RAM)

RAM (Random Access Memory) serves as the "short-term memory" of a computer and is also called "Primary memory."

Key Characteristics:

**Performance Features:**
- **Fast CPU connection**: Has a fast-track connection to the CPU
- **Quick data access**: Can access data very quickly
- **High read/write speed**: Provides very high speed for both reading and writing operations

**Limitations:**
- **Limited capacity**: Storage capacity is restricted compared to other storage types
- **Volatile memory**: Cannot hold any data without power - all data is lost when power is turned off

RAM acts as the working memory for active programs and data, providing rapid access for the CPU to perform computations and process information in real-time.

### Secondary Memory (Hard Disk Drive)

HDD represents a computer's "long-term memory," also referred to as "Secondary memory."

**Physical Properties:**
- Contains mechanical parts
- Significantly slower than RAM due to mechanical components

**Performance Metrics:**

Data Access Time:
- HDD: 1-8 milliseconds (ms)
- RAM (comparison): 10-50 nanoseconds (ns)

Read and Write Speeds:
- HDD: 20-100 MB/s
- RAM (comparison): 5-25 GB/s

**Key Advantages:**
1. **Large Storage Capacity**: Can store substantial amounts of data
2. **Persistent Memory**: Retains data even without power supply
3. **Cost-Effectiveness**: Remains competitive as solid-state disk (SSD) memory is still more expensive in comparison

HDDs are expected to remain in use for the foreseeable future due to the higher cost of SSD alternatives.

### Virtual Resources

Virtual resources are abstractions built on top of physical computing devices. They provide a logical view of system resources independent of the underlying hardware implementation.

Types of Virtual Resources:
- **Files**: Logical containers for data storage
- **Network connections**: Abstract communication channels between systems
- **Memory addresses**: Logical references to storage locations
- **CPU computing cycles**: Units of processing time allocation

Physical devices provide quantifiable measures of available virtual resources:
- **Hard disk storage capacity**: Determines the amount of file storage space available
- **CPU clock frequency**: Indicates the number of computing cycles available per unit time
- **Network bandwidth**: Measures the data transfer capacity of network connections

Virtual resources are derived from and constrained by the capabilities of physical hardware. The physical characteristics (capacity, frequency, bandwidth) define the upper limits of what virtual resources can provide to applications and users.

## CPU-RAM Interaction

How do the CPU and the RAM work together?

We need to store the data and the instructions of our program so that the CPU can access them as needed to run our program, and store any results of the computation, intermediate and final.

Components:
- RAM: Program Data, Program Instructions, Operating System and other programs
- CPU: Arithmetic Unit, Control Unit
- Inputs and Outputs

## Physical Aspects

### How Computers Work at the Fundamental Physical Level

Today's digital electronic computers contain a huge number of logic circuits that are made up from huge quantities of highly miniaturised transistors. These transistors are operated by electricity. The voltage of a control signal (high or low) will determine whether a transistor will let a current pass through or not.

**Binary Operation**:
- High voltage = transistor conducts current (ON state)
- Low voltage = transistor blocks current (OFF state)

This binary switching mechanism forms the foundation for digital computation, where information is represented and processed using two-state logic.

### Transistors

A transistor is a semiconductor, i.e. based on materials that give it dynamic electrical properties. Transistors are often used as electronic switches. Some advantages of transistors:
- Small in size
- Low weight
- Low power consumption
- Less heat emission than vacuum tubes
- Physically robust

### CMOS

Complementary-symmetrical Metal–Oxide–Semiconductor is a technology used for building digital logic circuits and fast memory. The word "complementary-symmetrical" refers to a design aspect specific of CMOS technology: The combined use of two different types of transistor.

## Logical Aspects

### How Computers Work at the Fundamental Logical Level

Multiple transistors of different type can be arranged in logic gates to implement well-known logic functions (e.g., NOT, AND, OR, XOR, etc.). These logic gates are then used to construct larger arrays of logic circuits that drive the elementary functions of a CPU, for example.

### CMOS Inverter Logic Gate (NOT Gate)

A CMOS inverter is a fundamental binary digital device that implements a NOT logic gate. It exists in one of two states, functioning as the basic building block of digital computers.

**CMOS Structure:**
- Built from a complementary and symmetrical pair of transistors:
  - p-type MOSFET (Metal Oxide Semiconductor Field Effect Transistor)
  - n-type MOSFET
- Each transistor has 3 connections
- Transistors function as switches

**Operating Principles:**

High Input State:
- Input ("In") receives high voltage
- Upper p-type transistor channel → high-resistance state
- Lower n-type transistor channel → low-resistance state
- **Output:** ground voltage (low)

Low Input State:
- Input ("In") receives ground voltage (low)
- Upper p-type transistor channel → low-resistance state
- Lower n-type transistor channel → high-resistance state
- **Output:** high voltage

**Logic Behavior:** The gate always inverts the signal received at the input. When input is high, output is low; when input is low, output is high.

**Truth Table:**

| Input (In) | Output |
|------------|--------|
| 0 (Low)    | 1 (High)|
| 1 (High)   | 0 (Low) |

The NOT gate performs logical negation - it produces the opposite of its input value, making it an essential component for implementing more complex digital logic circuits.

### NAND Logic Gate

A NAND gate is a "NOT AND" logic gate with two inputs (A and B) and one output.

**CMOS Implementation:**
The NAND gate is constructed using CMOS technology with:
- Two p-type transistors arranged in parallel
- Two n-type transistors arranged in series (corresponding to the p-type transistors)

**Universal Logic Gate:**
NAND is a universal logic gate, meaning:
- NAND circuits can be arranged and combined to reproduce any other logic function
- All digital circuits can be built using only NAND gates
- NOR is the other universal logic gate

The universal property of NAND gates makes them critically important for computing systems, as they provide the fundamental building block for constructing all digital logic operations.

**Truth Table:**

| Input A | Input B | Output |
|---------|---------|--------|
| 0       | 0       | 1      |
| 0       | 1       | 1      |
| 1       | 0       | 1      |
| 1       | 1       | 0      |

The output is 0 only when both inputs are 1; otherwise, the output is 1.

## Information Processing with Logic Circuits

Information processing in logic circuits operates through a hierarchical structure, where each level builds upon the previous one to enable computation.

### Architecture Layers

1. **Electrical Signals**
   - Electric signals with different voltage levels (low voltage and high voltage) serve as the foundation
   - These signals control transistor operation

2. **Transistors**
   - Transistors respond to electrical signals
   - They are arranged in specific configurations to create logic gates

3. **Logic Gates**
   - Built from transistor arrangements
   - Implement basic logical operations
   - Serve as building blocks for more complex circuits

4. **Logic Circuits**
   - Created by combining multiple logic gates
   - Represent higher-level functional devices
   - Perform operations by manipulating multiple electric signals simultaneously

### Operations Performed

Logic circuits enable two main categories of operations:
- **Arithmetic operations**: Mathematical calculations
- **Logic operations**: Boolean and logical computations

Logic circuits can be designed specifically to perform addition, demonstrating how the hierarchical structure translates into practical computational functionality.

## Information Storage with Logic Circuits

### Flip-Flops for Data Storage

A **flip-flop** is a fundamental circuit component that stores and retains binary state information (0 or 1).

**How Flip-Flops Work:**

State Changes:
- The state of a flip-flop can be changed by applying a pulse of HIGH voltage to one of its inputs
- Which input to use (upper or lower) depends on the current state of the device
- The specific input required varies based on whether the device is currently storing a 0 or 1

**Key Characteristic: State Retention**

The defining feature of a flip-flop is **memory persistence**:
- Once an input pulse is applied and the state changes, the flip-flop retains that new state
- The state remains stable even after the input pulse returns to LOW/0
- The state will only change again when another input pulse is applied

Multiple circuit designs can implement flip-flop functionality, demonstrating different approaches to achieving the same storage capability.

This state retention property makes flip-flops essential building blocks for information storage in digital systems. By maintaining their state without continuous power to the input, flip-flops enable:
- Memory circuits
- Data registers
- Sequential logic systems
- Binary information storage

## Summary

### Computing System Abstraction Levels

Computing systems can be understood and analyzed at multiple levels of abstraction, ranging from the physical components to logical representations. This layered approach allows different perspectives when working with computer systems.

**Key Perspectives:**
- **Physical Perspective**: The tangible, hardware components and their actual implementation
- **Logical Perspective**: The abstract, conceptual representation of how systems function

**Hierarchy of Abstraction Levels:**

1. **Transistors** - The basic electronic switches that form the foundation of digital circuits
2. **Logic Gates** - Combinations of transistors that perform basic logical operations (AND, OR, NOT, etc.)
3. **Logic Circuits** - Networks of logic gates that perform more complex operations
4. **Integrated Circuits** - Complete functional units combining multiple logic circuits on a single chip

Understanding these different abstraction levels allows professionals to:
- Work at the appropriate level of detail for their task
- Communicate effectively about system components
- Design and troubleshoot at various system layers
- Bridge the gap between physical hardware and logical functionality

### Key Points

- Most modern computers are based upon integrated electronic circuits that use transistors to perform different logic and arithmetic operations
- Modern computers are information processing systems that require resources to function
- Physical resources provide the basis for virtual resources that are needed for the processing, storage, or transmission of information

## Recommended Reading

Brookshear & Brylow
Computer Science: An Overview. Pearson Education, 12th edition, 2015.
Available online, there are also physical copies in the library
Chapter 0 (optional), Chapter 1

## Watch

Lecture on Computers and Heuristics by Richard Feynman (1985): https://www.youtube.com/watch?v=EKWGGDXe5MA

Key Topics and Timestamps:

**How Computers Work Internally:**
- Start time: Beginning of lecture (approximately 38 minutes of content)
- Key concept: "Dumber but faster" - describes the fundamental nature of computer operation
- Computers perform simple operations at high speed rather than complex intelligent operations

**Search Algorithms:**
- Time range: 43:30 - 51:30 minutes
- Covers search methodologies and approaches
- Discussion of heuristic methods in computational search

**Humans and Machines:**
- Section: Q&A session following main lecture
- Explores the relationship and differences between human cognition and machine computation
- Examines comparative advantages and limitations of each

## Next Lecture

- How software is run on computers
- How data and instructions are stored in memory
