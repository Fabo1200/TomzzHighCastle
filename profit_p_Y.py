from turnover_p_Y import turnover_per_year
from case_analysis import Chance
import numpy as np

class profit_per_year:
    def calc_p_p_y(self, cost_p_warehouse = 1500000, number_of_warehouses = 4):
        turnover = np.array(turnover_per_year.calc_t_p_y(turnover_per_year))
        profit =  turnover - (cost_p_warehouse * number_of_warehouses)
        return profit
    def print_p_p_y(self):
        for x in range(len(profit_per_year.calc_p_p_y(self))):
            print('[Profit per Year]: ',Chance.words[x],str(profit_per_year.calc_p_p_y(self)[x] / 1000000),'Million Euro')

                    