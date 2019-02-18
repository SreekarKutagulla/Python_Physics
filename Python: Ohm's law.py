
eye=0

###############################
r= input('Enter Resistance Value , Press x if no Value : ')

if r != str("x"):
    r = float(r)
if r == str("x") :
    eye = eye + 1
    
#############################

i= input('Enter Current Value , Press x if no Value : ')
if i != str("x"):
    i = float(i)
if i == str("x") :
    eye = eye + 1

#############################

v= input('Enter Voltage Value , Press Enter x if no Value : ')
if v != str("x"):
    v = float(v)
if v == str("x") :
    eye = eye + 1

#################################

if eye > 1 :
    print ('ERROR: Please enter only one x')

if v == "x":
        print(str(float( r * i)) + " Volts")

if i == "x":
        print(str(float(v/r)) + " Amps")


if r == "x":
        print (str(float(v/c)) + " Ohms")

