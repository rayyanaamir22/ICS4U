'''
Name: Rayyan Aamir
Date: May 30, 2022
Program: Object Oriented Sorting and Searching
'''

# Modules
import os
import timeit

# Other files
import functions as f
import insertionSort as ins
import linearSearch as lin
import binarySearch as bin
import dataGen as dg

def main(): # Main function
  # Create array
  test = dg.generateData(1000) # OBJECTS
  while True: # Program loop
    # Title
    print('OBJECT ORIENTED ALGORITHMS\n')
    print(f'Original array: {test[0:19]}...\n{test[-20:-1]}\n')    
    
    #----------------SORTING ALGORITHMS----------------
    
    # Insertion test
    startTime = timeit.default_timer()
    ins.insertionSort(test, 'x')
    print('\nInsertion time:', timeit.default_timer() - startTime)
    
    # Builtin test
    startTime = timeit.default_timer()
    test.sort(key=lambda n: n.x) 
    print('\nBuiltin time:', timeit.default_timer() - startTime)
  
    print(f'\nSorted list: {test[0:19]}...\n{test[-20:-1]}\n')
    
    #-----------DEFINE SEARCHING ALGORITHM-------------
    
    print('\n')
    # Choose search method
    searchAlgorithm = ''
    while searchAlgorithm not in ['LINEAR', 'BINARY']:
      print('Do you want to run LINEAR or BINARY search algorithm?')
      searchAlgorithm = input().upper()
  
      print('\n')
    # Choose search process
    algorithmType = ''
    while algorithmType not in ['ITERATIVE', 'RECURSIVE']:
      print('Do you want to use the ITERATIVE or RECURSIVE method?')
      algorithmType = input().upper()
  
    print('\n')
    # Choose target value for search
    algorithmTarget = test[0].x - 1
    # While target is outside of test's scope
    while algorithmTarget < test[0].x or algorithmTarget > test[-1].x:
      print(f'Select a target within the scope of the test array: [{test[0].x}, {test[-1].x}]')
      try:
        algorithmTarget = int(input())
      except (TypeError, ValueError):
        print('Enter a number.')
  
    #----------------RUN SEARCH ALGORITHM--------------
  
    # recursiveLinearSearch() causes StackOverflowError with data larger than 1 000 units.
    # recursiveBinarySearch() does not suffer this as it cuts the dataset in half, so to have it crash the data must be 2^1000 (10^304) units long.
    
    print('\n')
    print('Target is present at index: ', end='')
    startTime = timeit.default_timer() # Timer starts here
    
    if searchAlgorithm == 'LINEAR' and algorithmType == 'ITERATIVE': 
      print(lin.iterativeLinearSearch(test, algorithmTarget, 'x'))
      print('Algorithm time:', timeit.default_timer() - startTime)
    elif searchAlgorithm == 'LINEAR' and algorithmType == 'RECURSIVE': 
      print(lin.recursiveLinearSearch(test, 0, len(test)-1, algorithmTarget, 'x'))
      print('Algorithm time:', timeit.default_timer() - startTime)
    elif searchAlgorithm == 'BINARY' and algorithmType == 'ITERATIVE': 
      print(bin.iterativeBinarySearch(test, 0, len(test)-1, algorithmTarget, 'x'))
      print('Algorithm time:', timeit.default_timer() - startTime)
    elif searchAlgorithm == 'BINARY' and algorithmType == 'RECURSIVE': 
      print(bin.recursiveBinarySearch(test, 0, len(test)-1, algorithmTarget, 'x'))
      print('Algorithm time:', timeit.default_timer() - startTime)

    #------------------------REUSE---------------------

    if f.reuse('SEARCH'):
      os.system('clear')
      continue
    else:
      os.system('clear')
      print('Goodbye.')
      break

if __name__ == '__main__':
  main()
