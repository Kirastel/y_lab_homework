import random
import math

points = [(0, 1), (1, 4), (4, 1), (5, 5), (7, 2)]
number_of_options = math.factorial(len(points) - 1)


def distance_calculate(point_1, point_2) -> float:
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5


def get_variant(original_list: list) -> list:
    variant = [original_list[0]]
    original_list = original_list[1:]
    random.shuffle(original_list)
    variant.extend(original_list)
    variant.append(variant[0])
    return variant


def get_variants_array() -> list:
    variants_array = []
    while True:
        variant = get_variant(points)
        if variant in variants_array:
            continue
        else:
            variants_array.append(variant)
        if len(variants_array) == number_of_options:
            break
    return variants_array


def get_list_distances(points: list) -> list:
    return [distance_calculate(p1, p2) for p1, p2 in zip(points[:-1], points[1:])]


def get_route(variants: list) -> str:
    data_of_ways = {}
    for variant in variants:
        distances_list = get_list_distances(variant)
        data_of_ways[sum(distances_list)] = (variant, distances_list)

    min_route = data_of_ways.get(min(data_of_ways.keys()))

    variant = min_route[0]
    distances = min_route[1]

    result = f'{variant[0]}'
    total = 0
    for i in range(1, len(variant)):
        total += distances[i - 1]
        result += f' -> {variant[i]}[{total}]'
    result += f' = {total}'
    return result


if __name__ == '__main__':
    variants = get_variants_array()
    route = get_route(variants)
    print(route)


