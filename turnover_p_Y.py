from yield_p_Y import yield_per_year
from case_analysis import Chance
import numpy as np

class turnover_per_year:
    def calc_t_p_y(self, price_p_g = 6):
        ypy = np.array(yield_per_year.calc_y_p_y(yield_per_year))
        best_price = float(price_p_g * Chance.best_case_chance)
        worst_price = float(price_p_g * Chance.worst_case_chance)
        price_data = [best_price, price_p_g, worst_price]
        pda = np.array(price_data)
        turnover = (ypy * pda) 
        return turnover
    def print_t_p_y(self):
            for x in range(len(turnover_per_year.calc_t_p_y(self))):
                print('[Turnover per Year]: ',Chance.words[x],str(turnover_per_year.calc_t_p_y(self)[x]/ 1000000),'Million Euro')

    