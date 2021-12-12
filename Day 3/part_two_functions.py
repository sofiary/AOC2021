from collections import defaultdict

def find_most_common_bit(index: int, values: list, rating) -> str:
    total_values = len(values)
    values_of_1 = 0
    for value in values:
        if value[index] == '1':
            values_of_1 += 1
    if rating == 'o2':
        return '1' if values_of_1 / total_values >= 0.5 else '0'
    elif rating == 'co2':
        return '0' if values_of_1 / total_values >= 0.5 else '1'

def get_ratings(data: list) -> dict:
    # Prepare output dictionary
    ratings = defaultdict(lambda: None)
    # Prepare initial data
    o2_data = data.copy()
    co2_data = data.copy()

    for idx in range(len(data[0])):
        # Find relevant bit
        print(
            f"o2_data: {o2_data}, co2_data: {co2_data}, index {idx}"
        )
        
        # Filter by relevant bit
        if len(o2_data) > 1:
            o2_bit = find_most_common_bit(idx, o2_data, rating='o2')
            o2_data = [x for x in o2_data if x[idx] == o2_bit]
        if len(o2_data) == 1 and ratings["o2"] is None:
            ratings["o2"] = int(o2_data.pop(), 2)

        if len(co2_data) > 1:
            co2_bit = find_most_common_bit(idx, co2_data, rating='co2')
            co2_data = [x for x in co2_data if x[idx] == co2_bit]
        if len(co2_data) == 1 and ratings["co2"] is None:
            ratings["co2"] = int(co2_data.pop(), 2)

    ratings["life"] = ratings["o2"] * ratings["co2"]
    return ratings