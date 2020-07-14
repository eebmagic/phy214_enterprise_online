
def change_in_joules(mass, specefic_heat, temp_change):
    return mass * specefic_heat * temp_change


def work(pressure, vol_change):
    return pressure * vol_change


def work(pressure, vol_initial, vol_final):
    return pressure * (vol_final - vol_initial)


if __name__ == "__main__": 
    print(change_in_joules(80, 4186, 2))
