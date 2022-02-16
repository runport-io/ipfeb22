# brand
# (c) Port. Prerogative Club 2022

# Port.
import utilities


class Brand:
    """
    
    A class that represents a unit of identity in business. 

    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:
    
    FUNCTIONS:
    get_name            returns the name of the brand
    set_name            sets the name, controls overrides
    get_label           returns the label of the brand; can be same as name
    set_label           set the label
    get_lines           returns list of strings for printing
    ------------------  --------------------------------------------------------
    """
    def __init__(self, name=None):
        self._label = name
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name, override=False):
        utilities.set_with_override(self, "_name", name, override=override)

    def get_label(self):
        return self._label or self._name

    def set_label(self, label):
        utilities.set_with_override(self, "_label", label, override=True)

    def get_lines(self, header=False):
        lines = list()
        if header:
            line0 = "Brand"
            lines.append(line0)
            
        line1 = "Name:      " + self.get_name()
        lines.append(line1)
        line2 = "Label:     " + self.get_label()
        lines.append(line2)

        return lines

    def __str__(self):
        lines = self.pretty_print()
        view = constants.NEW_LINE.join(lines)
        print(view)

    @classmethod
    def from_flat(cls, data):
        new = cls()
        new.__dict__.update(data)
        return new

#
utilities.add_attributes_to_skip(Brand) 
    
