from cycles import Cycles
from yield_p_P import Yield
from yield_p_Y import yield_per_year
from turnover_p_Y import turnover_per_year
from profit_p_Y import profit_per_year

class Plant:  
    def print_data(self):
        Yield.print_yield(Yield) # print Yield per Plant
        Cycles.print_cycle(Cycles) #print Cycles per Plant
        yield_per_year.print_y_p_y(yield_per_year) #print Yield per Year 
        turnover_per_year.print_t_p_y(turnover_per_year) #print Turnover per Year
        profit_per_year.print_p_p_y(profit_per_year) #print Profit per Year

    