from case_analysis import Chance

class Cycles:
        def calc_cycles(self, average_cycles = 4):
            best_cycles = int(average_cycles * Chance.best_case_chance)
            worst_cycles = int(average_cycles * Chance.worst_case_chance)
            cycle_data = [best_cycles, average_cycles, worst_cycles]
            return cycle_data
        def print_cycle(self):
            for x in range(len(Cycles.calc_cycles(self))):
                print('[Cycles]: ',Chance.words[x],str(Cycles.calc_cycles(Cycles)[x]),'Cycles')
