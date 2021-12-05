from case_analysis import Chance

class Yield:
        def calc_yield(self, average_yield = 100):         
            best_yield = int(average_yield * Chance.best_case_chance)
            worst_yield = int(average_yield * Chance.worst_case_chance)
            yield_data = [best_yield, average_yield, worst_yield]
            return yield_data
        
        def print_yield(self):   
            for x in range(len(Yield.calc_yield(Yield))):
                print('[Yield]: ',Chance.words[x],str(Yield.calc_yield(Yield)[x]),'g')