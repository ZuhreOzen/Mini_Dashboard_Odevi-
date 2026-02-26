import random

def get_info():
    dereceler = [15, 20, 25, 30]
    durumlar = ["Gunesli", "Yagmurlu", "Ruzgarli"]
    return f"Hava su an {random.choice(dereceler)} derece ve {random.choice(durumlar)}."
