users = [1, 2, 3, 4, 5, 6, 7, 8, 9]
m = len(users)
movies = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
n = len(movies)


def brute_force(as_ranking, bs_ranking=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']):
    for i, rank in enumerate(bs_ranking):
        for j, renk in enumerate(bs_ranking):
            if i == j:
                continue
            else:
                if as_ranking[i] > as_ranking[j]:
                    pass
        # for j, rank enumerate(as_ranking):
        #     if i == j:
        #         continue
        #     else:
        #         if as_ranking[]
    pass


def divide_n_conquer(as_ranking, bs_ranking):
    pass
