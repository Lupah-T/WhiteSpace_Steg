# Zero-Width Unicode Steganography Decoder

## Overview

This project is a Python forensic utility designed to detect and decode hidden messages embedded using invisible Unicode characters.

The tool analyzes text files and searches for hidden Unicode characters commonly used in steganography:

- U+200B → Zero Width Space (ZWSP)
- U+200C → Zero Width Non-Joiner (ZWNJ)

These characters are invisible when viewing text normally, making them useful for hiding information inside documents without changing visible content.

---

## What is Zero-Width Steganography?

Zero-width steganography is a technique where invisible Unicode characters are inserted between visible characters in a text file.

Example:

Visible text:

Hello World

Actual stored text:

H[ZWSP]e[ZWNJ]l[ZWSP]l[ZWSP]o

The hidden characters cannot normally be seen by the user but still exist inside the file.

These characters can represent binary values:

| Unicode Character | Description | Binary Value |
|-------------------|-------------|--------------|
| U+200B | Zero Width Space | 0 |
| U+200C | Zero Width Non-Joiner | 1 |

Binary values can then be grouped into bytes and converted into hidden text.

---

## How the Tool Works

The tool performs the following steps:

### Step 1 — Read file contents

The script opens the supplied text file:

```python
with open(file,"r",encoding="utf-8")
```

Purpose:

- Read the complete file
- Preserve Unicode characters
- Load data into memory

---

### Step 2 — Search for invisible Unicode characters

The tool checks every character:

```python
if ord(character) in [0x200B,0x200C]
```

Purpose:

- Detect Zero Width Space
- Detect Zero Width Non-Joiner

---

### Step 3 — Extract hidden symbols

Detected invisible characters are stored for analysis.

Example:

Hidden sequence:

U+200B U+200C U+200B U+200B

---

### Step 4 — Convert symbols into binary

Example mapping:

U+200B → 0

U+200C → 1

Result:

0100

---

### Step 5 — Group bits into bytes

Binary data is grouped into:

01001000
01101001

---

### Step 6 — Convert bytes to text

The script converts binary values into ASCII characters.

Example:

01001000

↓

72

↓

H

---

## Requirements

### Operating System

Compatible with:

- Linux
- Windows
- macOS

---

### Python Version

Python 3.8+

Check installed version:

```bash
python3 --version
```

Example output:

```bash
Python 3.12.3
```

---

## Installation

Clone project:

```bash
git clone https://github.com/yourusername/zero-width-steg-tool.git
```

Move into directory:

```bash
cd zero-width-steg-tool
```

Make executable:

```bash
chmod +x zwdecode.py
```

---

## Usage

Run the tool against a target file:

```bash
python3 zwdecode.py example_file.txt
```

or

```bash
./zwdecode.py example_file.txt
```

---

## Example

Input:

example_file.txt

Visible content:

The quick brown fox jumps over the lazy dog.

Hidden content:

Invisible Unicode symbols embedded between characters.

Command:

```bash
python3 zwdecode.py example_file.txt
```

Output:

```bash
[+] Hidden Unicode characters found: 128

--- Mapping 1 ---
ZWSP=0 ZWNJ=1

flag{hidden_message}

--- Mapping 2 ---
ZWSP=1 ZWNJ=0

unreadable output
```

---

## Forensic Applications

This technique is useful for:

- Digital forensics
- Incident response
- Malware investigations
- CTF challenges
- Text artifact analysis
- Hidden data detection

---

## Indicators of Hidden Unicode Data

Potential indicators include:

- File size larger than expected
- Strange spacing behavior
- Text rendering inconsistencies
- Unexpected UTF-8 byte sequences
- Presence of:

U+200B

U+200C

U+200D

U+FEFF

---

## Disclaimer

This tool is intended for educational purposes, forensic analysis, and authorized investigations only.
