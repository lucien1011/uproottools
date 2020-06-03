import uproot

class EventBuilder(object):
    def build_single_file(self,in_path,tree_path):
        file = uproot.open(in_path)
        tree = file[tree_path] 
        return file,tree

    def build_by_file_pattern(self,file_pattern,tree_path,branches,namedecode):
        for path, file, start, stop, arrays in uproot.iterate(file_pattern,tree_path,branches,reportpath=True, reportfile=True, reportentries=True, namedecode=namedecode):
            print(path, file, start, stop, len(arrays))
