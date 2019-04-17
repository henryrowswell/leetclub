class reprVsStr(object):
    def __init__(self, val):
        self.val = val
    
    def __repr__(self):
        return '__repr__{}'.format(self.val)
    
    def __str__(self):
        return '__str__{}'.format(self.val)

a = reprVsStr("a")
