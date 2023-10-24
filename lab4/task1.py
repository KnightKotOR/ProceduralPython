import json


def task() -> float:
    filename = "input.json"
    with open(filename) as file:
        data = json.load(file)

    total_sum = sum([item["score"] * item["weight"] for item in data])
    return round(total_sum, 3)


print(task())
