class Package:
    def addAtribute(self, attribute, value):
        return setattr(self, attribute, value)

    def contains(self, searchQuery):
        return searchQuery in self.__dict__.values()
