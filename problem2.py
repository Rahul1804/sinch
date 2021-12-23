# Create a program that evaluates arithmetic expressions written in Polish notation. Expressions can contain double-precision floating point numbers and the
# following operations: addition, subtraction, division and multiplication.

# + + 0.5 1.5 * 4 10
# - 2e3 - 700 + 7 * 2 15
# - -1.5 * 3.1415 / -7 -2
# 100500
# 1 2
# + 1

# 42.00
# 1337.00
# -12.50
# 100500.00
# error
# error

import sys
from collections import deque

def eval_arithmetic_exp(tokens):

	token=tokens.popleft()
	if token=='+':
		return eval_arithmetic_exp(tokens)+eval_arithmetic_exp(tokens)
	elif token=='-':
		return eval_arithmetic_exp(tokens)-eval_arithmetic_exp(tokens)
	elif token=='*':
		return eval_arithmetic_exp(tokens)*eval_arithmetic_exp(tokens)
	elif token=='/':
		return eval_arithmetic_exp(tokens)/eval_arithmetic_exp(tokens)
	else:
		return float(token)


def main():
	stdin_list = sys.stdin.readlines()
	input_list = []
	for item in stdin_list:
		val = item.strip()
		if val:
			input_list.append(val)

	output_list = []

	for exp in input_list:
		try:
			tokens = deque(exp.split())
			exp_output = eval_arithmetic_exp(tokens)
			if len(tokens) > 0:
				raise Exception('Invalid Expression')
			formated_out = format(exp_output, '.2f')
			output_list.append(formated_out)
		except:
			output_list.append('error')
			continue

	print('---- output ----')
	for item in output_list:
		print(item)


if __name__=='__main__':
	main()


