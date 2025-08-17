import re
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
COMMON_FILE = os.path.join(DATA_DIR, "common_passwords.txt")

def load_common_passwords(filepath="COMMON_File"):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return [line.strip().lower() for line in f if line.strip()]
    except FileNotFoundError:
        return []
    
COMMON_SUBTRINGS = load_common_passwords()


def categorize(password):
    return {
        "lower" : bool(re.search(r"[a-z]", password)),
        "upper" : bool(re.search(r"[A-Z]", password)),
        "digit" : bool(re.search(r"\d", password )),
        "symbol" : bool(re.search(r"[^a-zA-Z0-9]", password))
    }

def has_repeats(password, thr=3):
    return bool(re.search(r"(.)\1{" + str(thr-1)+r",}", password))

def is_sequential(password, w=4):
    if len(password) < w:
        return False
    
    for i in range(len(password)-w+1):
        chunk = password[i:i+w]
        if chunk.isalpha() and "".join(chr(ord(chunk[0])+k) for k in range(w)) == chunk:
            return True
        if chunk.isdigit() and "".join(str(int(chunk[0]) + k) for k in range(w)) == chunk:
            return True

    return False

def contains_common_substrings(password):
    p = password.lower()
    return any(s in p for s in COMMON_SUBTRINGS)

def score_password(password):
    length = len(password)
    cats = categorize(password)
    cat_score = sum(cats.values())

    length_score = min(length, 20) * 3
    diversity = {1:0, 2:10, 3:20, 4:30}[cat_score]

    penalty = 0

    if contains_common_substrings(password): penalty += 25
    if has_repeats(password): penalty+=10
    if is_sequential(password): penalty += 15
    if length<8 : penalty +=20

    raw = max(0, min(100, length_score + diversity - penalty))

    if raw < 30: label = "Very Weak"
    elif raw < 50: label = "Weak"
    elif raw < 70: label = "Moderate"
    elif raw < 85: label = "Strong"
    else: label = "Very Strong"

    tips=[]
    if length < 8: tips.append("Use at least 12-16 characters.")
    if cat_score < 3 : tips.append("Use a mix of uppercase, lowercase, digits, and symbols.")
    if contains_common_substrings(password): tips.append("Avoid words like 'password', 'admin', 'qwerty'.")
    if has_repeats(password): tips.append("Avoid repeats like 'aaa' or '!!!!'.")
    if is_sequential(password): tips.append("Avoid sequences like 'abcd' or '1234'.")
    if not tips: tips.append("Great! prefer a passphrase + use a password manager.")

    return {"score":raw, "label": label, "length": length, "categorize":cats, "tips":tips}
    
    


