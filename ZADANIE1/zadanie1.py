def dodaj_element(wejscie): 
    stack = [(wejscie, 1)] 

    lists_by_depth = {}
    max_found_depth = 0

    while stack:
        current_item, current_depth = stack.pop()

        if isinstance(current_item, list):
            if current_depth not in lists_by_depth:
                lists_by_depth[current_depth] = []
            lists_by_depth[current_depth].append(current_item)
            
            if current_depth > max_found_depth:
                max_found_depth = current_depth
            
            for sub_item in current_item:
                stack.append((sub_item, current_depth + 1))
        
        elif isinstance(current_item, tuple):
            for sub_item in current_item:
                stack.append((sub_item, current_depth + 1))
        
        elif isinstance(current_item, dict):
            for sub_item in current_item.values():
                stack.append((sub_item, current_depth + 1))
    
    if max_found_depth in lists_by_depth:
        deepest_lists = lists_by_depth[max_found_depth]
        
        for lst in deepest_lists:
            new_element = 1
            
            if lst:
                try:
                    last_element = lst[-1]
                    if isinstance(last_element, int):
                        new_element = last_element + 1
                except (TypeError, IndexError):
                    pass
            lst.append(new_element)

    return wejscie

if __name__ == '__main__':
    input_list = [
     1, 2, [3, 4, [5, {"klucz": [5, 6], "tekst": [1, 2]}], 5],
     "hello", 3, [4, 5], 5, (6, (1, [7, 8]))
    ]
    output_list = dodaj_element(input_list)
    print(input_list)   