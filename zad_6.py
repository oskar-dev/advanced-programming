def list_merge(a: list, b: list) -> list:
    out = []
    for element in a:
        out.append(element**3)
    for element in b:
        new_element = element**3
        if new_element in out:
            continue
        out.append(element)

    return out


print(list_merge([2, 5], [2, 1]))
