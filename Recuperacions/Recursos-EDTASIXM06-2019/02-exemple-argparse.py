# /usr/bin/python
#-*- coding: utf-8-*-
#
# head [file]
#  10 lines, file o stdin
# -------------------------------------
# @ edt ASIX M06 Curs 2018-2019
# Gener 2018
# -------------------------------------
import argparse
parser = argparse.ArgumentParser(description=\
        """exemple de processar arguments""",\
        prog="exemple.py",\
        epilog="thats all folks")
parser.add_argument("-e","--edat",type=int, help="edat (int)",dest="useredat",metavar="laedat")
parser.add_argument("fit",type=str,help="fitxer",\
        metavar="elfitxer")
#parser.add_argument("--verbosity",help="ser verbose")
args=parser.parse_args()
print(parser)
print(args)
exit(0)

