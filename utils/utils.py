import os

perm_whitelist = [
    1,
    2,
    3,
    4,
    5,
    588081720436195504,
    6,
    537624465195139076,
    7,
    8,
    9,
    10
]

def hostUsers(roleid):
    # checks if roleid is in whitelist
    return bool(set(perm_whitelist).intersection(set(roleid)))


