class Package:
    def addAtribute(self, attribute, value):
        return setattr(self, attribute, value)


# for each line in the file
with open("packages.txt") as data_input:
    for line in data_input:

        if not line.strip():
            # add object to arr
            # create new empty object
        else
        # check where the : is
        # take stuff before as key and stuff after as value put it into an object


adduser = Package("adduser", "all", "3.116ubuntu1", "foreign", "important", "admin", "Ubuntu", "Ubuntu Core Developers <ubuntu-devel-discuss@lists.ubuntu.com>", "Debian Adduser Developers <adduser-devel@lists.alioth.debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 624, 'passwd, debconf (>= 0.5) | debconf-2.0', "liblocale-gettext-perl, perl, ecryptfs-utils (>= 67-1)",
                  "pool/main/a/adduser/adduser_3.116ubuntu1_all.deb", 162684, "97dff943493ad5831c5bfa67e4b503ac", "5f3a18ea4515c5afdbd54f326ffd2707ca571124", "d451eb00b2d0e2940e26028ea9f2fb1be4f5109010e997acfb2c46229ebd9ebe", "http://alioth.debian.org/projects/adduser/", "add and remove users and groups", "minimal", "7965b5cd83972a254552a570bcd32c93", "yes", "5y")
# apt = Package("apt", "amd64", "1.6.1", "important", "admin", "Ubuntu", "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", "APT Development Team <deity@lists.debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 3805, "apt-transport-https (= 1.6.1)", "adduser, gpgv | gpgv2 | gpgv1, ubuntu-keyring, libapt-pkg5.0 (>= 1.6.1), libc6 (>= 2.15), libgcc1 (>= 1:3.0), libgnutls30 (>= 3.5.6), libseccomp2 (>= 1.0.1), libstdc++6 (>= 5.2)", "ca-certificates", "apt-doc, aptitude | synaptic | wajig, dpkg-dev (>= 1.17.2), gnupg | gnupg2 | gnupg1, powermgmt-base", "apt-transport-https (<< 1.5~alpha4~), apt-utils (<< 1.3~exp2~), aptitude (<< 0.8.10)", "apt-transport-https (<< 1.5~alpha4~), apt-utils (<< 1.3~exp2~)", "pool/main/a/apt/apt_1.6.1_amd64.deb", 1166400, "8703b482ccad77b727e47f23247162a6", "a363ab9d70d0d6cfe3d71e5c85cea6b361cc40d3", "2ff201fadafd345f30c11824fa039d3ab9dfe34411d9ef45a7872a84498de9ff", "commandline package manager", "minimal", "9fb97a88cb7383934ef963352b53b4a7","yes", "5y")
# baseFiles = Package("base-file", "amd64", "10.1ubuntu2", "foreign", "required", "yes", "admin", "Ubuntu", "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", "Santiago Vila <sanvila@debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 375, "base", "awk", "initscripts (<< 2.88dsf-13.3), sendfile (<< 2.1b.20080616-5.2~)", "base, dpkg (<= 1.15.0), miscutils", "pool/main/b/base-files/base-files_10.1ubuntu2_amd64.deb", 58168,"347758ec69be8eaa0042c2831bba251d", "dcdbcd1b70ab49998eff9e8eebbac93ebe593626", "81d5fa6a8c31b739299552338ee1d1a7efe4b302702d157f3b67389bc1a948aa", "Debian base system miscellaneous files", "minimal", "6d16337f57b84c4747f56438355b2395", "5y")
# basePasswd = Package("base-passwd", "amd64", "3.5.44", "foreign", "required", "yes", "admin", "Ubuntu", "Colin Watson <cjwatson@debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 228,"libc6 (>= 2.8), libdebconfclient0 (>= 0.145)", "debconf (>= 0.5) | debconf-2.0", "base", "pool/main/b/base-passwd/base-passwd_3.5.44_amd64.deb", 47236, "aebe1a3831dec58dc5b87ec0661b3601", "ac2cc8b99766c74c23c94ef5669442342ba0b06d", "6910f5a7f6fa9ba8eb98e3925abba9709bd28cf6f368955e536119ad39e9ad94", "Debian base system master password and group files", "minimal", "aad0cc52ee72b2469af5552851e49f03", "5y")
# bash = Package("bash", "amd64", "4.4.18-2ubuntu1", "foreign", "required", "yes", "shells", "Ubuntu", "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", "Matthias Klose <doko@debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 1588, "libc6 (>= 2.15), libtinfo5 (>= 6)", "base-files (>= 2.1.12), debianutils (>= 2.15)", "bash-completion (>= 20060301-0)", "bash-doc", "bash-completion (<< 20060301-0)", "bash-completion (<< 20060301-0), bash-doc (<= 2.05-1)", "pool/main/b/bash/bash_4.4.18-2ubuntu1_amd64.deb", 614184, "bb172fdca61d926fe61d8e642876f369", "ff433274a20b8d832387d4a2fecaabd2786d98b1", "5895e980d1fc874906d27823ab31eeb65cfe1d059936b9d6d304bfee02c8995c", "http://tiswww.case.edu/php/chet/bash/bashtop.html", "GNU Bourne Again SHell", "minimal", "3522aa7b4374048d6450e348a5bb45d9", "5y")
# bsdutils = Package("bsdutils", "amd64", "1:2.31.1-0.4ubuntu3", "foreign", "required", "yes", "utils", "util-linux (2.31.1-0.4ubuntu3)", "Ubuntu", "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", "LaMont Jones <lamont@debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 263, "libc6 (>= 2.14), libsystemd0", "bsdmainutils", "bash-completion (<< 1:2.1-4.1~)", "bash-completion (<< 1:2.1-4.1~)", "pool/main/u/util-linux/bsdutils_2.31.1-0.4ubuntu3_amd64.deb", 60192, "099eedecd2d1837b5042207c4638fad3", "78a03221745b00360aa0c68f25491728c559a6f1", "842bf6a7fbe2b179185ebfa3032771972a4f18405c398a792759f1a98b419a85", "basic utilities from 4.4BSD-Lite", "minimal", "48257031d7f91a8655d15ca8e9e4e07d", "5y")
# bzip = Package("bzip2", "amd64", "1.0.6-8.1", "foreign", "important", "utils", "Ubuntu", "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", "Anibal Monsalve Salazar <anibal@debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 177, "libbz2-1.0 (= 1.0.6-8.1), libc6 (>= 2.14)", "bzip2-doc", "libbz2 (<< 0.9.5d-3)", "pool/main/b/bzip2/bzip2_1.0.6-8.1_amd64.deb", 33430, "d459b2b06f2c1cb75a068d1d8055175c", "250af937d2b37cc508c8bf71a7c1f0d2c72c78bd", "69a037ca02b43dcbb578cfd29a2d703ed55771cc68e681c5f67343b85e3fa244", "http://www.bzip.org/", "high-quality block-sorting file compressor - utilities", "minimal", "26e9d96b611ed3cf741ba7007fd4f233", "yes", "5y")
# coreutils = Package("coreutils", "amd64", "8.28-1ubuntu1", "foreign", "required", "yes", "utils", "Ubuntu", "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", "Michael Stone <mstone@debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 6560, "libacl1 (>= 2.2.51-8), libattr1 (>= 1:2.4.46-8), libc6 (>= 2.25), libselinux1 (>= 2.1.13)", "pool/main/c/coreutils/coreutils_8.28-1ubuntu1_amd64.deb", 1230832, "7d95d8dbaca7e89694e63ea4aa907c55", "297d10f91608486816dddfa439a308bb9e3361c8", "24541a48e25dfb17c98ce77dda61800e6cd68d74c25725753613fbcc00f2418f", "http://gnu.org/software/coreutils", "GNU core utilities", "minimal", "d0d975dec3625409d24be1238cede238", "5y")
# dash = Package("dash", "amd64", "0.5.8-2.10", "required", "yes", "shells", "Ubuntu", "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", "Gerrit Pape <pape@smarden.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 214, "libc6 (>= 2.14)", "debianutils (>= 2.15), dpkg (>= 1.15.0)", "pool/main/d/dash/dash_0.5.8-2.10_amd64.deb", 88544, "ffa3e8183dee1f73e5236afdf5a6cfe1", "725ef02f71f816f9c6a0be99bf9cc1795ee56fa6", "51fe28b98b8e023325ae8868f29807cdb53f6f2eac943723b5e6bd47cde0cb2c", "http://gondor.apana.org.au/~herbert/dash/", "POSIX-compliant shell", "minimal", "8d4d9c32c6b2b70328f7f774a0cc1248", "5y")
# debconf = Package("debconf", "all", "1.5.66", "foreign", "required", "admin", "Ubuntu", "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", 'Debconf Developers <debconf-devel@lists.alioth.debian.org>', "https://bugs.launchpad.net/ubuntu/+filebug", 545, "debconf-2.0", "perl-base (>= 5.20.1-3~)", "apt-utils (>= 0.5.1), debconf-i18n", "debconf-doc, debconf-utils, whiptail | dialog, libterm-readline-gnu-perl, libgtk3-perl, libnet-ldap-perl, perl, libqtgui4-perl, libqtcore4-perl", "apt (<< 0.3.12.1), cdebconf (<< 0.96), debconf-tiny, debconf-utils (<< 1.3.22), dialog (<< 0.9b-20020814-1), menu (<= 2.1.3-1), whiptail (<< 0.51.4-11), whiptail-utf8 (<= 0.50.17-13)", "apt-listchanges (<< 3.14), ubiquity (<< 17.10.2), update-notifier-common (<< 3.187~)", "debconf-tiny", "pool/main/d/debconf/debconf_1.5.66_all.deb", 123836, "2c66355efb679b954fb3c5c2376a5366", "d2eb92e915eab55165a6142e0097f6201c1eebe3", '4d15dfec3cac2d9edae8d57703bd01d05027e0fb5c1e3f4f54539768ddfd8c83', "Debian configuration management system", "minimal", "85b82bf406dfc9a635114f44ab7fb66d", "5y")
# debianutils = Package("debianutils", "amd64", "4.8.4", "foreign", "required", "yes", "utils", "Ubuntu", "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", "Clint Adams <clint@debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 212, "libc6 (>= 2.15)", "pool/main/d/debianutils/debianutils_4.8.4_amd64.deb", 85672, "221b1684dff6c8dcd04756f5644be139", '2232d5293fe3b051fd85b333c4d64cbb1332a874', "2956dc70a0bd3a56365922c8f90cf9b9d0917a0308d6ea310e0f94d8ea4e11bf", "Miscellaneous utilities specific to Debian", "minimal, ubuntu-core", "ccafef5bb90a2453aecca96cbb772d23", "5y")
# diffutils = Package("diffutils", "amd64", "1:3.6-1", "required", "yes", "utils", "Ubuntu", "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", "Santiago Vila <sanvila@debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 452, "libc6 (>= 2.17)", "diffutils-doc, wdiff", "diff", "pool/main/d/diffutils/diffutils_3.6-1_amd64.deb", 167178, "20ecce81c5828c75a27353ad13a50d19", "71c2356705201b1a1332fd95f1d2dd7ff5b79bc5", "4a2f0f62cb9c7bc00d535e85f5629eb9f513e9c6161474a95445db1c446b5dc1", "http://www.gnu.org/software/diffutils/", "File comparison utilities", "minimal", "5cf0bc18e36aa2957e62b309d6aa34f9", "5y")
# dpkg = Package("dpkg", "amd64", "1.19.0.5ubuntu2", "foreign", "required", "yes", "admin", "Ubuntu", "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", "Dpkg Developers <debian-dpkg@lists.debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 6773, "libbz2-1.0, libc6 (>= 2.14), liblzma5 (>= 5.2.2), libselinux1 (>= 2.3), libzstd1 (>= 1.3.2), zlib1g (>= 1:1.1.4)", 'tar (>= 1.28-1)', "apt, debsig-verify", "acidbase (<= 1.4.5-4), amule (<< 2.3.1+git1a369e47-3), beep (<< 1.3-4), im (<< 1:151-4), libdpkg-perl (<< 1.18.11), netselect (<< 0.3.ds1-27), pconsole (<< 1.0-12), phpgacl (<< 3.3.7-7.3), pure-ftpd (<< 1.0.43-1), systemtap (<< 2.8-1), terminatorx (<< 4.0.1-1), xvt (<= 2.1-20.1)", "pool/main/d/dpkg/dpkg_1.19.0.5ubuntu2_amd64.deb", 1139464, "655a349afa275cae790929defe2e07f8", "74d1b2591b043ef8e74abbc6cc1ff53942e59ff5", "ece5ad51a21fb17c0f63a755a1e925097b5137e6c62c96a6f160696928259bc3", "https://wiki.debian.org/Teams/Dpkg", "Debian package management system", "minimal", "2f156c6a30cc39895ad3487111e8c190", "5y")
# e2sprogs = Package("e2fsprogs", "amd64", "1.44.1-1", "foreign", "required", "yes", "admin", "Ubuntu", "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", "Theodore Y. Ts'o <tytso@mit.edu>", "https://bugs.launchpad.net/ubuntu/+filebug", 1222, "libblkid1 (>= 2.17.2), libc6 (>= 2.14), libcom-err2 (>= 1.42~WIP-2011-10-05-1), libext2fs2 (= 1.44.1-1), libss2 (>= 1.34-1), libuuid1 (>= 2.16)", "e2fsprogs-l10n", "gpart, parted, fuse2fs, e2fsck-static", "pool/main/e/e2fsprogs/e2fsprogs_1.44.1-1_amd64.deb", 390444, "e73fc4bdf03e7e3c87dedd6d8c2aef68", "8a6347ef4d806a899229e30daa1eb5326f763f63", "ccc18dea2f3bfef240c179ff142fbff07d084706848579a85bbbd955e2ddc045", "http://e2fsprogs.sourceforge.net", "ext2/ext3/ext4 file system utilities", "minimal, ubuntu-core", "92d0fdf684262bbfa702eaea3f50b97e", "5y")
# fdisk = Package("fdisk", "amd64", "2.31.1-0.4ubuntu3", "foreign", "required", "utils", "util-linux", "Ubuntu", "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", "LaMont Jones <lamont@debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 426, "libc6 (>= 2.14), libfdisk1 (>= 2.31.1), libmount1 (>= 2.24.2), libncursesw5 (>= 6), libsmartcols1 (>= 2.28~rc1), libtinfo5 (>= 6)", "util-linux (<< 2.30.1-0ubuntu4~)", "util-linux (<< 2.30.1-0ubuntu4~)", "pool/main/u/util-linux/fdisk_2.31.1-0.4ubuntu3_amd64.deb", 107708, "fc647fb18feccf78209c879579de56e9", "aa4429efc25bc000c999896d97049f976b511209", "1634050aa9bcf1b097e6bf143eed1e6cad207de4992c8d298107b7dc322fad32", "collection of partitioning utilities", "minimal", "yes", "389774810aae3f2323ace16ab9ab19ae", "5y")
# findutils = Package("findutils", "amd64", "4.6.0+git+20170828-2", "foreign", "required", "yes", "utils", "Ubuntu", "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", "Andreas Metzler <ametzler@debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 580, "libc6 (>= 2.17), libselinux1 (>= 1.32)", "mlocate | locate", "binstats (<< 1.08-8.1), guilt (<< 0.36-0.2), libpython3.4-minimal (<< 3.4.4-2), libpython3.5-minimal (<< 3.5.1-3), lsat (<< 0.9.7.1-2.1), mc (<< 3:4.8.11-1), switchconf (<< 0.0.9-2.1)", "pool/main/f/findutils/findutils_4.6.0+git+20170828-2_amd64.deb", 291344, "e8ea676b048bfade863f589082c9cc37", "eed1af211944c619c58567f0a3a8b4537483ef9f", "70a920ad25287775ed169b20405703f85860e7fba0cf0672e2aea6b800835b26", "https://savannah.gnu.org/projects/findutils/", "utilities for finding files--find, xargs", "minimal", "ad1a783819241ffdf3ff5f37a676af59", "5y")
# ggc8base = Package("gcc-8-base", "amd64", "8-20180414-1ubuntu2", "same", "required", "libs", "gcc-8", "Ubuntu", "Ubuntu Core developers <ubuntu-devel-discuss@lists.ubuntu.com>", "Debian GCC Maintainers <debian-gcc@lists.debian.org>", "https://bugs.launchpad.net/ubuntu/+filebug", 106, "gcc-4.4-base (<< 4.4.7), gcc-4.7-base (<< 4.7.3), gcj-4.4-base (<< 4.4.6-9~), gcj-4.6-base (<< 4.6.1-4~), gnat-4.4-base (<< 4.4.6-3~), gnat-4.6 (<< 4.6.1-5~)", "pool/main/g/gcc-8/gcc-8-base_8-20180414-1ubuntu2_amd64.deb", 18192, "6659c8be5599cfd5b8c6e842555bcd4c", "33f69eb42899967b96995f761c861afd041b6cde", "9e07db32880d60c76c82a40f4f08d72ee74d08efdb278476781af6f76d21ce72", "http://gcc.gnu.org/", "GCC, the GNU Compiler Collection (base package)", "minimal", "b6e93638a6d08ea7a18929d7cf078e5d", "5y")
