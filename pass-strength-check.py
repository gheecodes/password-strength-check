import re
from colorama import Fore, Style,init

# Initialize colorama
init()

def check_password_strength(password):
    if len(password) < 8:
        return  Fore.RED + "Weak: Password must be at least 8 characters long." + Style.RESET_ALL
    if not re.search(r"[A-Z]",password):
        return Fore.RED + "Weak: Password must contain at least one uppercase letter." + Style.RESET_ALL
    if not re.search(r"[a-z]",password):
        return Fore.RED +  "Weak: Password must contain at least one lowwercase letter." + Style.RESET_ALL
    if not re.search(r"[0-9]",password):
        return Fore.RED +  "Weak: Password must contain at least one digit." + Style.RESET_ALL
    if not re.search(r"[!@#$%^&*(),-.<>?;:'\"{}|_+=-]",password):
        return Fore.RED +  "Weak: Password must contain at least one special character." + Style.RESET_ALL
    if re.search(r"\s",password):
        return Fore.RED +  "Weak: Password must not contain any whitespace." + Style.RESET_ALL
    return Fore.GREEN + "Strong: Password is strong." + Style.RESET_ALL


import time


def main():

    print(Fore.CYAN + "=== Password Strength Checker ===" + Style.RESET_ALL)
    time.sleep(1)
    password = input("Enter your password:")
    result = check_password_strength(password)
    print(result)

if __name__ == "__main__":
    main()


#def main():
  #  password = input("Enter a password to check its strength: ")
   # result = check_password_strength(password)
    
    #if "Weak" in result:
     #   print(Fore.RED + result)
    #else:
     #   print(Fore.GREEN + result)