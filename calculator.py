from flask import Flask, render_template, request

Flask_App = Flask(__name__) # Creating our Flask Instance

@Flask_App.route('/', methods=['GET'])
def index():
    """ Displays the index page accessible at '/' """

    return render_template('index.html')

@Flask_App.route('/calculator/', methods=['POST'])
def calculator_operations():
    """Route where we send calculator form input"""

    error = None
    result = None

    # request.form looks for:
    # html tags with matching "name= "
    first_input = request.form['Input1']  
    second_input = request.form['Input2']
    operation = request.form['operation']

    try:
        input1 = float(first_input)
        input2 = float(second_input)

        # On default, the operation on webpage is addition
        if operation == "+":
            result = input1 + input2

        elif operation == "-":
            result = input1 - input2

        elif operation == "/":
            result = input1 / input2 

        elif operation == "*":
            result = input1 * input2

        else:
            operation = "%"
            result = input1 % input2

        # return render_template(
        #     'index.html',
        #     input1=input1,
        #     input2=input2,
        #     operation=operation,
        #     result=result,
        #     calculation_success=True
        # )

        return {
            "status": "Success",
            "result": result,
            "message": "None",
            "inputs": [input1, input2],
            "operation": operation
        }
        
    except ZeroDivisionError:
        # return render_template(
        #     'index.html',
        #     input1=input1,
        #     input2=input2,
        #     operation=operation,
        #     result="Bad Input",
        #     calculation_success=False,
        #     error="You cannot divide by zero"
        # )

        return {
            "status": "Failed",
            "result": "Bad Input",
            "message": "You cannot divide by zero",
            "inputs": [first_input, second_input],
            "operation": operation
        }
        
    except ValueError:
        # return render_template(
        #     'index.html',
        #     input1=first_input,
        #     input2=second_input,
        #     operation=operation,
        #     result="Bad Input",
        #     calculation_success=False,
        #     error="Cannot perform numeric operations with provided input"
        # )

        return {
            "status": "Failed",
            "result": "Bad Input",
            "message": "Cannot perform numeric operations with provided input",
            "inputs": [first_input, second_input],
            "operation": operation
        }

if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run(host='0.0.0.0')
