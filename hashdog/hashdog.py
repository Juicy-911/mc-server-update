###################################################################
#                                                                 #
#   Hashdog, homemade tool that aims at mimicking Hashcat         #
#   Author: Juicy                                                 #
#   GitHub: https://github.com/Juicy-911/                         #
#                                                                 #
###################################################################

from subprocess import getoutput
import argparse

parser = argparse.ArgumentParser(description='Apache server exploit (CVE-2021-41773 & 42013)')
parser.add_argument('-m', '--mode', help="Use to change the hash mode (Default: md5)", default="md5", required=False)
parser.add_argument('-f', '--filehash', help="Path to the file containing the hash to crack", default=None, required=True)
parser.add_argument('-w', '--wordlist', help="Path to the file that contains the wordlist", default=None, required=True)
args = parser.parse_args()


hash_padding = -3


def word_to_md5(word):
    hash = (getoutput(f"echo {word} | md5sum"))[:hash_padding]
    #print(f"Mot : {word} -> hash : {hash}")
    return(hash)

def check_hash(hash1, hash2):
    if hash1 == hash2 :
        return(True)
    else :
        return(False)

def main_func(wordlist_file, hash_file):
    with open (hash_file, "r") as hash_file:
        original_hash = hash_file.read().split()[0]
        print("Hash original : ", original_hash)
    with open (wordlist_file, "r") as dico:
        words = dico.read().split()
        for element in words:
            if(check_hash(original_hash, word_to_md5(element))):
                print("Hash cracked !")
                print(f"{original_hash}:{element}")
                return(True)
        return(False)


if __name__ == '__main__':
    print(f"[+] Mode used : {args.mode}")
    print(f"[+] Path of the hashfile : {args.filehash}")
    print(f"[+] Path of the wordlist : {args.wordlist}")
    main_func(args.wordlist, args.filehash)