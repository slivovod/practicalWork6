elements = list(input().split(", "))

def get_unique_elements(elements):
    unique = []

    for item in elements:
        if item in unique:
            continue
        else:
            unique.append(item)
    return unique
unique_sorted_list = sorted(get_unique_elements(elements))
print(unique_sorted_list)