def find_free_tables(tables: dict):
    free_tables = []
    for key in tables:
        if tables[key] == 0:
            free_tables.append(key)
    return free_tables


if __name__ == "__main__":
    vip_tables = {
        10: 1,
        20: 1,
        30: 1,
        40: 1,
        50: 1
    }

    common_tables = {
        60: 1,
        70: 0,
        80: 1,
        90: 0,
        100: 1,
        110: 1,
        120: 0
    }

    if len(find_free_tables(vip_tables)) == 0:
        print("No VIP tables available.")
    else:
        print(f'Free VIP tables: {find_free_tables(vip_tables)}\n')

    if len(find_free_tables(common_tables)) == 0:
        print("No common tables available.")
    else:
        print(f'Free VIP tables: {find_free_tables(common_tables)}\n')
