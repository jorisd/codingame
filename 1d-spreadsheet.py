# https://www.codingame.com/training/easy/1d-spreadsheet

import sys
import math
import functools

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

line=0

class Spreadsheet:
    sheet = [] 

    @classmethod
    def add(cls, cell):
        cls.sheet.append(cell)
    
    @classmethod
    def lookup(cls, cell):
        return cls.sheet[cell].value()

    @classmethod
    def get_sheet(cls):
        return cls.sheet


class Cell:
    def __init__(self, op, value1=None, value2=None):
        self.op = op
        self.value1 = value1
        self.value2 = value2

        #global line
        #line += 1
        #print("Debug messages...", line, self.op, self.value1, self.value2, file=sys.stderr, flush=True)
    ''' Used to memoize / speedup values already calculated '''
    @functools.cache
    def value(self):
        if self.op == "VALUE":
            if '$' in str(self.value1):
                val1 = Spreadsheet.lookup(int(str(self.value1).replace('$', '')))
                return int(val1)
            else:
                return self.value1

        val1 = None
        val2 = None

        if '$' in str(self.value1):
            val1 = Spreadsheet.lookup(int(str(self.value1).replace('$', '')))
        else:
            val1 = self.value1

        if '$' in str(self.value2):
            val2 = Spreadsheet.lookup(int(str(self.value2).replace('$', '')))
        else:
            val2 = self.value2
        
        if self.op == "MULT":
            return int(val1) * int(val2)
        elif self.op == "ADD":
            return int(val1) + int(val2)
        elif self.op == "SUB":
            return int(val1) - int(val2)


n = int(input())
for i in range(n):
    operation, arg_1, arg_2 = input().split()
    Spreadsheet.add(Cell(operation, arg_1, arg_2))


for cell in Spreadsheet.get_sheet():
    print(cell.value())
