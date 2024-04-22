def check_gay_percent(name):
    total = 0
    for i, char in enumerate(name, start=1):
        char_value = ord(char.lower()) - ord('a') + 1
        total += char_value * i
    percent_gay = total % 100
    return percent_gay

