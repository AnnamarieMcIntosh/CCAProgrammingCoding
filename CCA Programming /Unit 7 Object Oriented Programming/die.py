# die.py
'''
Die Class - Lab 7
<Annamarie McIntosh>
'''

DIE_PICS = ['''
-----------
+         +
+         +
+         +
+         +
+         +
-----------''','''
-----------
+         +
+         +
+    0    +
+         +
+         +
-----------''','''
-----------
+         +
+  0      +
+         +
+      0  +
+         +
-----------''','''
-----------
+ 0       +
+         +
+    0    +
+         +
+       0 +
-----------''','''
-----------
+         +
+  0   0  +
+         +
+  0   0  +
+         +
-----------''','''
-----------
+         +
+  0   0  +
+    0    +
+  0   0  +
+         +
-----------''','''
-----------
+  0   0  +
+         +
+  0   0  +
+         +
+  0   0  +
-----------''']



import random

class Die:
    def __init__(self):
        '''Constructor'''
        self.__face = 0

    def value(self):
        '''Return a current die face value, returns 0 if die has not been rolled.'''
        return self.__face

    def roll(self):
        '''Roll the die'''
        '''Should set the dice face to a randome value between 1 and 6.'''
        self.__face = random.randint(1,6)

    def pick_up(self):
        '''Pick-up the die'''
        '''Should reset the dice face to the unrolled state, 0.'''
        self.__face = 0

    def __str__(self):
        '''Special Python function, converts object to a string, used in print().'''
        '''Use the DIE_PICS list to display the current value'''
        return DIE_PICS[self.__face]

