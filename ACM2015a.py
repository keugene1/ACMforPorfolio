"""
    Author: Kyle Cooper
    Description: ACM 2015 Problem A from http://www.icpc-midcentral.us/archives/2015/mcpc2015.pdf

"""

import sys# command line arguments
import string# used to populate dictionary with the alphabet w/o a dict comprehension


def openInput():
    # function to open file with IO exception
    try:
        return open(sys.argv[1], 'r')
    except IOError:
        print('Check filename and try again.', arg)

def calculateScore(fname):
    """function that takes a file and returns that team's final score
    This approach takes advantage of python lists.  Take file lines as
    a list using readlines, then explode(split in python) each list element(all strings).
    Last element can be deleted as it is not useful for this approach."""
    problemList = fname.readlines()
    
    # initialize output
    completeProblems = 0# output 1
    finalTimeScore = 0# output 2
    
    # penalty is a dictionary that keeps track of the penalty time for each problem
    # populated with a-z uppercase
    penalty = dict.fromkeys(string.ascii_uppercase, 0)
    
    # This list comprehension does the splitting. The split removes the newline from
    # the 'right and wrong' values.  The LC could have handled the deletion, but the
    # input file may or may not have a newline at the end.  del was chosen for ease of
    # reading.
    problemList = [x.split() for x in problemList]
    del problemList[-1]
    
    for item in problemList:
        # conditional part 1) if problem is solved correctly, increment the output
        if item[2] == 'right':
            completeProblems += 1
            finalTimeScore = finalTimeScore + int(item[0]) + penalty[item[1]]
        # conditional part 2) if problem is solved incorrectly, apply penalty
        else:
            penalty[item[1]] += 20

    # gather output and return
    output = [completeProblems, finalTimeScore]
    return output


def main():
    problemInput = openInput()
    solution = calculateScore(problemInput)
    print(solution[0], solution[1])
    
main()
