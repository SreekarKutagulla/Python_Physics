
units = input(" Unit for distance: ")

units1 = input( " Unit for time: ")

fspeed = float(input(" Put in Final speed: "))

ispeed = float(input(" Put in Initial speed: "))

time = float(input(" Put in time: "))

answer = float((fspeed - ispeed)/ time)

if answer < 0.0:
    print( "The object decelerates by " + str(answer) +  units + "/" + units1 + "2")

if answer > 0.0:
    print( "The object accelerates by " + str(answer) +  units + "/" + units1 + "2")

if answer == 0:
    print(" The object is not accelerating nor decelerating. It is constant")

