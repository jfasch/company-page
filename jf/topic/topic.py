from .element import Element


class Topic(Element):
    def __init__(self, title, path, docname, dependencies):
        super().__init__(title=title, path=path, docname=docname)
        self.dependencies = dependencies
