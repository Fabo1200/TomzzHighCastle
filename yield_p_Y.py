from cycles import Cycles
from yield_p_P import Yield
from case_analysis import Chance
import numpy as np
from settings import settings

class yield_per_year:
    def calc_y_p_y(self, number_of_plants = 3000, number_of_warehouses = 1):
        yld = np.array(Yield.calc_yield(Yield))
        cyc = np.array(Cycles.calc_cycles(Cycles))
        yield_p_y = ((yld * cyc) * (number_of_plants * number_of_warehouses))
        return yield_p_y
    def print_y_p_y(self):
            for x in range(len(yield_per_year.calc_y_p_y(self))):
                print('[Yield per Year]: ',settings.words[x],str(yield_per_year.calc_y_p_y(self)[x] / 1000000),'tons')

    