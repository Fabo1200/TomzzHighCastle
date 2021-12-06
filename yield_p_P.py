from case_analysis import Chance
from settings import settings

class Yield:
        def calc_yield(self):         
            best_yield = int(settings.average_yield * Chance.best_case_chance)
            worst_yield = int(settings.average_yield * Chance.worst_case_chance)
            yield_data = [best_yield, settings.average_yield, worst_yield]
            return yield_data
        
        def print_yield(self):   
            for x in range(len(Yield.calc_yield(Yield))):
                print('[Yield]: ',settings.words[x],str(Yield.calc_yield(Yield)[x]),'g')