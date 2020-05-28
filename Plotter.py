from .Module import Module

class Plotter(Module):
    def __init__(self,plots):
        self.plots = plots

    def begin(self):
        for p in self.plots: self.collector.histManager.book(p)

    def analyze(self,data):
        for p in self.plots:
            if not hasattr(p,"select_func"):
                self.collector.histManager.fill(p,p.value_func(data,self.collector))
            else:
                idx = p.select_func(data,self.collector)
                self.collector.histManager.fill(p,p.value_func(data,self.collector)[idx])
