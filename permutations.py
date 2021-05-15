def permutations(items):
    if len(items)==0:
        yield ""
    elif len(items)==1:
        yield items
    else:
        for item in items:
            new_items = items.copy()
            new_items.remove(item)
            for permutation in permutations(new_items):
                yield [item]+permutation

for p in permutations(list('abcd')):
    print(p)