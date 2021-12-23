from typing import Optional

from fastapi import FastAPI

app = FastAPI()


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


@app.get("/calc")
def calculator():
	request_data = request.get_json()
	expressions = request_data['expressions']
	output_list = []
	for exp in expressions:
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
	return {"evaluated_result" : output_list}


