class Package:
    def addAtribute(self, attribute, value):
        return setattr(self, attribute, value)


packages = []

with open("packages.txt", mode='r', encoding='utf-8-sig', newline='/n') as data_input:
    newPackage = Package()
    for line in data_input:
        if not line.strip():
            packages.append(newPackage)
            newPackage = Package()
        else:
            beforeAndAfterColon = line.split(':')
            attribute = beforeAndAfterColon[0]
            value = beforeAndAfterColon[1]
            newPackage.addAtribute(attribute, value)
