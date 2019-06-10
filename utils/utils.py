perm_whitelist = {
    "admin": 537624465195139076
}

def cmd_permission(perm):
    return perm_whitelist.get(perm)