"""Documentation about the fairsharer module."""


def fair_sharer(values, num_iterations, share=0.1):
    for i in range(num_iterations):
        max_value = max(values)
        index_max = values.index(max_value)
        share_amount = max_value * share
        values[index_max] -= share_amount * 2
        values[index_max - 1] += share_amount
        values[(index_max + 1) % len(values)] += share_amount
    return values

