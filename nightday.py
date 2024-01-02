import random
from roles import reg, cop, doc


def night(roles, cop_checks):
    print(f"night roles: {roles}")

    kill = reg(roles)
    check, cop_checks = cop(roles, cop_checks)
    save = doc(roles)

    print(f"kill: {kill}")
    print(f"check: {check}")
    print(f"save: {save}")
    print("---")

    if kill == save:
        if "kdoc" not in roles:
            roles.remove("doc")
            roles.append("kdoc")

        if "doc" in cop_checks:
            cop_checks.remove("doc")
            cop_checks.append("kdoc")

        if "kdoc" not in cop_checks:
            cop_checks.append("kdoc")

    else:
        roles.remove(kill)

    return roles, check, cop_checks


def day(roles, check, cop_checks, n):
    print(f"day roles: {roles}")
    print("---")

    random.shuffle(roles)

    total_maf = [i for i in roles if i == "reg"]
    total_vil = [i for i in roles if i != "reg"]

    if len(total_maf) == len(total_vil):
        roles.pop()

    elif "cop" in roles:
        if check == "reg":
            roles.remove("reg")

            roles.remove("cop")
            roles.append("kcop")

        else:
            if n == 1:
                if "kdoc" in roles:
                    roles.remove("kdoc")
                    roles.pop()
                    roles.append("kdoc")

                else:
                    roles.pop()

    elif "kcop" in roles:
        if check == "reg":
            roles.remove("reg")

        else:
            if n == 1:
                temp_roles = []
                for i in cop_checks:
                    if i in roles:
                        temp_roles.append(i)
                        roles.remove(i)
                roles.pop()

                for i in temp_roles:
                    roles.append(i)

    elif "kdoc" in roles:
        if n == 1:
            roles.remove("kdoc")
            roles.pop()
            roles.append("kdoc")

    else:
        if n == 1:
            roles.pop()

    return roles
