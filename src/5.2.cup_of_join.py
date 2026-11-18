""" Module to join an unlimited amount of lists,
    separating them with '-' or a different given separator.
"""

def cup_of_join(*lists: list, sep: object = "-") -> list | None:
    """Join any number of lists into one list, separated by sep."""
    if not lists:
        return None

    result = []
    for current_list in lists:
        result.extend(current_list)
        result.append(sep)

    result.pop()  # to remove the last sep
    return result


def main() -> None:
    """Read lists from user input until an empty line, then print joined result."""
    user_lists: list[list[str]] = []

    while True:
        line = input("Enter list items (empty list to finish): ").strip()
        if not line:
            break
        user_lists.append(line.split())

    sep_input = input("Enter separator (leave empty for '-'): ").strip()
    if sep_input:
        print(cup_of_join(*user_lists, sep=sep_input))
    else:
        print(cup_of_join(*user_lists))

if __name__ == "__main__":
    main()