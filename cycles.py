from settings import settings

class Cycles:
        def calc_cycles(self):
            best_cycles = int(settings.average_cycles * settings.best_case_chance)
            worst_cycles = int(settings.average_cycles * settings.worst_case_chance)
            cycle_data = [best_cycles, settings.average_cycles, worst_cycles]
            return cycle_data
        def print_cycle(self):
            for x in range(len(Cycles.calc_cycles(self))):
                print('[Cycles]: ',settings.words[x],str(Cycles.calc_cycles(Cycles)[x]),'Cycles')
