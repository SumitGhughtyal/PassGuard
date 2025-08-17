import os 
import time

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
COMMON_FILE = os.path.join(DATA_DIR, "common_passwords.txt")

def load_dictionary(filepath=COMMON_FILE):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[!] Dictionary file not found: {filepath}")
        return []
    
def dictionary_attack(password : str, dictionary_file = COMMON_FILE) -> dict:
    dictionary = load_dictionary(dictionary_file)
    if not dictionary:
        return {"success" : False, "attempts":0, "time": 0, "match": None}
    
    start = time.time()
    for attempts, word in enumerate(dictionary, start=1):
        if password.lower() == word.lower():
            elapsed = time.time() - start
            return {
                "success": True,
                "attempts": attempts,
                "time": elapsed,
                "match":word,
            }
    
    elapsed = time.time() - start
    return {"success": False, "attempts": len(dictionary), "time": elapsed, "match":None}


