

def check_string_length(string):
    if len(string) > 2048:
        string_list = [string[i:i+2048] for i in range(0, len(string), 2048)]
        return string_list
    else:
        return string