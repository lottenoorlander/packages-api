class Package:
    def addAtribute(self, attribute, value):
        return setattr(self, attribute, value)

    def contains(self, searchQuery):
        # could make this better by creating a regex and searching for that in the value insted of searching the exact expression in values
        return searchQuery in self.__dict__.values()
