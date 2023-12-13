import typing as t


str_to_int_dict = {'one' : '1','two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}


def get_all_substring(rand_str:str):
    substrings = []
    length = len(rand_str)
    for start in range(length):
        for end in range(start + 1, length + 1):
            substrings.append(rand_str[start:end])
    return substrings
    
def get_first_valid_substring(substrings: t.List[str]):
    for substr in substrings:
        if substr in str_to_int_dict.keys():
            return str_to_int_dict[substr]
        if substr in str_to_int_dict.values():
            return substr

def parse_str(rand_str: str) -> int:
    all_substrings = get_all_substring(rand_str=rand_str)
    first_int = get_first_valid_substring(substrings=all_substrings)
    last_int = get_first_valid_substring(substrings=all_substrings[::-1])
    return int(first_int + last_int)              
    
    
def get_file_input(file_path:str = "file_1.txt") -> t.List[str]:
    inputs = []
    with open(file_path, 'r') as f:
        for line in f:
            inputs.append(line.strip())
    return inputs

file_inputs = get_file_input()
ints = []
for rand_str in file_inputs:
    ints.append(parse_str(rand_str=rand_str))
    
print(sum(ints))
    
    
