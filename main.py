msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msgs = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6,
        msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
opers = "+-*/"
memory = float()
calc_running = True


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7
    if ((v1 == 0 or v2 == 0)
            and (v3 == "*" or v3 == "+" or v3 == "-")):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    else:
        return False


while calc_running:
    print(msg_0)
    x, oper, y = [x for x in input().split()]

    try:
        y = memory if y == "M" else float(y)
        x = memory if x == "M" else float(x)

        if oper in opers:
            check(x, y, oper)
            if oper == '/' and y == 0:
                print(msg_3)
                continue
            elif oper == "+":
                result = x + y
                print(result)
            elif oper == "-":
                result = x - y
                print(result)
            elif oper == "*":
                result = x * y
                print(result)
            elif oper == "/":
                result = x / y
                print(result)
        else:
            print(msg_2)
            continue

    except Exception:
        print(msg_1)
        continue

    store_result = ""
    while store_result not in ["y", "n"]:
        print(msg_4)
        store_result = input()
        if store_result == "y":
            if is_one_digit(result):
                msg_index = 10
                while True:
                    print(msgs[msg_index])
                    answer = input()
                    if answer == "y":
                        msg_index += 1
                        if msg_index == 13:
                            memory = result
                            break
                    elif answer == "n":
                        break
                    else:
                        continue
            else:
                memory = result
    cont_calc = ""
    while cont_calc not in ["y", "n"]:
        print(msg_5)
        cont_calc = input()
        if cont_calc == "n":
            calc_running = False
