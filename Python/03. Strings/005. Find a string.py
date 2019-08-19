def count_substring(string, sub_string):
    return len([string[i:len(sub_string) + i] for i, char in enumerate(string) if string[i:len(sub_string) + i] == sub_string])
