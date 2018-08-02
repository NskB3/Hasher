import hashlib
import itertools
import sys

hash = input("Hash to crack: ").replace(' ', '')
tested = []
def dictionary():
    wlist = input("Wordlist: ")
    try:
        f = open(wlist, 'r').readlines()
    except IOError:
        print("Wordlist not found!")
        quit()
    for guess in f:
        newhash = hashlib.sha256(guess.encode("utf-8")).hexdigest()
        if newhash == hash:
            print("\nHash Cracked:", guess)
        else:
            print("\nTried: " + str(guess))
def brute():
    charset = input("Charset: ")
    for length in range(1, 9999):
        gen = itertools.product(charset, repeat=length)
        for i in gen:
            new = hashlib.sha256(''.join(i).encode("utf-8")).hexdigest()
            if new == hash:
                frst = ''.join(i).replace(',', '')
                frstt = frst.replace('(', '')
                frsttt = frstt.replace(')', '')
                print("\nHash Cracked:", frsttt)
                quit()
            else:
                frst = ''.join(i).replace(',', '')
                frstt = frst.replace('(', '')
                frsttt = frstt.replace(')', '')
                tested.append(frsttt)
                sys.stdout.write("\rTested %s Combinations" % str(len(tested)))
                sys.stdout.flush()
print("""
1. Dictionary Attack
2. Bruteforce
""")
choose = input(">> ")
if choose == "1":
    dictionary()
elif choose == "2":
    brute()
else:
    print("Not a valid option")
    quit()
