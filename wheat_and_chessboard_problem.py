def format_number_grains(grains):
    grains_per_kg = 15430
    grains_per_tonne = 1000 * grains_per_kg
    grains_per_titanics = 52000 * grains_per_tonne
    grains_per_empire_state_building = 365000 * grains_per_tonne
    grains_per_hoover_damn = 6600000 * grains_per_tonne
    grains_per_coal_reserve = 150000000 * grains_per_tonne
    grains_per_global_production = 760000000 * grains_per_tonne

    if grains > grains_per_global_production:
        return f'{round(grains / grains_per_global_production)} x global wheet production for 2020'
    elif grains > grains_per_coal_reserve:
        return f'{round(grains / grains_per_coal_reserve)} Chineese coal reserves for 2016'
    elif grains > grains_per_hoover_damn:
        return f'{round(grains / grains_per_hoover_damn)} hoover dams'
    elif grains > grains_per_empire_state_building:
        return f'{round(grains / grains_per_empire_state_building, 2)} empire state buildings'
    elif grains > grains_per_titanics:
        return f'{round(grains / grains_per_titanics, 2)} titanics'
    elif grains > grains_per_tonne:
        return f'{round(grains / grains_per_tonne, 2)} tonnes'
    else:
        return f'{round(grains / grains_per_kg, 4)} kg'


def main():
    max_squares = 64
    current_grains = 0

    for current_square in range(max_squares):
        current_grains += (2 ** current_square)
        print(f'{current_grains} grains, weighing:', format_number_grains(current_grains))


if __name__ == '__main__':
    main()
