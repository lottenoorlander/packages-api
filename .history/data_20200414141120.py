class Package:
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
    
adduser = Package("adduser", "all", "3.116ubuntu1", "foreign", "important", "admin", "Ubuntu", "Ubuntu Core Developers <ubuntu-devel-discuss@lists.ubuntu.com>", "Debian Adduser Developers <adduser-devel@lists.alioth.debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 624, 'passwd, debconf (>= 0.5) | debconf-2.0', "liblocale-gettext-perl, perl, ecryptfs-utils (>= 67-1)", "pool/main/a/adduser/adduser_3.116ubuntu1_all.deb", 162684, "97dff943493ad5831c5bfa67e4b503ac", "5f3a18ea4515c5afdbd54f326ffd2707ca571124", "d451eb00b2d0e2940e26028ea9f2fb1be4f5109010e997acfb2c46229ebd9ebe", "http://alioth.debian.org/projects/adduser/", "add and remove users and groups", "minimal", "7965b5cd83972a254552a570bcd32c93", "yes", "5y")
