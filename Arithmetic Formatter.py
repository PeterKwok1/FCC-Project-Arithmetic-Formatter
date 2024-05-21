import operator as ops
# print(ops.add(1,1))

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

key = {
    '+': ops.add,
    '-': ops.sub
}

def pad(str, paddding):
    # append padding, slice from end 
    pass

def solve_problems(problems):
    problems_formatted = []
    for i in range(len(problems)):
        problems[i] = problems[i].split()
        operand_one = problems[i][0]
        operand_two = problems[i][2]
        operator = problems[i][1]
        solution = str(key[operator](int(operand_one), int(operand_two)))
        problems[i].append(solution) # to compare length 

        problems_formatted.append([])
        return_length = lambda l : len(l)
        length = len(max(problems[i], key = return_length)) + 2 # + 2 for space operator + space
        # pad twice, once for length, another 4
        # append to list 

        # combine operator and operand_two
        # add line

    # remove spaces from first problem and add line breaks to last 

    # print(problems, problems_formatted)

solve_problems(problems)

# answer --
# solve to get all pieces 
# split
# operator table 
# format -- +
# replace with formatted string and combine
# indentation based on longest operand
# single space between operator and longest operand 
# operator will be on lowest line
# dashes underline problem 
# 4 spaces between problems

