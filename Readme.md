# 🔐 PassGuard: Password Security Analyzer

This project is a web-based tool built with Streamlit to analyze the strength of a password. It provides a comprehensive, interactive security report that includes a strength score, an estimation of the time required for a brute-force attack, and a check against a list of common passwords, all presented in a clean and modern user interface.

## Features

* **Interactive Web Interface:** A sleek, dark-themed UI built with Streamlit for a user-friendly experience.
* **Strength Analysis:** Scores the password on a scale of 0-100 based on length, character diversity, and common patterns. It also provides actionable tips for improvement.
* **Brute-Force Estimation:** Calculates the estimated time to crack the password using brute-force methods at different guessing speeds (from an offline attack to a supercomputer).
* **Dictionary Attack Simulation:** Checks if the password is in a list of commonly used passwords to identify major vulnerabilities.

## Requirements

* Python 3.x
* `streamlit`

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/PassGuard.git](https://github.com/your-username/PassGuard.git)
    cd PassGuard
    ```

2.  **Install the required library:**
    ```bash
    pip install streamlit
    ```

## Usage

To run the password analysis tool, execute the `streamlit.py` script from your terminal:

```bash
streamlit run streamlit.py
````

This will launch the web application in your default browser, where you can enter a password to begin the analysis.

