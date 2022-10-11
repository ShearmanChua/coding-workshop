from sys import stdin, stdout

lines_to_check = stdin.readlines()
lines_cleaned = []

for line in lines_to_check:
    line_cleaned = line.strip()
    if line_cleaned[:2] == "//" and (line_cleaned[-1] == ";" or line_cleaned[-1] == "{"):
        continue
    else:
        lines_cleaned.append(line)

lines_cleaned = ''.join(lines_cleaned)
print(lines_cleaned)
