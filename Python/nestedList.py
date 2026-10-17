def main():
    mixed_list = [1, [2, 3], 4, [5, 6], 7, [8]]
    flat_list = []

    for item in mixed_list:
        
        if isinstance(item,list):
            flat_list.extend(item)
        else:
            flat_list.append(item)

    print(flat_list)

main()