#!/usr/bin/env python
import time, argparse, datetime, linecache

## Tool to easily count worked hours.
##

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
today = str(datetime.date.today()) + '.pc'

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
#print(MORNING,LUNCH,RESTARTAFTERLUNCH,GOHOME)

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
    data =  i + "," + str(time.time()) + "\n"
    print(data)
    f.write(data)
f.close()


m = linecache.getline(today,1)
l = linecache.getline(today,2)
r = linecache.getline(today,3)
g = linecache.getline(today,4)

m = float(m.split(',')[1])
m = datetime.datetime.fromtimestamp(m)

l = float(l.split(',')[1])
l = datetime.datetime.fromtimestamp(l)

r = float(r.split(',')[1])
r = datetime.datetime.fromtimestamp(r)

g = float(g.split(',')[1])
g = datetime.datetime.fromtimestamp(g)


morn1 = l - m
print morn1.seconds
noon1 = g - r
print noon1.seconds
total = morn1 + noon1
print("you worked: %s today") %total
## now read the fucking file to see  how many time you've been working.
#>>> import datetime
#>>> a=datetime.datetime.fromtimestamp(1367332369.24)
#>>> b=datetime.datetime.fromtimestamp(1367332379.82)
#>>> c = b - a
#>>> print c
#0:00:10.580000
#>>> c.seconds
#10

#>>> import linecache
#>>> linecache.getline('2013-04-30.pc',1)
#'morning,1367332369.24\n'

