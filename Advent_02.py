

def calculate_sublevel_distances(sublevel):
    is_safe_report = True
    for i in range(len(sublevel)-1):
        difference = abs(sublevel[i] - sublevel[i+1])
        if difference < 1 or difference > 3:
            is_safe_report = False
            break
    return is_safe_report


def calculate_level_distances(level):
    is_safe_report = True
    distances_between_levels = []
    bad_level_count = 0
    for i in range(len(level)-1):
        difference = abs(level[i] - level[i+1])
        if difference < 1 or difference > 3:
            #is_safe_report = False
            bad_level_count += 1
            #break
        distances_between_levels.append(difference)
    if bad_level_count > 1:
        is_safe_report = False
    elif bad_level_count == 0:
        pass
    else:
        pointer = 0
        level_copy = level.copy()
        verify_validation = False
        while pointer < len(distances_between_levels) or not verify_validation:
            if distances_between_levels[pointer] == 0 or distances_between_levels[pointer] > 3:
                level_copy.pop(pointer)
                verify_validation = calculate_sublevel_distances(level_copy)
                if not verify_validation:
                    level_copy = level.copy()
                    level_copy.pop(pointer + 1)
                    verify_validation = calculate_sublevel_distances(level_copy)
            pointer += 1
        if not verify_validation:
            is_safe_report = False
    return is_safe_report


def main():
    data = get_data()
    count_safe_levels = 0
    for i in range(len(data)):
        # Check first condition (whether is increasing or decreasing)
        if max(data[i]) == data[i][0]:
            ordered_list = sorted(data[i], reverse=True)
        elif min(data[i]) == data[i][0]:
            ordered_list = sorted(data[i])
        first_condition_check = data[i] == ordered_list
        # Check for second condition (distance between levels)
        if first_condition_check:
            is_level_safe = calculate_level_distances(data[i])
            if is_level_safe:
                count_safe_levels = count_safe_levels + 1
    print(count_safe_levels)


def get_data():
    file_path = "day_2.txt"
    data = []
    test_data = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9]
    ]

    with open(file_path, "r") as file:
        for line in file:
            level = list(map(int, line.split()))
            data.append(level)

    return data


if __name__ == "__main__":
    main()

