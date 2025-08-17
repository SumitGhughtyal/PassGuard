# Password Security Analyzer

This project is a command-line tool to analyze the strength of a password. It provides a comprehensive security report that includes a strength score, an estimation of the time required for a brute-force attack, and a check against a list of common passwords.

## Features

* **Strength Analysis:** Scores the password on a scale of 0-100 based on length, character diversity, and common patterns. It also provides tips for improvement.
* **Brute-Force Estimation:** Calculates the estimated time to crack the password using brute-force methods at different guessing speeds.
* **Dictionary Attack Simulation:** Checks if the password is in a list of commonly used passwords.

## Requirements

* Python 3.x
* `colorama` library

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/password-security-analyzer.git](https://github.com/your-username/password-security-analyzer.git)
    cd password-security-analyzer
    ```

2.  **Install the required library:**
    ```bash
    pip install colorama
    ```

## Usage

To run the password analysis, execute the `main.py` script:

```bash
python main.py