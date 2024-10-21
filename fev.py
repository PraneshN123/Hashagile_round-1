def find_first_non_repeating_char(s: str) -> str:

    count_map = {}

    for char in s:
        if char in count_map:
            count_map[char] += 1
        else:
            count_map[char] = 1

   
    for char in s:
        if count_map[char] == 1:
            return char

 
    return None


s = "swiss"
result = find_first_non_repeating_char(s)
print(f"The first non-repeating character is: {result}")
