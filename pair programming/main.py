from sys import stdin
import re

def check_valid_string(input_text):
    valid_str = re.compile(r'.*\(\).*', re.IGNORECASE)
    # print(input_text.split("\""))
    if (valid_str.match(input_text) and "() ->" not in input_text) or len(input_text.split("\"")) > 4 or (not input_text.split(",")[-1].strip().isalnum() and "() ->" not in input_text):
        return True
    else:
        return False

lines = stdin.readlines()

complete_statements = []
complete_statement_line = []
ran_lines = []
for line in range(0,len(lines)):
    complete_line = ""
    if not lines[line].startswith('//') and "logger.debug" in lines[line]:
        complete_line += lines[line]
        count = 1
        while ";" not in complete_line:
            complete_line += lines[line + count]
            count += 1
        complete_line = complete_line.replace("\n","")
        complete_line = complete_line[complete_line.find("logger.debug(")+13:complete_line.find(";") - 1]
        
        # print(complete_line)
        if check_valid_string(complete_line):
           print(line + 1)
        