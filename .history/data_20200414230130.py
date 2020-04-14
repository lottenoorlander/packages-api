class Package:
    def addAtribute(attribute, value):
        return setattr(self, attribute, value)


data = []

# for each line in the file
with open("packages.txt") as data_input:
    newPackage = Package()
    for line in data_input:
        if not line.strip():
            data.append(newPackage)
            newPackage = Package()
        else:
            attributeAndValue = line.split(':')
            attribute = attributeAndValue[0]
            value = attributeAndValue[1]
            newPackage.addAtribute(attribute, value)
            # check where the : is
            # take stuff before as key and stuff after as value put it into an object
