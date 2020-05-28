import uproot

class EventBuilder(object):
    def build_single_file(self,inpath,treepath):
        file = uproot.open(inpath)
        tree = file[treepath] 
        return file,tree
