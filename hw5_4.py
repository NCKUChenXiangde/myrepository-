#統計系116陳祥德H24124068
def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except SyntaxError:
        return "Error: Unsupported character or syntax"
    except TypeError:
        return "Error: Operand error"
    except ValueError:
        return "Error: Operand error"


def check_parentheses(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


def main():
    while True:
        expression = input("Enter an arithmetic expression (or 'q' to quit): ")
        if expression.lower() == 'q':
            break

        if not all(char.isdigit() or char in '+-*/() ' for char in expression):
            print("Error: Unsupported character error")
            continue

        if not check_parentheses(expression):
            print("Error: Unbalanced parentheses error")
            continue

        result = evaluate_expression(expression)
        if isinstance(result, str):
            print(result)
        else:
            print("Result:", result)


if __name__ == "__main__":
    main()
