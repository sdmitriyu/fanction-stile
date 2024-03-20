def kvadrat (nambers):
    return nambers ** 2

def nechyotn(nedva):
    return nedva % 2

my_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

result = filter(nechyotn, map(kvadrat, my_list))

print(list(result))