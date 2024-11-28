import sys


def read_kv_array(text):
    """Reads input key-value pairs from stdin and returns them as a list of dictionaries."""
    key_values = []

    for line in text:
        # Strip whitespace and split the line into key and value
        line = line.strip()
        key, value = line.split('\t')
        key_values.append({'key': key, 'value': value})

    return key_values


def write_kv_dict(key_values):
    """Writes key-value pairs to stdout in the required format."""
    for k, v in key_values.items():
        print(f'{k}\t{v}')


def word_count(words):
    """Counts the occurrences of each key and finds the most frequent one."""
    key_values = {}

    for w in words:
        # Aggregate counts
        key_values[w['key']] = key_values.get(w['key'], 0) + int(w['value'])

    # Find the word with the maximum frequency
    max_key = max(key_values, key=key_values.get)  # Get the key with the maximum value
    max_value = key_values[max_key]  # Get the maximum value

    # Return the most frequent word and its count as a dictionary
    return {max_key: max_value}


if __name__ == '__main__':
    # Read input from stdin, process it, and write the result to stdout
    write_kv_dict(word_count(read_kv_array(sys.stdin)))
