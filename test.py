import pytgcalls
import pkgutil

module_path = pytgcalls.__path__[0]

submodules = [name for _, name, _ in pkgutil.iter_modules([module_path])]
print(submodules)
