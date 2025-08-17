import os
import sys
from colorama import Fore, Style, init

init(autoreset=True)

BASE_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.join(BASE_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from strength_checker import score_password
from bruteforce_estimator import estimate_bruteforce_time
from simulated_dictionary_attack import dictionary_attack

def run_analysis(password: str):
    print(Fore.CYAN + "\n========== Password Security Report ==========\n")

    # Strength Checker
    strength = score_password(password)
    print(Fore.YELLOW + "🔐 Strength Analysis")
    print(Fore.YELLOW + "--------------------")
    label_color = {
        "Weak": Fore.RED,
        "Moderate": Fore.YELLOW,
        "Strong" : Fore.GREEN,
    }.get(strength['label'], Fore.WHITE)

    print(f"Length: {Fore.CYAN}{strength['length']}{Style.RESET_ALL}")
    print(f"Score: {label_color}{strength['score']}/100 ({strength['label']}){Style.RESET_ALL}")
    print(f"Character categories: {Fore.CYAN}{strength['categorize']}{Style.RESET_ALL}")
    print("Tips")
    for tip in strength['tips']:
        print(Fore.MAGENTA + f" - {tip}")
    print()

    # Brute Force Estimation
    estimate = estimate_bruteforce_time(password)
    print(Fore.YELLOW + "⚡ Brute Force Resistance")
    print(Fore.YELLOW + "-------------------------")
    print(f"Charset size : {Fore.CYAN}{estimate['charset_size']}{Style.RESET_ALL}")
    print(f"Password len : {Fore.CYAN}{estimate['length']}{Style.RESET_ALL}")
    print(f"Avg guesses  : {Fore.CYAN}{estimate['avg_guesses']:.2e}{Style.RESET_ALL}")
    print(f"Time @ 1e9/s : {Fore.GREEN}{estimate['time_at_1e9_gps']}{Style.RESET_ALL}")
    print(f"Time @ 1e6/s : {Fore.YELLOW}{estimate['time_at_1e6_gps']}{Style.RESET_ALL}")
    print(f"Time @ 1e3/s : {Fore.RED}{estimate['time_at_1e3_gps']}{Style.RESET_ALL}")
    print()

    # Dictionary Attack
    result = dictionary_attack(password)
    print(Fore.YELLOW + "📖 Dictionary Attack Simulation")
    print(Fore.YELLOW + "--------------------------------")
    if result["success"]:
        print(
            Fore.RED
            + f"[+] Password found in dictionary after {result['attempts']} attempts"
        )
        print(Fore.RED + f"    -> Match: {result['match']}")
        print(Fore.RED + f"    -> Time Taken: {result['time']:.6f} seconds")
    else:
        print(Fore.GREEN + "[-] Password NOT found in dictionary")
        print(
            Fore.GREEN
            + f"Tried {result['attempts']} words in {result['time']:.6f} seconds"
        )
    
    print(Fore.CYAN + "\n=============================================\n")

if __name__ == "__main__":
    password = input(Fore.CYAN + "Enter a password to analyze: " + Style.RESET_ALL)
    run_analysis(password)


