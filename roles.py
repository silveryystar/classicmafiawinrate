import random


def reg(roles):
    kill = ""
    random.shuffle(roles)

    if "reg" in roles:
        if "kcop" in roles:
            if "kdoc" in roles:
                kill = "kdoc"

            elif "doc" in roles:
                kill = roles[0]
                if kill == "reg" or kill == "kcop":
                    kill = roles[1]
                if kill == "reg" or kill == "kcop":
                    kill = roles[2]
                if kill == "reg" or kill == "kcop":
                    kill = roles[3]

            else:
                kill = "kcop"

        elif "kdoc" in roles:
            if len(roles) == 2:
                kill = "kdoc"

            else:
                kill = roles[0]
                if kill == "reg" or kill == "kdoc":
                    kill = roles[1]
                if kill == "reg" or kill == "kdoc":
                    kill = roles[2]
                if kill == "reg" or kill == "kdoc":
                    kill = roles[3]

        else:
            kill = roles[0]
            if kill == "reg":
                kill = roles[1]
            if kill == "reg":
                kill = roles[2]

    return kill


def cop(roles, cop_checks):
    check = ""
    random.shuffle(roles)

    if "cop" in roles or "kcop" in roles:
        temp_roles = [i for i in roles if i not in cop_checks]

        check = temp_roles[0]
        if check == "cop" or check == "kcop" or check == "kdoc":
            check = temp_roles[1]
        if check == "cop" or check == "kcop" or check == "kdoc":
            check = temp_roles[2]
        if check != "reg":
            cop_checks.append(check)

    return check, cop_checks


def doc(roles):
    save = ""

    if "doc" in roles or "kdoc" in roles:
        if "kcop" in roles:
            save = "kcop"

        elif "kdoc" in roles:
            save = "kdoc"

        else:
            save = "doc"

    return save
