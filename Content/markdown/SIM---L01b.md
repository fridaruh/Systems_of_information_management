# SIM   L01b

**Conversion date:** 2026-01-11
**Original file:** `SIM - L01b.pptx`
**Total slides:** 32

---


## Table of Contents

1. [Systems for Information ManagementLecture 1b](#slide-1-systems-for-information-managementlecture-1b)
2. [Previously](#slide-2-previously)
3. [Today](#slide-3-today)
4. [Software](#slide-4-software)
5. [Software](#slide-5-software)
6. [Software](#slide-6-software)
7. [Programming Languages](#slide-7-programming-languages)
8. [Machine Code](#slide-8-machine-code)
9. [Hierarchy of Control](#slide-9-hierarchy-of-control)
10. [Code Translation](#slide-10-code-translation)
11. [Summary: Software and Computers](#slide-11-summary-software-and-computers)
12. [Data Representation in Memory](#slide-12-data-representation-in-memory)
13. [Data Representation in Memory](#slide-13-data-representation-in-memory)
14. [Data Representation in Memory](#slide-14-data-representation-in-memory)
15. [CPU Information Processing](#slide-15-cpu-information-processing)
16. [Binary numbers / bits](#slide-16-binary-numbers--bits)
17. [Bit patterns](#slide-17-bit-patterns)
18. [Bit patterns](#slide-18-bit-patterns)
19. [Number bases](#slide-19-number-bases)
20. [Number bases](#slide-20-number-bases)
21. [Number bases](#slide-21-number-bases)
22. [Number bases](#slide-22-number-bases)
23. [Bitwise operations](#slide-23-bitwise-operations)
24. [Bitwise operations](#slide-24-bitwise-operations)
25. [Bitwise operations](#slide-25-bitwise-operations)
26. [Bitwise operations](#slide-26-bitwise-operations)
27. [Bitwise operations](#slide-27-bitwise-operations)
28. [Bitwise Information Storage](#slide-28-bitwise-information-storage)
29. [Bitwise Information Storage](#slide-29-bitwise-information-storage)
30. [Bitwise Information Storage](#slide-30-bitwise-information-storage)
31. [Read](#slide-31-read)
32. [Next Lecture](#slide-32-next-lecture)

## 1. Systems for Information ManagementLecture 1b {#slide-1-systems-for-information-managementlecture-1b}

### Content

Dr Imran U Khan		School of Engineering and Informatics		    Autumn term 2021

---

## 2. Previously {#slide-2-previously}

### Content

- Computing basics
- Basic concepts of computing
- Examples of computer hardware components and what they do
- The physical and logical perspective on computer systems

---

## 3. Today {#slide-3-today}

### Content

- Computing basics: Software
- How software is run on computing systems
- The hierarchy of control
- How data and instructions are represented in memory
- How a CPU carries out instructions

---

## 4. Software {#slide-4-software}

### Content

What kind of software runs on computers?

---

## 5. Software {#slide-5-software}

### Content

Software

What kind of software runs on computers?

Examples:
Operating System
Drivers
Services
Applications

### Visual Analysis

# Software Categories

## Types of Software on Computers

Software that runs on computers can be classified into four main categories:

### Operating System
The fundamental software that manages computer hardware and provides services for other software programs.

### Drivers
Software components that enable the operating system to communicate with and control hardware devices.

### Services
Background processes that provide specific functionality to the operating system and applications, typically running without direct user interaction.

### Applications
End-user programs designed to perform specific tasks or solve particular problems for users.

---

## 6. Software {#slide-6-software}

### Content

Software

What kind of software runs on computers?

Examples:
Operating System
Drivers
Services
Applications

### Visual Analysis

# Software Types

## Main Question
What kind of software runs on computers?

## Categories of Software

### Operating System
Software that manages computer hardware and software resources and provides common services for computer programs.

### Drivers
Software components that enable the operating system to communicate with hardware devices.

### Services
Background programs that run continuously to support system or application functionality.

### Applications
Programs designed to perform specific tasks for users, such as word processors, web browsers, or games.

---

## 7. Programming Languages {#slide-7-programming-languages}

### Content

How do computers run software?
Software applications are usually programmed using a programming language that humans can learn and use.
There are many different programming languages that use different degrees of abstraction, to make it easier to use the computer’s basic functions and hardware.
Which programming languages do you know?

---

## 8. Machine Code {#slide-8-machine-code}

### Content

How do computers run software?
The key to running any software on an electronic computer is the translation of whatever has been programmed using a programming language into the low-level signals that control the transistors in the CPU and other components, in order to perform the instructions in the program as a sequence of more basic commands, such as arithmetic and logic operations.
The lowest logical representation of this translation output can be represented in the form of 0s and 1s (and interpreted as low and high voltages). This is called Machine codeMachine code is the only language a computer can actually “understand”.

---

## 9. Hierarchy of Control {#slide-9-hierarchy-of-control}

### Content

Hierarchy of Control

High-level language, e.g. C or C++

Assembly language

Machine code

Computingplatform 
independence

Human
readability
of the code

How do computers run software?

9

### Visual Analysis

# Hierarchy of Control in Software Execution

## Programming Language Levels

Software can be written at different levels of abstraction, forming a hierarchy:

### 1. High-level Language
- Examples: C, C++
- Characteristics:
  - Maximum computing platform independence
  - Highest human readability
  - Abstract syntax that resembles natural language and mathematical notation

### 2. Assembly Language
- Middle layer in the hierarchy
- Moderate platform independence
- Moderate human readability
- Uses mnemonic codes to represent machine operations

### 3. Machine Code
- Lowest level of the hierarchy
- Minimal to no platform independence (hardware-specific)
- Lowest human readability
- Binary instructions directly executed by the processor

## Key Relationships

**Platform Independence vs. Abstraction Level:**
- Higher-level languages provide greater platform independence
- Lower-level languages are more tied to specific hardware architectures

**Human Readability vs. Abstraction Level:**
- Higher-level languages are easier for humans to read and write
- Lower-level languages are more difficult to understand but closer to hardware execution

## Software Execution Process

Programs written in high-level languages must be translated down through these layers before the computer can execute them, ultimately converting to machine code that the processor can understand.

---

## 10. Code Translation {#slide-10-code-translation}

### Content

How can we translate programs into machine code?
Compile high-level code = Translation before executionLanguages: C, C++, Objective-C
Interpret high-level code = Translation during executionLanguages: JavaScript, PHP, MATLAB
Compile and interpret = Translation into an intermediate format (e.g., Java bytecode) which is then executed within another software environment (e.g., a virtual machine)Languages: Java, C#, Python

- 10

---

## 11. Summary: Software and Computers {#slide-11-summary-software-and-computers}

### Content

Modern electronic computers execute binary machine code.
Any higher-level language code needs to be translated into assembly/machine language to run (e.g., be compiled, or interpreted).
The lower the level we program at, the more platform-dependent our code is.
Machine code is specific to a particular hardware platform (e.g., Intel x86, ARM, AMD64, etc.)

---

## 12. Data Representation in Memory {#slide-12-data-representation-in-memory}

### Content

Data Representation in Memory

How does the basic representation of data and instructions work?

Computers do not understand the human-readable code of “high-level” programming languages such as Java, Python, C, or PHP.
Such code needs to be translated into data and instructions a computer can actually work with, e.g.:

12

### Visual Analysis

# Data Representation in Memory

## Core Concept

Computers cannot directly understand human-readable code written in high-level programming languages. A translation process is necessary to convert source code into a format the computer can execute.

## High-Level Programming Languages

Examples of high-level programming languages include:
- Java
- Python
- C
- PHP

These languages use human-readable syntax and abstractions that must be converted to machine-executable format.

## Translation Process

Code written in high-level languages needs to be translated into:
- Data representations that computers can store and manipulate
- Instructions that processors can execute directly

This translation bridges the gap between human-readable code and machine-executable binary instructions that the computer's hardware can process.

---

## 13. Data Representation in Memory {#slide-13-data-representation-in-memory}

### Content

Data Representation in Memory

How does the basic representation of data and instructions work?

Computers do not understand the human-readable code of “high-level” programming languages such as Java, Python, C, or PHP.
Such code needs to be translated into data and instructions a computer can actually work with, e.g.:

13

### Visual Analysis

# Data Representation in Memory

## Core Concept

Computers cannot directly understand human-readable code written in high-level programming languages. A translation process is necessary to convert this code into a format the computer can execute.

## High-Level Programming Languages

High-level programming languages are designed for human understanding and include:
- Java
- Python
- C
- PHP

## Translation Requirement

Code written in high-level languages must be translated into:
- Data representations that computers can process
- Instructions that computers can execute

This translation bridges the gap between human-readable programming syntax and machine-executable binary code.

---

## 14. Data Representation in Memory {#slide-14-data-representation-in-memory}

### Content

Data Representation in Memory

How does the basic representation of data and instructions work?

Computers do not understand the human-readable code of “high-level” programming languages such as Java, Python, C, or PHP.
Such code needs to be translated into data and instructions a computer can actually work with, e.g.:

14

### Visual Analysis

# Data Representation in Memory

## Core Concept

Computers cannot directly process human-readable programming code. All high-level programming languages must be translated into a format that computers can execute.

## High-Level Programming Languages

Programming languages designed for human readability and comprehension include:
- Java
- Python
- C
- PHP

## Translation Requirement

Code written in high-level languages must undergo translation into:
- Machine-readable data formats
- Executable instructions that the computer's processor can interpret and execute

This translation process bridges the gap between human-understandable code and the binary representations that computer hardware operates on.

---

## 15. CPU Information Processing {#slide-15-cpu-information-processing}

### Content

CPU Information Processing

How does the CPU run a program, in principle?

15

### Visual Analysis

# CPU Information Processing

## Core Question

**How does the CPU run a program, in principle?**

This fundamental question addresses the basic operating mechanism of the Central Processing Unit (CPU) when executing program instructions. Understanding this process is essential for comprehending how computers execute software and perform computational tasks.

## Key Concepts

The CPU program execution involves understanding:

- The fetch-decode-execute cycle
- How instructions are retrieved from memory
- How the CPU interprets these instructions
- How operations are performed on data
- The sequential or parallel nature of instruction processing

---

## 16. Binary numbers / bits {#slide-16-binary-numbers--bits}

### Content

- Modern computers are binary machines
We program in higher-level languages, using alpha-numerical symbols.
If there is any maths involved, we tend to express real-world tasks and problems in the number system we’re most familiar with: decimal.
Ultimately, all programs and all data are represented as binary bit patterns
Data and programs are stored in memory in a binary format
- CPU information processing is performed by binary operations
Memory addresses and large binary numbers are often expressed as hexadecimal numbers

---

## 17. Bit patterns {#slide-17-bit-patterns}

### Content

Bit patterns

What is a bit?Consider beads on a frame. Each bead is in one of two states: up or down.This frame has 8 beads in a fixed pattern. It can store 8 bits of information. 
	How many different states can it be in?

### Visual Analysis

# Bit Patterns

## Definition of a Bit

A bit can be understood through a physical analogy: beads on a frame where each bead exists in one of two states - up or down. This binary nature is fundamental to how bits function.

## Information Storage Capacity

- A frame with 8 beads can store 8 bits of information
- Each bead position represents one bit
- The beads are arranged in a fixed pattern

## Calculating Possible States

**Key Question:** How many different states can 8 bits represent?

Since each bit has 2 possible states (up/down, or 0/1), and there are 8 bits:
- Total possible states = 2^8 = 256 different states

This demonstrates the exponential relationship between the number of bits and the total number of unique patterns or values that can be represented.

## Core Principle

The two-state nature of bits (binary system) is the foundation of digital information storage and processing. Any information stored digitally is ultimately represented as patterns of these binary states.

---

## 18. Bit patterns {#slide-18-bit-patterns}

### Content

Bit patterns

Binary numbers

All bits in a binary number represent increasing powers of 2, starting with 20 from right to left
We can convert bit patterns to decimal numbers, e.g. the 8-bit number 11111111 could be interpreted like this:
If a bit is switched “on” (1), then the value that this bit representscounts towards the totalrepresented by the entire pattern.
2bits = states, e.g.:28 = 2*2*2*2*2*2*2*2 = 256 possible states

### Visual Analysis

# Binary Numbers and Bit Patterns

## Binary Number Structure

Binary numbers use bits that represent increasing powers of 2, starting with 2⁰ from right to left.

## Converting Binary to Decimal

An 8-bit binary number can be converted to decimal by evaluating each bit position:

**Example: 11111111**

- Each bit position represents a power of 2
- When a bit is "on" (1), its corresponding value counts toward the total
- When a bit is "off" (0), that position contributes nothing to the total

## Calculating Possible States

The number of possible states in a binary system is calculated using:

**Formula:** 2^n states (where n = number of bits)

**Example:**
- 2⁸ = 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 = 256 possible states
- An 8-bit number can represent 256 different values (0-255)

## Key Concept

If a bit is switched "on" (1), the value that bit represents counts toward the total represented by the entire bit pattern. This additive property allows binary numbers to encode numerical values through combinations of powers of 2.

---

## 19. Number bases {#slide-19-number-bases}

### Content

Number bases

Decimal numbers

In decimal, we organise our numbers into powers of ten, i.e. units of ones, tens, hundreds, and so on, starting with 100 from right (the least significant digit) to left (towards the most significant digit)
For example, the number 5617:





						5 * 1000 + 6 * 100 + 1 * 10 + 7 * 1

### Visual Analysis

# Number Bases

## Decimal Number System

Decimal numbers organize values into powers of ten. Each position represents a power of 10, starting from 10⁰ at the rightmost position (least significant digit) and increasing towards the left (most significant digit).

### Positional Values in Decimal

The positions represent:
- Units of ones (10⁰)
- Tens (10¹)
- Hundreds (10²)
- Thousands (10³)
- And so on...

### Example: Decomposing 5617

The number 5617 can be broken down by its positional values:

```
5 * 1000 + 6 * 100 + 1 * 10 + 7 * 1
```

This demonstrates how each digit's value is determined by:
- The digit itself
- Its position in the number
- The base (10) raised to the power corresponding to that position

---

## 20. Number bases {#slide-20-number-bases}

### Content

Number bases

Binary numbers

In binary, the number 5617 translates to 1 0 1 0 1 1 1 1 1 0 0 0 1
All bits in a binary number represent increasing decimal powers of 2, starting with 20 from right (the least significant bit) to left (towards the most significant bit)




				
1 * 4096 + 0 * 2048 + 1 * 1024 + 0 * 512 + 1 * 256 + 1 * 128 + 1 * 64 + 1 * 32 + 1 * 16 + 0 * 8 + 0 * 4 + 0 * 2 + 1 * 1, or in short:
4096 + 1024 + 256 + 128 + 64 + 32 + 16 + 1

### Visual Analysis

# Binary Number System

## Core Concept

Binary numbers use base-2 representation, where each digit (bit) can only be 0 or 1.

## Positional Value System

Each bit position in a binary number represents a power of 2:
- The rightmost bit (least significant bit) represents 2⁰
- Each position moving left represents the next higher power of 2
- The leftmost bit (most significant bit) represents the highest power of 2 in that number

## Binary to Decimal Conversion

### Example: Converting binary 1010111110001 to decimal

**Binary representation:** 1 0 1 0 1 1 1 1 1 0 0 0 1

**Position values (right to left):**
- Position 0: 2⁰ = 1
- Position 1: 2¹ = 2
- Position 2: 2² = 4
- Position 3: 2³ = 8
- Position 4: 2⁴ = 16
- Position 5: 2⁵ = 32
- Position 6: 2⁶ = 64
- Position 7: 2⁷ = 128
- Position 8: 2⁸ = 256
- Position 9: 2⁹ = 512
- Position 10: 2¹⁰ = 1024
- Position 11: 2¹¹ = 2048
- Position 12: 2¹² = 4096

**Calculation:**
```
1 × 4096 + 0 × 2048 + 1 × 1024 + 0 × 512 + 1 × 256 + 1 × 128 + 1 × 64 + 1 × 32 + 1 × 16 + 0 × 8 + 0 × 4 + 0 × 2 + 1 × 1
```

**Simplified (only non-zero terms):**
```
4096 + 1024 + 256 + 128 + 64 + 32 + 16 + 1 = 5617
```

## Conversion Method

To convert from binary to decimal:
1. Identify each bit position from right to left
2. Multiply each bit by its corresponding power of 2
3. Sum all the results to get the decimal value

---

## 21. Number bases {#slide-21-number-bases}

### Content

Number bases

Hexadecimal numbers

Each hex-digit represents a 4-bit binary number (00002 to 11112) or the decimal numbers 0  to 15 (The decimal values 10 - 15 are mapped to the letters A - F)
In hexadecimal, the number 561710 (or 10101111100012) translates to:





						1 * 4096 + 5 * 256 + F(=1510) * 16 + 1 * 1

### Visual Analysis

# Hexadecimal Numbers

## Relationship to Binary and Decimal

Each hexadecimal digit represents a 4-bit binary number, ranging from:
- Binary: `0000₂` to `1111₂`
- Decimal: 0 to 15

## Hexadecimal Digit Mapping

The decimal values 10 through 15 are mapped to letters:
- 10 = A
- 11 = B
- 12 = C
- 13 = D
- 14 = E
- 15 = F

## Conversion Example

Converting the decimal number **5617₁₀**:

**Binary representation:** `1010111110001₂`

**Hexadecimal representation:** `15F1₁₆`

### Calculation breakdown:

```
15F1₁₆ = (1 × 4096) + (5 × 256) + (F × 16) + (1 × 1)
       = (1 × 16³) + (5 × 16²) + (15 × 16¹) + (1 × 16⁰)
       = 4096 + 1280 + 240 + 1
       = 5617₁₀
```

This demonstrates positional notation in hexadecimal, where each position represents a power of 16, moving from right to left (16⁰, 16¹, 16², 16³, etc.).

---

## 22. Number bases {#slide-22-number-bases}

### Content

- Binary numbers
What is the binary equivalent of the decimal number 44?
What is the hexadecimal equivalent of the same number?

---

## 23. Bitwise operations {#slide-23-bitwise-operations}

### Content

Bitwise operations

Bitwise operations

Knowing that data is stored in binary,we can manipulate bit patterns directlyto perform certain types of computation

### Visual Analysis

# Bitwise Operations

## Core Concept

Bitwise operations are techniques for manipulating individual bits in binary data representations. Since all data in computers is ultimately stored in binary format (sequences of 0s and 1s), bitwise operations allow direct manipulation of these underlying bit patterns to perform computations.

## Key Principle

By working directly with binary representations, programmers can:
- Perform efficient low-level operations
- Execute certain types of computations more quickly than higher-level operations
- Implement specific algorithms that require bit-level control
- Optimize memory usage and processing speed

## Applications

Bitwise operations enable:
- Direct manipulation of binary data structures
- Efficient implementations of certain computational tasks
- Low-level system programming
- Performance optimization in critical code sections

---

## 24. Bitwise operations {#slide-24-bitwise-operations}

### Content

Bitwise operations

Multiplication

Knowing that data is stored in binary,we can manipulate bit patterns directlyto perform certain types of computation
E.g.,Shifting bits to the left: 		multiply with 2

### Visual Analysis

# Bitwise Operations for Multiplication

## Core Concept

Data is stored in binary format, which allows for direct manipulation of bit patterns to perform computational operations efficiently.

## Bit Shifting as Multiplication

### Left Shift Operation
Shifting bits to the left multiplies a number by 2.

**How it works:**
- Each left shift moves all bits one position to the left
- A new 0 is added on the right side
- The result is equivalent to multiplying the original number by 2

**Example:**
```
Original:  0101  (decimal 5)
Left shift: 1010  (decimal 10)
Result: 5 × 2 = 10
```

## Advantages of Bitwise Multiplication
- Direct hardware-level operation
- Faster than standard arithmetic multiplication
- Efficient for powers of 2 (multiple left shifts for 4, 8, 16, etc.)
- Used in performance-critical code and low-level programming

---

## 25. Bitwise operations {#slide-25-bitwise-operations}

### Content

Bitwise operations

Division

Knowing that data is stored in binary,we can manipulate bit patterns directlyto perform certain types of computation
E.g.,Shifting bits to the left: 		multiply with 2Shifting bits to the right: 	divide by 2

### Visual Analysis

# Bitwise Operations: Division

## Core Concept

Binary data can be manipulated directly at the bit level to perform computational operations efficiently.

## Bit Shifting for Division and Multiplication

### Left Shift Operation
- **Operation:** Shifting bits to the left
- **Result:** Multiplies the value by 2
- Each left shift is equivalent to multiplying by 2^1

### Right Shift Operation
- **Operation:** Shifting bits to the right
- **Result:** Divides the value by 2
- Each right shift is equivalent to dividing by 2^1 (integer division)

## Practical Application

By leveraging binary representation of data, bit shifting provides a fast method for multiplication and division by powers of 2, which is more efficient than traditional arithmetic operations at the hardware level.

---

## 26. Bitwise operations {#slide-26-bitwise-operations}

### Content

Bitwise operations

Logic operations

Knowing that data is stored in binary,we can manipulate bit patterns directlyto perform certain types of computation
E.g.,Shifting bits to the left: 		multiply with 2Shifting bits to the right: 	divide by 2Logic operations: XOR, AND, OR…(may require two numbers as input)

### Visual Analysis

# Bitwise Operations and Logic Operations

## Core Concept

Data stored in binary format can be manipulated directly at the bit pattern level to perform computational operations efficiently.

## Bit Shifting Operations

### Left Shift
- **Operation**: Shifting bits to the left
- **Mathematical effect**: Multiplies the value by 2
- Each left shift position doubles the number

### Right Shift
- **Operation**: Shifting bits to the right
- **Mathematical effect**: Divides the value by 2
- Each right shift position halves the number

## Logic Operations

Logic operations manipulate bit patterns using Boolean logic principles.

### Common Logic Operations
- **XOR** (Exclusive OR)
- **AND**
- **OR**

### Input Requirements
Logic operations may require two numbers as input to perform bit-by-bit comparisons and transformations.

## Practical Application

These bitwise operations provide:
- Efficient arithmetic computation (multiplication/division by powers of 2)
- Direct hardware-level data manipulation
- Performance optimization for specific calculations

---

## 27. Bitwise operations {#slide-27-bitwise-operations}

### Content

Bitwise operations

Logic operations

Logic operations are carried out bit by bitfrom right to left
AND will yield 1 only if both inputs are 1.
OR will yield 1 only if either ofthe inputs are 1, or both are 1
XOR will yield 1 only if either of the inputs are 1, but not both
NOT will simply negate the current truth value of each bit

### Visual Analysis

# Bitwise Logic Operations

## Overview
Logic operations are performed bit by bit, processing from right to left.

## Core Logic Operations

### AND Operation
- Yields 1 only if both inputs are 1
- All other combinations yield 0

### OR Operation
- Yields 1 if either input is 1, or both are 1
- Only yields 0 when both inputs are 0

### XOR Operation (Exclusive OR)
- Yields 1 only if either input is 1, but not both
- Yields 0 when both inputs are the same (both 0 or both 1)

### NOT Operation
- Negates the current truth value of each bit
- Converts 1 to 0 and 0 to 1

## Operational Characteristics
- Operations process individual bits sequentially
- Direction of processing: right to left
- Each bit position is evaluated independently

---

## 28. Bitwise Information Storage {#slide-28-bitwise-information-storage}

### Content

Bitwise Information Storage

Of chips and packages

A chip is connected to the rest of the computing platform by a limited number of electrical connections, e.g. 84 in a typical package like the one displayed below. 
There may sometimes be more than one chip mounted on to the circuit board
If we had two chips, and each stored 512 Megabit of information, how many megabytes of memory does our system have in total?

### Visual Analysis

# Bitwise Information Storage

## Chip Physical Connections

Computer chips connect to the computing platform through a limited number of electrical connections. A typical chip package uses 84 electrical connections.

## Multiple Chip Configurations

Circuit boards can accommodate more than one chip mounted simultaneously, allowing for expanded memory capacity.

## Memory Calculation Problem

**Scenario:** A system contains two chips, each storing 512 Megabit of information.

**Question:** What is the total memory capacity in megabytes?

### Solution Approach

Key conversion factors needed:
- 1 byte = 8 bits
- Total bits = 2 chips × 512 Megabit = 1024 Megabit
- Total bytes = 1024 Megabit ÷ 8 = 128 Megabytes

**Answer:** The system has 128 MB of total memory.

## Key Concept: Bit to Byte Conversion

When calculating memory capacity, it's essential to distinguish between:
- **Megabit (Mb):** Measurement commonly used for chip storage capacity
- **Megabyte (MB):** Standard measurement for system memory capacity
- **Conversion ratio:** 8 bits = 1 byte

---

## 29. Bitwise Information Storage {#slide-29-bitwise-information-storage}

### Content

- The confusion around bits and bytes
In modern computing, 8 bit are grouped to represent 1 byte of information but there are some legacy issues concerning the terminology commonly used to express large amounts of bits and bytes.
As digital memory is based on the binary system, storage capacity is expressed in numbers that are powers of two. For example: 28 bit = 2*2*2*2*2*2*2*2 = 256 bit.
It is for this reason, that when (IT- or Computer science-) people talk about memory capacity, that the term kilobit has come to mean 210 bit. The same holds for megabit (220), gigabit (230), and so on. We use exactly the same system for storage capacity expressed in bytes as well.
BUT: According to the international system of units (SI), using kilobit (Kb) to mean 1024 bits is inaccurate (it should be 1000 = 103). The correct terminology for 1024 would be Kibibit (Kibit), but this is not widely used, in spite of being correct! (Analog for all the other units)

---

## 30. Bitwise Information Storage {#slide-30-bitwise-information-storage}

### Content

Bitwise Information Storage

The confusion around bits and bytes

One chip stores 512 Megabit (Mb) = 512 * 1024 Kilobit (Kb) = 524.288 Kb = 524.288 * 1024 bit (b) = 536.870.912 b
Each group of 8 bit equals 1 byte, so both memory chips together hold 134.217.728 bytes = 128 MeBiByte (or “Megabyte”) = 128 * 1024 * 1024 Bytes combined.

### Visual Analysis

# Bitwise Information Storage

## Memory Capacity Units and Conversions

### Single Chip Storage Calculation

One memory chip stores **512 Megabit (Mb)**

Breaking down the conversion:
- 512 Mb = 512 × 1,024 Kilobit (Kb)
- = 524,288 Kb
- = 524,288 × 1,024 bits
- = 536,870,912 bits

### Bit to Byte Conversion

**Fundamental relationship:** 8 bits = 1 byte

When combining two memory chips:
- Total bits: 536,870,912 bits × 2 = 1,073,741,824 bits
- Total bytes: 1,073,741,824 bits ÷ 8 = 134,217,728 bytes
- In MeBiByte (MiB): 134,217,728 bytes = 128 MiB
- Calculation: 128 × 1,024 × 1,024 = 134,217,728 bytes

## Binary vs Decimal Measurements

### Important Distinction

The slide highlights "confusion around bits and bytes" regarding measurement standards:

- **Megabit/Megabyte (MB)** can refer to decimal (base-10) measurements
- **MeBiByte (MiB)** specifically refers to binary (base-2) measurements
- 1 MiB = 1,024 × 1,024 bytes (binary)
- This differs from decimal megabyte definitions used in some contexts

### Key Conversion Factor

The consistent use of **1,024** as the multiplier reflects the binary nature of computer memory:
- 1,024 = 2^10
- Used for Kilobit → bit conversions
- Used for MiB calculations

---

## 31. Read {#slide-31-read}

### Content

- Brookshear and Brylow
- Sections 1.1, 1.4, 2.1, 2.2

---

## 32. Next Lecture {#slide-32-next-lecture}

### Content

- Computer networks and the Internet

---


---

## Processing Metadata

### Slide Classification
- Text slides: 13
- Visual slides: 19
- Optimized percentage (without API): 40.6%

### API Costs
- Input tokens: 89,504
- Output tokens: 19,787
- Total cost: $0.5653 USD

### System
- Generated by: PPTX to Markdown Converter
- Date: 2026-01-11 19:13:33