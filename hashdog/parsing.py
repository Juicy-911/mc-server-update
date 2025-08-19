import argparse

from subprocess import getoutput

###################################################################
#                                                                 #
#   Hashdog, homemade tool that aims at mimicking Hashcat         #
#   Author: Juicy                                                 #
#   GitHub: https://github.com/Juicy-911/                         #
#                                                                 #
###################################################################

parser = argparse.ArgumentParser(description='Apache server exploit (CVE-2021-41773 & 42013)')

parser.add_argument('-m', '--mode', help="Use to change the hash mode (Default: md5)", default="md5", required=False)
parser.add_argument('-f', '--filehash', help="Path to the file containing the hash to crack", default=None, required=True)
parser.add_argument('-w', '--wordlist', help="Path to the file that contains the wordlist", default=None, required=True)


args = parser.parse_args()

if __name__ == '__main__':
    print(f"[+] Mode used : {args.mode}")
    print(f"[+] Path of the hashfile : {args.filehash}")
    print(f"[+] Path of the wordlist : {args.wordlist}")
    