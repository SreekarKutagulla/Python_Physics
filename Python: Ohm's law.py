class ohm(object):
    def __init__(self,r,i,v):
        self.r=r
        self.i=i
        self.v=v

    def get_volt(self): 
        "Get the Value of Voltage"
        if self.r ==0 or self.i==0:
            return "Values must be greater than '0' "
        else:
            return self.r*self.i

    def get_current(self):
        "Get the value of Current"
        if self.v ==0 or self.r==0:
            return "Values must be greater than '0' "
        else:
            return self.v/self.r

    def get_resistance(self):
        "Get the Value of Resistance"
        if self.v==0 or self.i==0:
            return "Values must be greater than '0' "
        else:
            return self.v/self.i




eye=0 
try:
    r=float(input('Enter Resistance Value , Press Enter if no Value : '))
except:
    eye+=1
try:
    i=float(input('Enter Current Value , Press Enter if no Value : '))
except:
    eye+=1
try:
    v=float(input('Enter Voltage Value , Press Enter if no Value : '))
except:
    eye+=1

if eye>=2 :
    print ('ERRORR: Enter atlest Two Values')


try :
    if r and i :
        v=0
        print ('Voltage = ',ohm(r,i,v).get_volt(),'Volt')
except :
    pass
try:
    if v and r:
        i=0
        print ('Current = ',ohm(r,i,v).get_current(),'Amp')
except :
    pass
try:
    if v and i:
        r=0
        print ('Resistance = ',ohm(r,i,v).get_resistance(),'Ohm')
except :
    pass
