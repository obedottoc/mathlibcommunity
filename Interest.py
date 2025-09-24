class Interest:

    @staticmethod
    def SI(principal:float, rate:float, years:float):
        if principal < 0 or rate < 0 or years < 0:
            raise ValueError("Principal, rate, and years must be non-negative.")
        return principal * (1 + rate * years)
    
    @staticmethod
    def CI(principal:float, rate:float, times_compounded:int, years:float):
        if principal < 0 or rate < 0 or times_compounded <= 0 or years < 0:
            raise ValueError("Principal, rate, times compounded, and years must be non-negative, with times compounded positive.")
        return principal * (1 + rate / times_compounded) ** (times_compounded * years)

    @staticmethod
    def empirical_rate(nominal_rate:float, compounding_periods:int):
        if compounding_periods <= 0:
            raise ValueError("Compounding periods must be positive.")
        return (1 + nominal_rate / compounding_periods) ** compounding_periods - 1
        
    @staticmethod
    def cagr(beginning_value: float, ending_value: float, num_years: int):
        if beginning_value <= 0 or num_years <= 0:
            raise ValueError("Beginning value and number of years must be positive.")
        return (ending_value / beginning_value) ** (1 / num_years) - 1
    
    @staticmethod
    def apr(periodic_rate:float, periods_per_year:int):
        if periods_per_year <= 0:
            raise ValueError("Periods per year must be positive.")
        return periodic_rate * periods_per_year
    
    @staticmethod
    def eir(apr:float, periods_per_year:int):
        if periods_per_year <= 0:
            raise ValueError("Periods per year must be positive.")
        return (1 + apr / periods_per_year) ** periods_per_year - 1
