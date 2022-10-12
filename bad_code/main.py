strings = ["apple","pear","orange","-123?"]

def is_valid(entry):
    return entry.isalnum()

def get_valid_entries(ls):
    return [entry for entry in ls if is_valid(entry)]

print(get_valid_entries(strings))
