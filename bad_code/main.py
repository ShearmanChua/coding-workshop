VALID = "valid"
INVALID = "invalid"

def is_valid(entry):
    return len(entry) > 0

ls = ["apple","pear","","orange"]

validity_statements = [VALID if is_valid(entry) else INVALID for entry in ls] 
print(validity_statements)
