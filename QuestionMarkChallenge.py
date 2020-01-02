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

def question_mark(string):
    positions = []
    qm = 0
    verdict = ''

    # Iterate through provided string
    # Add the index of any integers to an array
    for i in range(len(string)):
        positions.append(i) if string[i].isdigit() else next
    print( '-----')
    print( 'Str: ' + string    )
    print( 'Nums: ' + str(positions) )
    
    # Iterate through the pairs to check for sum total and question mark count
    for i in range(len(positions)-1):
        # If the total isn't 10, skip this pairing and move on
        if string[positions[i]] + string[positions[i+1]] != 10:
            next

        # If there aren't exactly 3 question marks between each pair, move on
        for x in range(positions[i]+1, positions[i+1]):
            if string[x] == '?':
                qm += 1
        if qm == 3: verdict = 'Pass'
        else: verdict = 'Fail'
        qm = 0
        return verdict

print("a = " + str(question_mark(a)))
print("b = " + str(question_mark(b)))
print("c = " + str(question_mark(c)))
print("d = " + str(question_mark(d)))
print("e = " + str(question_mark(e)))
print("f = " + str(question_mark(f)))
print("g = " + str(question_mark(g)))
print("h = " + str(question_mark(h)))
print("i = " + str(question_mark(i)))
print("j = " + str(question_mark(j)))
print("k = " + str(question_mark(k)))
