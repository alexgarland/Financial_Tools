def simple_retirement(avg_ror, years_until_retirement, contributions):
    total_saved = 0
    for i in range(0, years_until_retirement):
        total_saved += total_saved*(avg_ror) + contributions
    return total_saved

def simple_retirement_age(ror_eq, ror_bonds, years, contributions):
	 total_saved = 0
	 retirement_age = 67
	 current_age = 67 - years
	 for i in range(0, years):
	    current_stock_allocation = (120.0 - current_age-i) / 100.0
	    print(current_stock_allocation)
	    avg_ror = current_stock_allocation * ror_eq + (1-current_stock_allocation) * ror_bonds
	    total_saved += total_saved*(avg_ror) + contributions
	    print(total_saved)
	 return total_saved