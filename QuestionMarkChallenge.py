""" Question Marks Problem """
""" Read a string and return True if there are exactly 3 '?' between every set of numbers that add up to 10 """

#Simplest correct solution (Pass)
a = '5???5'
#Using the same number in two pairs (Pass)
b = 'a5a???a5a???a5a'
#Only require pairs that equal 10 to be ok (Pass)
c ='a5a???a5a???a6a'
#ALL 10 pairs must be valid (Fail)
d = 'a5a???a5aa5a'
#No valid number pairs (Pass)
e = 'a4a???a5a???a6a'
#No instances of either (Pass)
f = 'aa6?9'
#No numbers (Pass)
g = 'aaa?a'
#No Qmarks (Fail)
h = '5aaa5'
#Single number (Pass)
i = 'aa5???aa'
#Dispersed question marks (Pass)
j = 'a5a?a?a?a5a'
# 4Question Marks (False)
k = 'a5a???a?a5a'

def checkfail(qm,start,end):
        # If pairs aren't 10 then we dont care, return Success
        if start + end != 10:
            return 0

        # If pairs are 10 AND 3 question marks, return Success
        elif start + end == 10 and qm == 3:
            return 0
      
        # Else return Fail
        # eg. If pairs equal 10 but not correct question marks, return Fail
        else:
            return 1

def question_mark(string):
    positions = []
    qm,valid = 0,0

    # Iterate through provided string
    # Add the index of any integers to an array
    for i in range(len(string)):
        positions.append(i) if string[i].isdigit() else next

    print( 'Str: ' + string    )
    print( 'Nums: ' + str(positions) )
    
    # Iterate through the pairs to check for sum total and question mark count
    for i in range(len(positions)-1):
        # If the total isn't 10, skip this pairing and move on
        if string[positions[i]] + string[positions[i+1]] != 10:
            next

        
        for x in range( positions[i]+1, positions[i+1] ):
            #Iterate through the chars between each number pair
            if string[x] == '?':
                #Check for question marks
                qm += 1
            valid += checkfail(qm,int(string[positions[i]]),int(string[positions[i+1]]))
        qm = 0 #Reset number of question marks, then move on to the next number pairing

print("a = " + str(question_mark(a)))
