from collections import Counter


def frequency_count(string):
    output=Counter(string)
    result=""
    for key in sorted(output.keys()):
        result += f"{key}{output[key]}"
    return result

string="geeksforgeeks"
print(frequency_count(string))
