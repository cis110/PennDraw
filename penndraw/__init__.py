import inspect
from . import penndraw as core

# Import all functions from core
CONSTANTS = ["BLACK", "WHITE", "RED", "GREEN", "BLUE",
             "YELLOW", "CYAN", "MAGENTA", "ORANGE", "PINK",
             "GRAY", "DARK_GRAY", "LIGHT_GRAY", "HSS_RED",
             "HSS_BLUE", "HSS_YELLOW", "HSS_ORANGE", "TQM_NAVY",
             "TQM_BLUE", "TQM_WHITE"]

for const in CONSTANTS:
    globals()[const] = getattr(core, const)

__all__ = []
for name, obj in inspect.getmembers(core):
    if inspect.isfunction(obj) or inspect.isclass(obj):
        globals()[name] = obj
        __all__.append(name)
__all__.extend(CONSTANTS)

# If you have any package-level variables or constants, you can define them here
__version__ = "0.1.8"

# Add the version to __all__
__all__.append('__version__')
