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
apt = Package("apt", "amd64", "1.6.1", "important", "admin", "Ubuntu", "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", "APT Development Team <deity@lists.debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 3805, "apt-transport-https (= 1.6.1)", "adduser, gpgv | gpgv2 | gpgv1, ubuntu-keyring, libapt-pkg5.0 (>= 1.6.1), libc6 (>= 2.15), libgcc1 (>= 1:3.0), libgnutls30 (>= 3.5.6), libseccomp2 (>= 1.0.1), libstdc++6 (>= 5.2)", "ca-certificates", "apt-doc, aptitude | synaptic | wajig, dpkg-dev (>= 1.17.2), gnupg | gnupg2 | gnupg1, powermgmt-base", "apt-transport-https (<< 1.5~alpha4~), apt-utils (<< 1.3~exp2~), aptitude (<< 0.8.10)", "apt-transport-https (<< 1.5~alpha4~), apt-utils (<< 1.3~exp2~)", "pool/main/a/apt/apt_1.6.1_amd64.deb", 1166400, "8703b482ccad77b727e47f23247162a6", "a363ab9d70d0d6cfe3d71e5c85cea6b361cc40d3", "2ff201fadafd345f30c11824fa039d3ab9dfe34411d9ef45a7872a84498de9ff", "commandline package manager", "minimal", "9fb97a88cb7383934ef963352b53b4a7","yes", "5y")
baseFiles = Package("base-file", "amd64", "10.1ubuntu2", "foreign", "required", "yes", "admin", "Ubuntu", "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", "Santiago Vila <sanvila@debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 375, "base", "awk", "initscripts (<< 2.88dsf-13.3), sendfile (<< 2.1b.20080616-5.2~)", "base, dpkg (<= 1.15.0), miscutils", "pool/main/b/base-files/base-files_10.1ubuntu2_amd64.deb", 58168,"347758ec69be8eaa0042c2831bba251d", "dcdbcd1b70ab49998eff9e8eebbac93ebe593626", "81d5fa6a8c31b739299552338ee1d1a7efe4b302702d157f3b67389bc1a948aa", "Debian base system miscellaneous files", "minimal", "6d16337f57b84c4747f56438355b2395", "5y")
basePasswd = Package("base-passwd", "amd64", "3.5.44", "foreign", "required", "yes", "admin", "Ubuntu", "Colin Watson <cjwatson@debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 228,"libc6 (>= 2.8), libdebconfclient0 (>= 0.145)", "debconf (>= 0.5) | debconf-2.0", "base", "pool/main/b/base-passwd/base-passwd_3.5.44_amd64.deb", 47236, "aebe1a3831dec58dc5b87ec0661b3601", "ac2cc8b99766c74c23c94ef5669442342ba0b06d", "6910f5a7f6fa9ba8eb98e3925abba9709bd28cf6f368955e536119ad39e9ad94", "Debian base system master password and group files", "minimal", "aad0cc52ee72b2469af5552851e49f03", "5y")
bash = Package("bash", "amd64", "4.4.18-2ubuntu1", "foreign", "required", "yes", "shells", "Ubuntu", "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", "Matthias Klose <doko@debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 1588, "libc6 (>= 2.15), libtinfo5 (>= 6)", "base-files (>= 2.1.12), debianutils (>= 2.15)", "bash-completion (>= 20060301-0)", "bash-doc", "bash-completion (<< 20060301-0)", "bash-completion (<< 20060301-0), bash-doc (<= 2.05-1)", "pool/main/b/bash/bash_4.4.18-2ubuntu1_amd64.deb", 614184, "bb172fdca61d926fe61d8e642876f369", "ff433274a20b8d832387d4a2fecaabd2786d98b1", "5895e980d1fc874906d27823ab31eeb65cfe1d059936b9d6d304bfee02c8995c", "http://tiswww.case.edu/php/chet/bash/bashtop.html", "GNU Bourne Again SHell", "minimal", "3522aa7b4374048d6450e348a5bb45d9", "5y")
bsdutils = Package("bsdutils", "amd64", "1:2.31.1-0.4ubuntu3", "foreign", "required", "yes", "utils", "util-linux (2.31.1-0.4ubuntu3)", "Ubuntu", "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", "LaMont Jones <lamont@debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 263, "libc6 (>= 2.14), libsystemd0", "bsdmainutils", "bash-completion (<< 1:2.1-4.1~)", "bash-completion (<< 1:2.1-4.1~)", "pool/main/u/util-linux/bsdutils_2.31.1-0.4ubuntu3_amd64.deb", 60192, "099eedecd2d1837b5042207c4638fad3", "78a03221745b00360aa0c68f25491728c559a6f1", "842bf6a7fbe2b179185ebfa3032771972a4f18405c398a792759f1a98b419a85", "basic utilities from 4.4BSD-Lite", "minimal", "48257031d7f91a8655d15ca8e9e4e07d", "5y")
bzip = Package("bzip2", "amd64", "1.0.6-8.1", "foreign", "important", "utils", "Ubuntu", "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", "Anibal Monsalve Salazar <anibal@debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 177, "libbz2-1.0 (= 1.0.6-8.1), libc6 (>= 2.14)", "bzip2-doc", "libbz2 (<< 0.9.5d-3)", "pool/main/b/bzip2/bzip2_1.0.6-8.1_amd64.deb", 33430, "d459b2b06f2c1cb75a068d1d8055175c", "250af937d2b37cc508c8bf71a7c1f0d2c72c78bd", "69a037ca02b43dcbb578cfd29a2d703ed55771cc68e681c5f67343b85e3fa244", "http://www.bzip.org/", "high-quality block-sorting file compressor - utilities", "minimal", "26e9d96b611ed3cf741ba7007fd4f233", "yes", "5y")
