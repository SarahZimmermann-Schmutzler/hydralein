# HYDRALEIN

A programm to **crack SSH passwords via Brute-Force or Dictionary Attack**.  
This is a lightweight version of the known [hydra](https://github.com/vanhauser-thc/thc-hydra) - tool.  

The program was created as part of my training at the Developer Academy and is used exclusively for teaching purposes.  

## Table of Contents

1. [Technologies](#technologies)
1. [Getting Started](#getting-started)
1. [Usage](#usage)
   * [Program Options](#program-options)
   * [Program Flow](#program-flow)
   * [Example Run](#example-run)

## Technologies

* **Python** 3.12.2
  * **argparse, itertools, string**
  * **paramiko** 3.3.1 [More Information](https://www.paramiko.org/)
    * It is a third-party library used to establish SSH connections in Python.

## Getting Started

0) [Fork](https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) the project to your namespace, if you want to make changes or open a [Pull Request](https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

1. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the project to your platform if you just want to use it:

    ```bash
    git clone git@github.com:SarahZimmermann-Schmutzler/XSStrike.git
    ```

1. Install the **dependencies**:
   * Create a **Virtual Environment (Venv)** in the project folder:

      ```bash
      python -m venv env
      ```

   * **Activate** the Venv:

      ```bash
      source venv/bin/activate #Linux
      env\Scripts\activate #Windows
      ```

   * Install the **dependencies** from [requirements.txt](./requirements.txt):

      ```bash
      pip install -r requirements.txt
      ```

> [!NOTE]
> If you want to test the the program safely, you can create a test environment with Docker, that establishes an SSH connection to localhost. Make sure the container runs before testing the program. The user could named `vik` and the password could be `test123abc`.

## Usage

* For the further commands navigate to the directory you cloned **hydralein** into.

### Program Options

* To see all available **program options** have a look in the `help-section`:

    ```bash
    python hydralein.py -h
    # or
    python hydralein.py --help
    ```

  | Option (Long) | Short | Choices | Description | Required? |
  | ------------- | ----- | ------- | ----------- | --------- |
  | --help | -h |  | Get a list of the **available options** | no |
  | --username | -u |  | **User** of SSH connection | yes |
  | --server | -s |  | **Address** of target server (IP or DNS) | yes |
  | --wordlist | -w |  | Path to **wordlist for dictionary attack** | no |
  | --min |  |  | **Minimum password length** for Brute-Force Attack <br> default: 4 | no |
  | --max |  |  | **Maximum password length** for Brute-Force Attack <br> default: 6 | no |
  | --charset | -c | A: Uppercase letters (A-Z)<br>a: Lowercase letters (a-z)<br>1: Digits (0-9)<br>!: Special characters | **Charset** to use for Brute-Force Attack<br>default: a1 (lowercase letters and digits)<br>Example that uses all options: -c Aa1! | no |
  
### Program Flow

* **Brute-Force-Attack**: The program systematically tries all possible combinations of characters to guess a password or access. It is a time-consuming “trial and error” method in which every possible password is tried until the right one is found.  
  * Is no wordlist given the programm runs automatically a Brute-Force Attack.  
  * In this case you can optionally define the minimum and maximum password length as well as the character set.

* **Dictionary Attack**: A dictionary attack involves trying out a pre-prepared list of commonly used passwords. It's faster than a Brute-Force Attack, but won't work if the password isn't in the list.  
  * If a wordlist is given, e.g. [hydralein_pwd.txt](./hydralein_pwd.txt), the program runs a Dictionary Attack with it.

### Example Run

* To run a **Brute-Force Attack** with no further specifications use the following command:

    ```bash
    python hydralein.py -u vik -s 127.0.0.1
    ```

> [!NOTE]
> With the default charset (digits and lowercase letters), this attack would require 42.5 days of computing time. Using the --min and --max options would not shorten the processing time much

* To run a **Dictionary Attack** you need this command:  

    ```bash
    python hydralein.py -u vik -s 127.0.0.1 -w hydralein_pwd.txt
    ```

  * It will yield the following **output**:

    ```bash
    Starting a Dictionary Attack on server 127.0.0.1 ...
    Password for user vik is: test123abc.
    Password cracked successfully!
    ```
