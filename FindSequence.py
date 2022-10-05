#FindSequence():
    #Goal: Create a pythonic function which finds the shortest route from 1 to
    #a target number, using only increment() and square() functions

#Increment() and square() are very simple functions which are used as primitives
    #A primitive is the lowest-level unit of data that a program interfaces with
    #Usually things like "int" or "byte"
def increment(givenVal):
    return givenVal+1

def square(givenVal):
    return givenVal**2

#Apply() is a combination that takes a list of functions as argument 1,
#and a starting value as argument 
#It recursively runs through each given function, one at a time
def apply(funcList, value):
    if(len(funcList) < 1):
        return value
    else:
        #Remove the first function in funcList, apply it to value
        #Keep rest of functions in funcList
        #Call apply() again, with new funcList and new value
        return apply(funcList[1:len(funcList)], funcList[0](value))

#findNext appends a "next possible step" to a given list of functions
    #First parameter is the current list of functions
    #Second parameter is the list of possible next-steps
    #Returns a list of possible funcLists, with each next step appended
def addNext(funcList, stepList):
    #retList is a list of lists
    retList = []
    #For each possible next-step, retList holds a list
    #Each list is "All the previous steps",
        #then "One of the next possible steps"
    for idx, x in enumerate(stepList):
        retList.append(funcList[:])
        retList[idx].append(x)
    return retList

#Given a starting number, finds the shortest sequence of
#increment() and square() calls  such that the result is the end number
def findSequence(givenStart, givenEnd):
    retList = []
    if(givenStart >= givenEnd):
        print("Start position is not less than end position.")
        return
    #maximum size of sequence consists of all increment()
    for x in range(givenStart, givenEnd):
        
