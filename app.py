from flask import Flask
from flask import request
from flask import jsonify
from collections import deque

app = Flask(__name__)
@app.route('/calc')
def calculator():
    request_data = request.get_json()
    expressions = request_data['expressions']
    app.logger.info('The input expressions list is : ', expressions)
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

    return jsonify({"evaluated_result": output_list}), 200


def eval_arithmetic_exp(tokens):
    token = tokens.popleft()
    if token == '+':
        return eval_arithmetic_exp(tokens)+eval_arithmetic_exp(tokens)
    elif token == '-':
        return eval_arithmetic_exp(tokens)-eval_arithmetic_exp(tokens)
    elif token == '*':
        return eval_arithmetic_exp(tokens)*eval_arithmetic_exp(tokens)
    elif token == '/':
        return eval_arithmetic_exp(tokens)/eval_arithmetic_exp(tokens)
    else:
        return float(token)


# if __name__ == '__main__':
#     # run app in debug mode on port 5000
#     app.run(debug=True, port=5000)
