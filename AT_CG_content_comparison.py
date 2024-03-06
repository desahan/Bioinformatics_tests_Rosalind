all_fastas = {}

current_key = None

f = open("rosalind_gc.txt", "r")
for lines in f:
    lines = lines.replace("\n", "")
    if lines[0] == ">":
        current_key = lines
        all_fastas[current_key] = ""
    if all_fastas[current_key] == "":
        all_fastas[current_key] = lines
    else:
        all_fastas[current_key] += lines

AC_content = {}

for keys in all_fastas:
    all_fastas[keys] = all_fastas[keys][14:len(all_fastas[keys])]

    count_AT = all_fastas[keys].count("A") + all_fastas[keys].count("T")
    count_CG = all_fastas[keys].count("C") + all_fastas[keys].count("G")
    perc = (100 * count_CG) / (count_AT + count_CG)
    perc = round(perc, 6)
    AC_content[keys] = perc

biggest = 0
biggest_key = ""

for keys in AC_content:
    if AC_content[keys] > biggest:
        biggest = AC_content[keys]
        biggest_key = keys

print(biggest_key)
print(biggest)
