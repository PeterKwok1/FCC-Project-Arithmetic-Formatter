import operator as ops
# print(ops.add(1,1))

problem = "32 + 8"
#   32    
# +  8    
# ----    
#   40    

def problemSolver(problem):
    pieces = problem.split()
    print(pieces)

problemSolver(problem)

# answer --
# produce answer to get all pieces 
# split 
# operator table 
# format -- 
# indentation based on longest operand
# single space between operator and longest operand 
# operator will be on lowest line
# dashes underline problem 
# 4 spaces between problems

# loop
problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474

# fcc test
# arithmetic_arranger(
# ["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True
# ) should return
#    32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028



