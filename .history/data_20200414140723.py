class Pacakage:
  def __init__(Package, Architecture, Version, MultiArch, Priority, Sextion, Origin, Maintainer, OriginalMaintainer, Bugs, InstalledSize, Depends, Suggests, Filename, Size, MD5sum, SHA1, SHA256, Homepage, Description, Task, DescriptionMd5, BuildEssential,Supported ):
    self.Package = Package
    self.Architecture = Architecture 
    self.Version = Version
    self["Multi-Arch"] = MultiArch 
    self.Priority = Priority 
    self.Sextion = Sextion 
    self.Origin = Origin
    self.Maintainer = Maintainer
    self["Original-Maintainer"] = OriginalMaintainer
    self.Bugs = Bugs
    self["Installed-Size"] = InstalledSize
    self.Depends = Depends
    self.Suggests = Suggests
    self.Filename = Filename
    self.Size = Size
    self.MD5sum = MD5sum
    self.SHA1 = SHA1
    self.SHA256 = SHA256
    self.Homepage = Homepage
    self.Description = Description
    self.Task = Task
    self["Description-md5"] = DescriptionMd5
    self["Build-Essential"] = BuildEssential
    self.Supported = Supported
    
