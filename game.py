from nightday import night, day


def game(roles):
    cop_checks = ["cop", "kcop"]

    roles, check, cop_checks = night(roles, cop_checks)
    wins = check_win(roles)

    if wins == [0, 0]:
        roles = day(roles, check, cop_checks, 0)
        wins = check_win(roles)

        while wins == [0, 0]:
            roles, check, cop_checks = night(roles, cop_checks)
            wins = check_win(roles)

            if wins == [0, 0]:
                roles = day(roles, check, cop_checks, 1)
                wins = check_win(roles)

    print(f"final roles: {roles}")
    print(f"wins: {wins}")

    return wins


def check_win(roles):
    village_win, mafia_win = 0, 0

    if "reg" not in roles:
        village_win = 1

    else:
        m_total, v_total = 0, 0
        for i in roles:
            if i == "reg":
                m_total += 1
            else:
                v_total += 1
        if m_total > v_total:
            mafia_win = 1

    return [village_win, mafia_win]
