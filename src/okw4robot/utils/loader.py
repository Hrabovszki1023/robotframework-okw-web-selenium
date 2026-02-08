import importlib

def load_class(qualified_name: str):
    module_name, class_name = qualified_name.rsplit(".", 1)
    module = importlib.import_module(module_name)
    return getattr(module, class_name)