import operator as ops
# print(ops.add(1,1))
import re

problems = ["3801 - 2", "123 + 49"]
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

def pad(str, padding):
    # python string format method 
    padded = f"{str:{' '}{'>'}{padding}}"
    return padded

def solve_problems(problems, show_answers = False):
    # validation 
    if len(problems) > 5:
        return 'Error: Too many problems.'
    if re.search('[*/]', ' '.join(problems)):
        return "Error: Operator must be '+' or '-'."
    if re.search('[a-zA-Z]', ' '.join(problems)):
        return 'Error: Numbers must only contain digits.'
    if re.search(r'\d{5}', ' '.join(problems)):
        return 'Error: Numbers cannot be more than four digits.'

    problems_formatted = []
    for i in range(len(problems)):
        problems[i] = problems[i].split()
        operand_one = problems[i][0]
        operand_two = problems[i][2]
        operator = problems[i][1]
        solution = str(key[operator](int(operand_one), int(operand_two)))

        # append formatted problem
        # pad twice: length, length + 4
        return_length = lambda l : len(l)
        length = len(max(problems[i], key = return_length)) + 2 # + 2 for space operator + space
        formatted = []
        formatted.append(pad(pad(operand_one, length), length + 4))
        formatted.append(pad(operator + pad(operand_two, length - 1), length + 4))
        formatted.append(pad('-' * length, length + 4)) 
        formatted.append(pad(pad(solution, length), length + 4))
        problems_formatted.append(formatted)
        
    # remove spaces from first problem and add line breaks to last 
    for j in range(len(problems_formatted[-1])):
        problems_formatted[-1][j] += '\n'
    for k in range(len(problems_formatted[0])):
        problems_formatted[0][k] = re.sub('^    ', '', problems_formatted[0][k]) 

    # flatten list and join
    problem_lines = []
    for l in range(len(problems_formatted[0])):
        for m in range(len(problems_formatted)):
            problem_lines.append(problems_formatted[m][l])

    # remove answer if show_answers false
    if not show_answers:
        problem_lines = problem_lines[:-len(problems_formatted)]

    # remove last line break 
    problem_lines[-1] = re.sub('\n$', '', problem_lines[-1])

    return ''.join(problem_lines)

print(solve_problems(problems))

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
