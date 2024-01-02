from game import game
import copy


def get_data(roles, vn):
    n, v_total, m_total = 0, 0, 0

    while n != 1000000:
        n += 1
        deep_roles = copy.deepcopy(roles)
        w = game(deep_roles)
        v_total += w[0]
        m_total += w[1]

    print(100*v_total/n)

    with open("results.txt", "a") as f:
        f.write(f"{vn}, {100*v_total/n}\n")

    return 100*v_total/n
