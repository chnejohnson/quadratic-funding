contrib_dict = {'4': {'1': 10.0, '2': 15.0, '3': 7.0, '5': 15.0, '4': 10.0}, '5': {
    '1': 15.0, '2': 25.0, '3': 3.0, '8': 2.0, '9': 10.0, '7': 7.0}}

tot_overlap = {}

# start pairwise match
for _, contribz in contrib_dict.items():
    for k1, v1 in contribz.items():
        if k1 not in tot_overlap:
            tot_overlap[k1] = {}

        # pairwise matches to current round
        for k2, v2 in contribz.items():
            if k2 not in tot_overlap[k1]:
                tot_overlap[k1][k2] = 0
                print("hello")
            print(tot_overlap[k1][k2])
            tot_overlap[k1][k2] += (v1 * v2) ** 0.5

            print(v1, v2)
            print(tot_overlap[k1][k2])
