class Choice:

    def __init__(self, default=None, options=list()):
        self.value = Value(default)
        self._default = default
        self._options = options
        self._cache = list()

    def get(self):
        result = self.value.get()
        return result

    def set(self, value, force=False):
        if not force:
            if value in options:
                self.value.set(value)
            else:
                raise Exception
        else:
            self.value.set(value)
    
    def reset(self):
        self.value.set(self._default)
    
    def toggle(self):
        """

        Method sets value to the first item in options, puts existing 
        """

        if not self._cache:
            self._cache = self._options.copy()
            # should really be up to and after the current item

        old = self.get()
        new = self._options.pop(0)

        #<------------------------------------------------------ start here.
        
        cat_old = self.get()
        cat_new = self._permitted_values.pop(0)
        
        if old_cat in self._:
            self._toggle_state.append(old_cat)
            # so I can keep cycling

        self.set(new)
