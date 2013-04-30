#!/usr/bin/env python
import time, argparse, datetime

parser = argparse.ArgumentParser(
    prog = 'punchcard.py',                                                           # the name of the program
    description = "This is a tool to track worked hours",     # text displayed on top of --help
    epilog = 'just an example of the beauty of the code.')                                  # last text displayed 

parser.add_argument('-V', '--version', action='version', version='%(prog)s 0.1')
parser.add_argument('-M','--morning',action="store_true",dest='morning',help='arrival hour in the morning')
parser.add_argument('-L','--lunch',action="store_true",dest='lunch',help='lunch break')
parser.add_argument('-R','--restartafterlunch', action="store_true",dest='restartafterlunch',help='restart after lunch time')
parser.add_argument('-G','--gohome',action="store_true",dest='gohome',help='hour of depart')
arguments = parser.parse_args()

morning  = arguments.morning
lunch = arguments.lunch
restartafterlunch = arguments.restartafterlunch
gohome=arguments.gohome
MORNING=LUNCH=RESTARTAFTERLUNCH=GOHOME=False
# need to open 1 file per day instead of punchtime.db
today = str(datetime.date.today())

# if there is an duplicate entry/day/dicto the first one counts
open(today,'a').close()

dataonfile=open(today,'r')
for line in dataonfile.readlines():
  if 'morning' in line:
    MORNING=True
  if 'lunch' in line:
    LUNCH=True
  if 'restartafterlunch' in line:
    RESTARTAFTERLUNCH=True
  if 'gohome' in line:
    GOHOME=True
dataonfile.close()
print(MORNING,LUNCH,RESTARTAFTERLUNCH,GOHOME)

f = open(today,'a+')
dicto =  {'morning':morning,'lunch':lunch,'restartafterlunch':restartafterlunch,'gohome':gohome}
if MORNING  == True:
  print("Already punched this morning")
  dicto.pop('morning',None)
if LUNCH == True:
  print("Already punched for lunck")
  dicto.pop('lunch',None)
if RESTARTAFTERLUNCH == True:
  print("Already punched back from lunch")
  dicto.pop('restartafterlunch',None)
if GOHOME == True:
  print("Already went home")
  dicto.pop('gohome',None)

filedata = f.read()
for i in dicto:
  if dicto[i]==True:
    #data = filedata + i + "," + time.ctime() + "\n"
    data =  i + "," + time.ctime() + "\n"
    print(data)
    f.write(data)
f.close()


## now read the fucking file to see  how many time you've been working.
#>>> import datetime
#>>> a = datetime.datetime.now()
#>>> b = datetime.datetime.now()
#>>> d = b - a
#>>> d.seconds
#10


