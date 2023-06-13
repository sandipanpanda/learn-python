# import module as namespace
import helpers
helpers.display('Message 1')

# import all into current namespace
from helpers import *
display('Message 2')

# import specific items into current namespace
from helpers import display
display('Message 3', True)