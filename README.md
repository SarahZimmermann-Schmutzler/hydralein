# HYDRALEIN

A programm to crack SSH passwords via Brute-Force or Dictionary Attack.  
This is a lightweight version of the known <a href="https://github.com/vanhauser-thc/thc-hydra">**Hydra**</a> - tool.  

The program was created as part of my training at the Developer Academy and is used exclusively for teaching purposes.  

It was coded on **Windows 10** using **VSCode** as code editor.

## Table of Contents
1. <a href="#technologies">Technologies</a>  
2. <a href="#features">Features</a>  
3. <a href="#getting-started">Getting Started</a>  
4. <a href="#usage">Usage</a>  
5. <a href="#additional-notes">Additional Notes</a>  

## Technologies
* **Python** 3.12.2
    * **paramiko** 3.3.1 (module to install, <a href="https://www.paramiko.org/">More Information</a>)
    * **argparse, itertools, string** (modules from standard library) 

## Features
The following table shows which functions Hydralein supports:  

| Flag | Description | Required |
| ---- | ----------- | -------- |
| -h <br> --help | Get a list of the available options | no
| -u <br> --username | User of SSH connection | yes |
| -s <br> --server | Address of target server (IP or DNS) | yes |
| -w <br> --wordlist | Path to wordlist for dictionary attack | no |
| --min | Minimum password length for Brute-Force Attack; default: 4 | no |
| --max | Maximum password length for Brute-Force Attack; default: 6 | no |
| -c <br> --charset | Charset to use for Brute-Force Attack<br>default: a1 (lowercase letters and digits)<br>Available option:<br>A: Uppercase letters (A-Z)<br>a: Lowercase letters (a-z)<br>1: Digits (0-9)<br>!: Special characters<br>Example that uses all options: -c Aa1! | no |

- **Brute-Force-Attack**: The program systematically tries all possible combinations of characters to guess a password or access. It is a time-consuming “trial and error” method in which every possible password is tried until the right one is found.  
    - Is no wordlist given the programm runs automatically a Brute-Force Attack.  
    - In this case you can optionally define the minimum and maximum password length as well as the character set.  
- **Dictionary Attack**: A dictionary attack involves trying out a pre-prepared list of commonly used passwords. It's faster than a Brute-Force Attack, but won't work if the password isn't in the list.  
    - If a wordlist is given, the program runs a Dictionary Attack with it.

## Getting Started
0) <a href="https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo">Fork</a> the project to your namespace, if you want to make changes or open a <a href="https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests">Pull Request</a>.
1) <a href="https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository">Clone</a> the project to your platform if you just want to use the program.
2) Install the dependencies. In this case it's just **Paramiko**. You can install it across platforms with **Pip**:  
    `pip install paramiko`  

>i: If you want to test the the program safely, you can create a test environment with Docker, that establishes an SSH connection to localhost. Make sure the container runs before testing the program. *How to create this environment is not part of this Repository*.

## Usage
- Make sure you are in the folder where you cloned Hydralein into.  

- Help! What options does the program support!?  
    `python hydralein.py -h`  
    or  
    `python hydralein --help`  

- To run a **Brute-Force Attack** with no further specifications use the following command in your terminal:  
    `python hydralein.py -u [nameOfSshUser] -s [addressOfSshServer]`  
    - <ins>Example</ins>: Crack the SSH login passwort from user HomerJ at the server with the IP-address 123.4.5.6:  
    `python hydralein.py -u HomerJ -s 123.4.5.6`  
    >i: Carried out with the default charset (digits and lowercase letters), this attack would require 42.5 days of computing time.  
    Then use --min and --max! Good idea. It still doesn't change as much as you think...  

- To run a **Dictionary Attack** you need this command:  
    `python hydralein.py -u [nameOfSshUser] -s [addressOfSshServer] -w [pathToWordlist]`  
    - <ins>Example</ins>: to crack the SSH login passwort from user HomerJ at the server 123.4.5.6:  
    `python hydralein.py -u HomerJ -s 123.4.5.6 -w "path/to/wordlist"`  
    - What you see, if the attack was succesful:  
    ```
    Starting a Dictionary Attack on server [serverName] ...
    Password for user [userName] is: [password].
    Password cracked successfully!
    ```

## Additional Notes
**Paramiko** is a third-party library used to establish SSH connections in Python.  
  
The **argparse** module is used to parse (read) command line arguments in Python programs. It allows to define arguments and options that can be passed to the program when starting it from the command line. These are then processed and are available in the program as variables.  
  
**Itertools** provides a collection of iterators for efficient loops in Python. It provides functions that enable common combinatorial operations such as infinitely iterating over elements.
  
The **string** module offers functions and constants that make working with character strings easier. It includes pre-built strings for letters, numbers, whitespace and other useful things, as well as string manipulation functions.  
  
**ChatGPT** was involved in the creation of the program (Debugging, Prompt Engineering etc.).  
  
I use **Google Translate** for translations from German into English.