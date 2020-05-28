class EventLooper(object):
    def __init__(self,sequence,collector):
        self.sequence = sequence
        self.collector = collector

    def run(self,events,cfg):
        for m in self.sequence:
            m.collector = self.collector
            m.begin() 
        for data in events.iterate(**cfg):
            for m in self.sequence:
                passed = m.analyze(data)
                if not passed: break
        for m in self.sequence:
            m.end()
