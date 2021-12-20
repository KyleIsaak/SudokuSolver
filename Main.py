from Heuristics import Heuristics
from TextToMatrix import *
from BreadthFirstSearch import *
from DepthFirstSearch import *
from SequentialSearch import *
from RandomSearch import *
from GreedySearch import *


import sys
import time

import csv

RESTRICTEDPUZZLESAMOUNT = 40000

#Restrict to only 40,000 puzzles
def openCSV(file):
    list = []
    header = True
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if header == False:
                list.append(row[0])
            #Gets rid of the header
            header = False
            if len(list) == RESTRICTEDPUZZLESAMOUNT:
                return list
    return list

#Answers to the 40,000 puzzles
def answerCSV(file):
    list = []
    header = True
    with open(file, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if header == False:
                list.append(row[1])
            #Gets rid of the header
            header = False
            if len(list) == RESTRICTEDPUZZLESAMOUNT:
                return list
    return list

#Driver program
#To run, type python Main.py (Txt file)
#Ex: python Main.py sudoku.csv

def main():
    SIZE = 9
    file = sys.argv[1]
    
    #Sequence of 81 numbers
    contents = openCSV(file)
    answers = answerCSV(file)
   
    #initialPuzzle = ConvertTextToMatrix(contents[0],SIZE)
    #answerPuzzle = ConvertTextToMatrix(answers[0],SIZE)
    
    #print("Answers Matrix")
    #print(answerPuzzle)

    #print("Initial Matrix")
    #print(initialPuzzle)
    ########Different search techniques#########
    
    #-------------------------------------------------------------------------------

    # BFS
    '''
    for puzzle in range(len(contents)):
        initialPuzzle = ConvertTextToMatrix(contents[puzzle],SIZE)
        answerPuzzle = ConvertTextToMatrix(answers[puzzle],SIZE)
        
        testPuzzle = initialPuzzle.copy()
        start_time = time.time()
        BFSPuzzle = BreadthFirstSearch(testPuzzle)
        end_time = time.time()
        print("") #Spacer
        print("") #Spacer
        print("") #Spacer
        print("Initial Puzzle:")
        print(initialPuzzle)
        print("BFS Puzzle:")
        print(BFSPuzzle)
        print("--- %s seconds ---" % (end_time - start_time))
    '''  


    ## DFS  
    '''
    for puzzle in range(len(contents)):
        initialPuzzle = ConvertTextToMatrix(contents[puzzle],SIZE)
        answerPuzzle = ConvertTextToMatrix(answers[puzzle],SIZE)

        testPuzzle = initialPuzzle.copy()
        start_time = time.time()
        DFSPuzzle = DepthFirstSearch(testPuzzle)
        end_time = time.time()
        print("") #Spacer
        print("") #Spacer
        print("") #Spacer
        print("DFS Puzzle:")
        print(DFSPuzzle)
        print("--- %s seconds ---" % (end_time - start_time))
    '''


    ## Random
    '''
    for puzzle in range(len(contents)):
        initialPuzzle = ConvertTextToMatrix(contents[puzzle],SIZE)
        answerPuzzle = ConvertTextToMatrix(answers[puzzle],SIZE)

        testPuzzle = initialPuzzle.copy()
        start_time = time.time()
        RandomPuzzle = RandomSearch(testPuzzle)
        end_time = time.time()
        print("") #Spacer
        print("") #Spacer
        print("") #Spacer
        print("Random Search Puzzle:")
        print(RandomPuzzle)
        print("--- %s seconds ---" % (end_time - start_time))
    '''

    '''
    ## Greedy Rows
    start_time = time.time()
    for puzzle in range(len(contents)):
        initialPuzzle = ConvertTextToMatrix(contents[puzzle],SIZE)
        answerPuzzle = ConvertTextToMatrix(answers[puzzle],SIZE)
        testPuzzle = initialPuzzle.copy()
        
        #start_time = time.time()
        GreedyPuzzle = GreedySearch(testPuzzle, 'rows')
        #end_time = time.time()

        #print("") #Spacer
        #print("") #Spacer
        #print("") #Spacer
        #print("Greedy Search Puzzle:")
        #print(GreedyPuzzle)

    end_time = time.time()
    print("--- %s seconds ---" % (end_time - start_time))
    '''

    
    ## Greedy Columns
    
    start_time = time.time()
    for puzzle in range(len(contents)):
        initialPuzzle = ConvertTextToMatrix(contents[puzzle],SIZE)
        answerPuzzle = ConvertTextToMatrix(answers[puzzle],SIZE)
        testPuzzle = initialPuzzle.copy()
        
        #start_time = time.time()
        GreedyPuzzle = GreedySearch(testPuzzle, 'columns')
        #end_time = time.time()

        #print("") #Spacer
        #print("") #Spacer
        #print("") #Spacer
        #print("Greedy Search Puzzle:")
        #print(GreedyPuzzle)

    end_time = time.time()
    print("--- %s seconds ---" % (end_time - start_time))
    


    
    ## SINGLE GREEDY TESTS
    '''
    initialPuzzle = ConvertSingleFileToMatrix(file)


    # Rows
    initialPuzzle = ConvertSingleFileToMatrix(file)
    print("Initial Puzzle:")
    print(initialPuzzle)
    print("") #Spacer
    print("") #Spacer
    print("") #Spacer

    testPuzzle = initialPuzzle.copy()
        
    start_time = time.time()
    GreedyPuzzle = GreedySearch(testPuzzle, 'rows')
    end_time = time.time()

    print("") #Spacer
    print("") #Spacer
    print("") #Spacer
    print("Greedy Rows Puzzle:")
    print(GreedyPuzzle)

    print("--- %s seconds ---" % (end_time - start_time))


    # Columns
    testPuzzle = initialPuzzle.copy()
        
    start_time = time.time()
    GreedyPuzzle = GreedySearch(testPuzzle, 'columns')
    end_time = time.time()

    print("") #Spacer
    print("") #Spacer
    print("") #Spacer
    print("Greedy Columns Puzzle:")
    print(GreedyPuzzle)

    print("--- %s seconds ---" % (end_time - start_time))
    '''

    '''
    # Cells
    testPuzzle = initialPuzzle.copy()
        
    start_time = time.time()
    GreedyPuzzle = GreedySearch(testPuzzle, 'cells')
    end_time = time.time()

    print("") #Spacer
    print("") #Spacer
    print("") #Spacer
    print("Greedy Cells Puzzle:")
    print(GreedyPuzzle)

    print("--- %s seconds ---" % (end_time - start_time))
    '''


    #TODO
    '''
    for puzzle in range(len(contents)):
        initialPuzzle = ConvertTextToMatrix(contents[puzzle],SIZE)
        answerPuzzle = ConvertTextToMatrix(answers[puzzle],SIZE)
        testPuzzle = initialPuzzle.copy()
        start_time = time.time()
        HeuristicPuzzle = Heuristics(testPuzzle)
        end_time = time.time()
        print("") #Spacer
        print("") #Spacer
        print("") #Spacer
        print("Heuristics Puzzle:")
        print(HeuristicPuzzle)
        print("--- %s seconds ---" % (end_time - start_time))
    '''
    


main()