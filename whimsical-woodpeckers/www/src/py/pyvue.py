# __pragma__ ('js', "{}", "import * as VuePkg from 'vue';")
# __pragma__ ('noalias', 'default')
# __pragma__ ('noalias', 'name')


JSVue = VuePkg.default


def clone_data(data):
    if isinstance(data, dict):
        new_data = dict(data)
        # __pragma__ ('iconv')
        for key in new_data:
            new_data[key] = clone_data(new_data[key])
        # __pragma__ ('noiconv')
    elif isinstance(data, list):
        new_data = list(data)
        for i, data in enumerate(new_data):
            new_data[i] = clone_data(data)
    else:
        new_data = data
    return new_data


class Vue:
    data = {}
    template = ""
    components = {}

    def __init__(self, el):
        self.el = el
        self.data = clone_data(self.data)
        methods = {func: getattr(self, func) for func in dir(self) if callable(getattr(self, func)) and not func.startswith("__")}
        data = self.get_component()
        data['el'] = el
        self._vue = __new__(JSVue(data))

    def get_component(self):
        methods = {func: getattr(self, func) for func in dir(self) if callable(getattr(self, func)) and not func.startswith("__")}
        data = {
            "data": self.data,
            "template": self.template
        }
        # __pragma__("tconv")
        if methods:
            data['methods'] = methods
        if self.components:
            data['components'] = self.components
        # __pragma__("notconv")
        return data


def making_component(comp):
    def func(one, two, three):
        console.log(one, two, three)
        return __new__(comp(one, two))
    return func


class Component:
    data = {}
    template = ""
    props = []
    components = {}

    def __init__(self):
        self._vue = self.get_component()
        JSVue.component(self.__class__.__name__.lower(), self._vue)

    @classmethod
    def get_component(cls):
        methods = {func: getattr(cls, func) for func in dir(cls) if callable(getattr(cls, func)) and not func.startswith("__")}
        data = {
            "data": cls.get_data,
            "template": cls.template
        }
        # __pragma__("tconv")
        if methods:
            data['methods'] = methods
        if cls.components:
            data['components'] = cls.components
        if cls.props:
            data['props'] = cls.props
        # __pragma__("notconv")
        return JSVue.extend(data)

    @classmethod
    def get_data(cls):
        return clone_data(cls.data)

#
#
# def createComponent(one, two):
#     console.log(this, one, two)
#
# class Component:
#     data = {}
#     props = []
#     template = ""
#     _registration = None
#     name = ""
#     methods = {}
#
#     def __init__(self):
#         self.name = self.name
#         self.data = clone_data(self.data)
#         self.methods = {func: getattr(self, func) for func in dir(self) if callable(getattr(self, func)) and
#                         not func.startswith("__")}
#         # self._vue = __new__(JSVue.component(self.name, self.__class__))
#
#     @classmethod
#     def get_data(cls):
#         return clone_data(cls.data)
#
#     @classmethod
#     def create_data(cls):
#         # methods = {func: getattr(cls, func) for func in dir(cls) if callable(getattr(cls, func)) and
#                      not func.startswith("__")}
#         data = clone_data(cls.data)
#         methods = dict(cls.methods)
#         methods['created'] = createComponent
#         console.log(methods)
#         return {
#             "name": cls.name,
#             "data": cls.get_data,
#             "methods": methods,
#             "template": cls.template
#         }
#
#
#
#
#     @classmethod
#     def register(cls, name):
#         name = name
#         if not name:
#             name = cls.__name__
#         cls.name = name
#         console.log(name, cls)
#         data = cls.create_data()
#         console.log(data)
#         cls._registration = JSVue.component(name, data)
#
#
#
