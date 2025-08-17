def charset_size(password):
    size=0
    if any(c.islower() for c in password):size+=26
    if any(c.isupper() for c in password):size+=26
    if any(c.isdigit() for c in password):size+=10
    if any(not c.isalnum() for c in password):size+=33
    return size if size > 0 else 1

def _humanize(seconds):
    units = [("years", 365*24*3600), ("days", 24*3600), ("hours", 3600), ("minutes", 60), ("seconds", 1)]
    out=[]
    for name, unit in units:
        if seconds >= unit:
            val = int(seconds // unit)
            seconds -= val*unit
            out.append(f"{val} {name}")
    return ", ".join(out) 

def estimate_bruteforce_time(password, guesses_per_second=1e9):
    N = charset_size(password)
    L = len(password)
    total = N**L
    avg_guesses = total /2
    seconds = avg_guesses / guesses_per_second
    return {
        "charset_size":N,
        "length":L,
        "avg_guesses":avg_guesses,
        "time_at_1e9_gps" : _humanize(seconds),
        "time_at_1e6_gps" : _humanize(avg_guesses / 1e6),
        "time_at_1e3_gps" : _humanize(avg_guesses / 1e3),
    }

