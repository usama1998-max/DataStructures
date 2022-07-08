# for Testing
print("Huffman Codding")


def unique(string, return_list=False, return_dict=True):
    f = {}
    l = []

    for c in string:
        if c in f:
            f[c] += 1
        else:
            f[c] = 1
            l.append(c)

    if return_list is True:
        return l

    elif return_dict is True:
        return f

    else:
        return l, f

chars = "hello"

print(len(chars) * 3, "bits")




