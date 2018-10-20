class OrderedDict:
    def __init__(self):
        self._keys = []
        self._values = []
    
    def __setitem__(self, key, value):
        self._keys.append(key)
        self._values.append(value)
        
    def __getitem__(self, a_key):
        for k, v in zip(self._keys, self._values):
            if k == a_key:
                return v
        raise KeyError(repr(k))
                
    def __contains__(self, item):
        for k, v in zip (self._keys,self._values):
            if k == item:
                return True
        return False
        
    def __len__(self):
        return len(self._keys)
    
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for k, v in zip(self._keys, self._values):
            if k not in other or other[k] != v:
                return False
        return True
        
    def __ne__(self,other):
        return not self == other
        
    def __str__(self):
        s = '{'
        for k, v in zip(self._keys, self._values):
            s += '{}: {}, '.format(repr(k), repr(v))
        s = s.rstrip(', ')
        s += '}'
        return s
        
    __repr__ = __str__
    
    def __add__(self,other):
        new = OrderedDict()
        for k, v in self.items():
            new[k] = v
        for k, v in other.items():
            new[k] = v
        return new
        
        
    @classmethod
    def from_keys(cls, item):
        new = OrderedDict()
        for _ in item:
            new[_] = None
        return new
        
            
    def keys(self):
        return self._keys

    def values(self):
        return self._values

    def items(self):
        items = []
        for k, v in zip(self._keys, self._values):
            items.append((k, v))
        return items


