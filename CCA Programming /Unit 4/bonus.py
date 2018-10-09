# Loops Unit 4 - Bonus
# Annamarie McIntosh

def ninety_nine_bottles():
    times = 99
    while times > 0:
        print ("%s bottles of root beer on the wall, %s bottles of root beer. Take one down, pass it around, %s bottles of root beer on the wall." % (times, times, times - 1))
        times = times - 1
