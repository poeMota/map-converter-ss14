class Component:
    def __init__(self, dontShowOnDefault: bool = False):
        self._dontShowOnDefault = dontShowOnDefault

    def _serialize(self):
        defaultParams = self.defaultParametrs()
        ret = {"type": type(self).__name__.replace("Component", "")}
        params = {
            name: self._convert(value) for name, value in vars(self).items()
            if (not callable(value)
            and not name.startswith('_')
            and (name not in defaultParams or value != defaultParams[name]))
        }
        if not params and self._dontShowOnDefault: return

        ret.update(params)
        return ret

    def _convert(self, value):
        if type(value) is list:
            return ",".join([str(i) for i in value])
        return value


    def defaultParametrs(self) -> dict:
        arg_names = self.__init__.__code__.co_varnames[:self.__init__.__code__.co_argcount]
        defaults = self.__init__.__defaults__ or ()
        positional_defaults = dict(zip(arg_names[-len(defaults):], defaults))
        keyword_defaults = self.__init__.__kwdefaults__ or {}

        return {**positional_defaults, **keyword_defaults}

