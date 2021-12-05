from profit_p_Y import profit_per_year
from cycles import Cycles
from turnover_p_Y import turnover_per_year
from yield_p_Y import yield_per_year
from yield_p_P import Yield
from tkinter import Tk,Label,Frame

class gGUI:
    NAME = 'TomzzHighCastle(THC)'
    WIDTH=1000 
    HEIGHT=800
    WID_HEI_str = str(WIDTH)  + 'x' + str(HEIGHT)
    best_case = "[Best Case] "
    average_case = "[Average Case] "
    worst_case = "[Worst Case] "
    mio_euro = " Million Euro"
    cyc = " Cycles"
    tn = " tons"
    ppy = "Profit per Year: "
    tpy = "Turnover per Year: "
    cpy = "Cycles per Year: "
    ypy = "Yield per Year: "
    ypp = "Yield per Plant: "
    #Window
    def center_gui(self,window):
        # move window center
        window.geometry(self.WID_HEI_str)
        winWidth = window.winfo_reqwidth()
        winwHeight = window.winfo_reqheight()
        posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
        posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
        window.geometry("+{}+{}".format(posRight, posDown))

    def gui(self):
        # declare the window
        window = Tk()
        # set window title
        window.title(self.NAME)
        # set window width and height
        window.configure(width=self.WIDTH,height=self.HEIGHT)
        # set window background color
        window.configure(bg='white')
        frm = Frame(window)
        frm.grid()
        l1 = Label(frm, text=self.best_case+ self.ppy + str(profit_per_year.calc_p_p_y(profit_per_year)[0] / 1000000) + self.mio_euro).grid(column=0, row=0)
        l2 = Label(frm, text=self.average_case + self.ppy + str(profit_per_year.calc_p_p_y(profit_per_year)[1] / 1000000) + self.mio_euro).grid(column=0, row=1)
        l3 = Label(frm, text=self.worst_case + self.ppy + str(profit_per_year.calc_p_p_y(profit_per_year)[2] / 1000000) + self.mio_euro).grid(column=0, row=2)

        l4 = Label(frm,  text=self.best_case + self.tpy + str(turnover_per_year.calc_t_p_y(profit_per_year)[0] / 1000000) + self.mio_euro).grid(column=0, row=3)
        l5 = Label(frm,  text=self.average_case + self.tpy + str(turnover_per_year.calc_t_p_y(profit_per_year)[1] / 1000000) + self.mio_euro).grid(column=0, row=4)
        l6 = Label(frm,  text=self.worst_case + self.tpy + str(turnover_per_year.calc_t_p_y(profit_per_year)[2] / 1000000) + self.mio_euro).grid(column=0, row=5)
              
        l7 = Label(frm,  text=self.best_case + self.cpy + str(Cycles.calc_cycles(Cycles)[0]) + self.cyc).grid(column=0, row=6)
        l8 = Label(frm,  text=self.average_case + self.cpy + str(Cycles.calc_cycles(Cycles)[1]) + self.cyc).grid(column=0, row=7)
        l9 = Label(frm,  text=self.worst_case + self.cpy + str(Cycles.calc_cycles(Cycles)[2]) + self.cyc).grid(column=0, row=8)
        
        l10 = Label(frm, text=self.best_case + self.ypy + str(yield_per_year.calc_y_p_y(yield_per_year)[0] / 1000000) + self.tn).grid(column=1, row=0)
        l11 = Label(frm, text=self.average_case + self.ypy + str(yield_per_year.calc_y_p_y(yield_per_year)[1] / 1000000) + self.tn).grid(column=1, row=1)
        l12 = Label(frm, text=self.worst_case + self.ypy + str(yield_per_year.calc_y_p_y(yield_per_year)[2] / 1000000) + self.tn).grid(column=1, row=2)
        
        l13 = Label(frm, text=self.best_case + self.ypp + str(Yield.calc_yield(Yield)[0]) + 'g').grid(column=1, row=3)
        l14 = Label(frm, text=self.average_case + self.ypp + str(Yield.calc_yield(Yield)[1]) + 'g').grid(column=1, row=4)
        l15 = Label(frm, text=self.worst_case + self.ypp + str(Yield.calc_yield(Yield)[2]) + 'g').grid(column=1, row=5)

    
        #self.center_gui(self,window)
        window.mainloop()
    #End Window
