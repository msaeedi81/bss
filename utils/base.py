from decouple import config


def import_config(name, default=None, class_type=str):
    if default is None:
        name = config(name)
    else:
        name = config(name, str(default))
    if issubclass(class_type, bool):
        if name == "True":
            name = True
        elif name == "False":
            name = False
        else:
            raise ValueError(f"{name} is not {class_type} type")
    elif issubclass(class_type, int) and str.isnumeric(name):
        name = int(name)
    return name
