from profit_p_Y import profit_per_year
from cycles import Cycles
from turnover_p_Y import turnover_per_year
from yield_p_Y import yield_per_year
from yield_p_P import Yield
from tkinter import Tk,Label,Frame, Text,Button
from settings import settings
class gGUI:
    # declare the window
    window = Tk()
    # set window title
    window.title(settings.NAME)
    # set window width and height
    window.configure(width=settings.WIDTH, height=settings.HEIGHT)
    # set window background color
    window.configure(bg='white')
    frm = Frame(window)
    frm.grid()
    #Collum
    col = 0
    #Row
    rrow = 0
    #Label Array
    label_list = []
    label_cnt = 0
    def center_gui(self,window):
        # move window center
        window.geometry(self.WID_HEI_str)
        winWidth = window.winfo_reqwidth()
        winwHeight = window.winfo_reqheight()
        posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
        posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
        window.geometry("+{}+{}".format(posRight, posDown))

    def create_label(self, label):
        self.frm = Frame(self.window)
        self.frm.grid()
        lbl = Label(self.frm, text=label).grid(column=self.col, row=self.rrow)
        self.label_list.append(lbl)
#        self.col = self.col + 1
        self.rrow = self.rrow + 1
        #print("Row:", self.rrow)
        #self.label_list[0] = Label(self.frm, text="test").grid(column=self.col, row=self.rrow)
        self.label_cnt = self.label_cnt + 1
        print("label_cnt:", self.label_cnt)
        #for i in self.label_list:
         #   print("List", self.label_list[i])
        self.change_label(self, self.label_list[0])
        return lbl

    def change_label(self, label):
        label = Label(self.frm, text="test").grid(column=self.col, row=self.rrow)

    def gui(self):
        self.create_label(self, settings.best_case+ settings.ppy + str(profit_per_year.calc_p_p_y(profit_per_year)[0] / 1000000) + settings.mio_euro)
        #l1 = Label(self.frm, text=settings.best_case+ settings.ppy + str(profit_per_year.calc_p_p_y(profit_per_year)[0] / 1000000) + settings.mio_euro).grid(column=0, row=0)
        self.create_label(self, settings.average_case + settings.ppy + str(profit_per_year.calc_p_p_y(profit_per_year)[1] / 1000000) + settings.mio_euro)
        # l2 = Label(self.frm, text=settings.average_case + settings.ppy + str(profit_per_year.calc_p_p_y(profit_per_year)[1] / 1000000) + settings.mio_euro).grid(column=0, row=1)
        self.create_label(self, settings.worst_case + settings.ppy + str(profit_per_year.calc_p_p_y(profit_per_year)[2] / 1000000) + settings.mio_euro)
        #l3 = Label(self.frm, text=settings.worst_case + settings.ppy + str(profit_per_year.calc_p_p_y(profit_per_year)[2] / 1000000) + settings.mio_euro).grid(column=0, row=2)
        self.create_label(self, settings.best_case + settings.tpy + str(turnover_per_year.calc_t_p_y(profit_per_year)[0] / 1000000) + settings.mio_euro)
        #l4 = Label(self.frm,  text=settings.best_case + settings.tpy + str(turnover_per_year.calc_t_p_y(profit_per_year)[0] / 1000000) + settings.mio_euro).grid(column=0, row=3)
        self.create_label(self, settings.average_case + settings.tpy + str(turnover_per_year.calc_t_p_y(profit_per_year)[1] / 1000000) + settings.mio_euro)
        #l5 = Label(self.frm,  text=settings.average_case + settings.tpy + str(turnover_per_year.calc_t_p_y(profit_per_year)[1] / 1000000) + settings.mio_euro).grid(column=0, row=4)
        self.create_label(self, settings.worst_case + settings.tpy + str(turnover_per_year.calc_t_p_y(profit_per_year)[2] / 1000000) + settings.mio_euro)
        #l6 = Label(self.frm,  text=settings.worst_case + settings.tpy + str(turnover_per_year.calc_t_p_y(profit_per_year)[2] / 1000000) + settings.mio_euro).grid(column=0, row=5)
        self.create_label(self, settings.best_case + settings.cpy + str(Cycles.calc_cycles(Cycles)[0]) + settings.cyc)
       # l7 = Label(self.frm,  text=settings.best_case + settings.cpy + str(Cycles.calc_cycles(Cycles)[0]) + settings.cyc).grid(column=0, row=6)
        self.create_label(self, settings.average_case + settings.cpy + str(Cycles.calc_cycles(Cycles)[1]) + settings.cyc)
        #l8 = Label(self.frm,  text=settings.average_case + settings.cpy + str(Cycles.calc_cycles(Cycles)[1]) + settings.cyc).grid(column=0, row=7)
        self.create_label(self, settings.worst_case + settings.cpy + str(Cycles.calc_cycles(Cycles)[2]) + settings.cyc)
        #l9 = Label(self.frm,  text=settings.worst_case + settings.cpy + str(Cycles.calc_cycles(Cycles)[2]) + settings.cyc).grid(column=0, row=8)

        self.create_label(self, settings.best_case + settings.ypy + str(yield_per_year.calc_y_p_y(yield_per_year)[0] / 1000000) + settings.tn)
        #l10 = Label(self.frm, text=settings.best_case + settings.ypy + str(yield_per_year.calc_y_p_y(yield_per_year)[0] / 1000000) + settings.tn).grid(column=0, row=9)
        self.create_label(self, settings.average_case + settings.ypy + str(yield_per_year.calc_y_p_y(yield_per_year)[1] / 1000000) + settings.tn)
        #l11 = Label(self.frm, text=settings.average_case + settings.ypy + str(yield_per_year.calc_y_p_y(yield_per_year)[1] / 1000000) + settings.tn).grid(column=0, row=10)
        self.create_label(self, settings.worst_case + settings.ypy + str(yield_per_year.calc_y_p_y(yield_per_year)[2] / 1000000) + settings.tn)
        #l12 = Label(self.frm, text=settings.worst_case + settings.ypy + str(yield_per_year.calc_y_p_y(yield_per_year)[2] / 1000000) + settings.tn).grid(column=0, row=11)

        self.create_label(self, settings.best_case + settings.ypp + str(Yield.calc_yield(Yield)[0]) + 'g')
        #l13 = Label(self.frm, text=settings.best_case + settings.ypp + str(Yield.calc_yield(Yield)[0]) + 'g').grid(column=0, row=12)
        self.create_label(self, settings.average_case + settings.ypp + str(Yield.calc_yield(Yield)[1]) + 'g')
        #l14 = Label(self.frm, text=settings.average_case + settings.ypp + str(Yield.calc_yield(Yield)[1]) + 'g').grid(column=0, row=13)
        self.create_label(self, settings.worst_case + settings.ypp + str(Yield.calc_yield(Yield)[2]) + 'g')
        #l15 = Label(self.frm, text=settings.worst_case + settings.ypp + str(Yield.calc_yield(Yield)[2]) + 'g').grid(column=0, row=14)

        #self.center_gui(self.window)
        self.window.mainloop()
    #End Window
