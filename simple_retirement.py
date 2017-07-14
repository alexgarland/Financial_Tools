def simple_retirement(avg_ror, years_until_retirement, contributions):
    total_saved = 0
    for i in range(0, years_until_retirement):
        total_saved += total_saved*(avg_ror) + contributions
        print(total_saved)
    return total_saved