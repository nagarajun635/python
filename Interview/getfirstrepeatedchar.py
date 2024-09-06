def get_first_repeated_char(input_string):
    have_seen = {}
    for ch in input_string:
        if ch in have_seen:
            return ch
        else:
            have_seen[ch] = True
    return None

input_string = 'HELLO'
first_repeat = get_first_repeated_char(input_string)
print(first_repeat)