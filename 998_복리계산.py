total_years = 10 
future_value_20_years = 0
initial_monthly_investment = 2000000 # 시작 금액
investment_increase_per_year = 100000 # 연 증가 금액
annual_return_rate = 0.25  # 평균 연 이율 18.35% 
monthly_return_rate = annual_return_rate / 12


for year in range(total_years):
    monthly_investment = initial_monthly_investment + (investment_increase_per_year * year)
    for month in range(1, 13):
        future_value_20_years += monthly_investment * ((1 + monthly_return_rate) ** ((total_years - year) * 12 - month))


print(future_value_20_years)