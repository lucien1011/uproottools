import numpy,matplotlib
import uproot_methods as um
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class HistManager(object):
    def __init__(self):
        self.hist_dict = {}
    
    def book(self,var):
        self.hist_dict[var.name] = plt.hist([],bins=var.bins,range=var.range)
    
    def fill(self,var,array,):
        if var.type == "Hist":
            temp = plt.hist(array,bins=var.bins,range=var.range)
            if self.hist_dict[var.name] is None:
                self.hist_dict[var.name] = temp
            else:
                self.hist_dict[var.name] = (self.hist_dict[var.name][0]+temp[0],*temp[1:])
        else:
            raise RuntimeError

    def __getitem__(self,name):
        return self.hist_dict[name]
