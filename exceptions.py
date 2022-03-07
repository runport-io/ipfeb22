# Copyright Port. Prerogative Club ("the Club")
#
# 
# This file is part of Port. 2 ("Port.")
#
# Port. is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Port. is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Port. If not, see <https://www.gnu.org/licenses/>.
#
# Questions? Contact hi@runport.io.

# Imports
# 1) Built-ins
# N/a

# 2) Port.
# N/a

# 3) Constants
# N/a

# 4) Functions
class PortError(Exception):
    """

    Ancestor for exceptions made by Port. 
    """
    pass

class OverrideError(PortError):
    """

    Flag for when you try to overwrite a value that has protection.
    """
    pass

class PlaceholderError(PortError):
    """

    Flag for operations that I have not yet defined.
    """
    pass

class ParameterError(PortError):
    """

    Flag for something beinng wrong with inputs.
    """
    pass

class OperationError(PortError):
    """

    I raise this when the outcome differs from what I wanted.
    """
    pass
