def arithmetic_arranger(problems, print_answer = False):
  number_of_problems = len(problems)
  first_nums = []
  opers = []
  second_nums = []
  all_digits = True
  all_simple_oper = True
  correct_digit_length = True
  ans_nums = []

  if number_of_problems > 5:
    error = "Error: Too many problems."
    return error

  for problem in problems:
    xx = problem.split()
    if (not xx[0].isdigit()) or (not xx[2].isdigit()):
      all_digits = False
      break
    if (len(xx[0]) > 4) or (len(xx[2]) > 4):
      correct_digit_length = False
      break
    first_nums.append(xx[0])
    second_nums.append(xx[2])
    if (not xx[1] == '+') and (not xx[1] == '-'):
      all_simple_oper = False
      break
    opers.append(xx[1])

    ans = str(eval(problem))
    ans_nums.append(ans)


  if not all_simple_oper:
    error = "Error: Operator must be \'+\' or \'-\'."
    return error
  if not all_digits:
    error = "Error: Numbers must only contain digits."
    return error
  if not correct_digit_length:
    error = "Error: Numbers cannot be more than four digits."
    return error


  first_rows = []
  second_rows = []
  dash_rows = []
  ans_rows = []

  for (oper, second_num, first_num, ans_num) in zip(opers, second_nums, first_nums, ans_nums):

    if len(first_num)>len(second_num):
      dash_row = "-" * (len(first_num)+2)
      first_row = f"  {first_num}"
      second_row = f"{oper}" + (" " * (len(first_row) - len(second_num) - 1)) + f"{second_num}"
      ans_row = (" " * (len(first_row) - len(ans_num))) + f"{ans_num}"


    else:
      second_row = f"{oper} {second_num}"
      dash_row = "-" * len(second_row)
      first_row = (" " * (len(second_row) - len(first_num))) + first_num
      ans_row = (" " * (len(second_row) - len(ans_num))) + f"{ans_num}"


    first_rows.append(first_row)
    second_rows.append(second_row)
    dash_rows.append(dash_row)
    ans_rows.append(ans_row)

  line_one = "    ".join(first_rows).rstrip()
  line_two = "    ".join(second_rows).rstrip()
  line_three = "    ".join(dash_rows).rstrip()
  line_four = "    ".join(ans_rows).rstrip()

  if print_answer:
    arranged_problems = f"{line_one}\n{line_two}\n{line_three}\n{line_four}"
  else:
    arranged_problems = f"{line_one}\n{line_two}\n{line_three}"


  return arranged_problems