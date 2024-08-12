class Component:
    def __init__(self):
        pass

    def _serialize(self):
        ret = {"type": type(self).__name__.replace("Component", "")}
        ret.update({
            name: self._convert(value) for name, value in vars(self).items() if not callable(value) and not name.startswith('__')
        })
        return ret

    def _convert(self, value):
        if type(value) is list:
            return ",".join([str(i) for i in value])
        return value

