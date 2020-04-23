#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : sweeper
Version  : 20.04.0
Release  : 18
URL      : https://download.kde.org/stable/release-service/20.04.0/src/sweeper-20.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.04.0/src/sweeper-20.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.04.0/src/sweeper-20.04.0.tar.xz.sig
Summary  : System Cleaner
Group    : Development/Tools
License  : LGPL-2.1
Requires: sweeper-bin = %{version}-%{release}
Requires: sweeper-data = %{version}-%{release}
Requires: sweeper-license = %{version}-%{release}
Requires: sweeper-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kactivities-stats-dev
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package bin
Summary: bin components for the sweeper package.
Group: Binaries
Requires: sweeper-data = %{version}-%{release}
Requires: sweeper-license = %{version}-%{release}

%description bin
bin components for the sweeper package.


%package data
Summary: data components for the sweeper package.
Group: Data

%description data
data components for the sweeper package.


%package doc
Summary: doc components for the sweeper package.
Group: Documentation

%description doc
doc components for the sweeper package.


%package license
Summary: license components for the sweeper package.
Group: Default

%description license
license components for the sweeper package.


%package locales
Summary: locales components for the sweeper package.
Group: Default

%description locales
locales components for the sweeper package.


%prep
%setup -q -n sweeper-20.04.0
cd %{_builddir}/sweeper-20.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587673870
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1587673870
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sweeper
cp %{_builddir}/sweeper-20.04.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/sweeper/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd
%find_lang sweeper

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sweeper

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.sweeper.desktop
/usr/share/dbus-1/interfaces/org.kde.sweeper.xml
/usr/share/kxmlgui5/sweeper/sweeperui.rc
/usr/share/metainfo/org.kde.sweeper.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/sweeper/index.cache.bz2
/usr/share/doc/HTML/ca/sweeper/index.docbook
/usr/share/doc/HTML/de/sweeper/index.cache.bz2
/usr/share/doc/HTML/de/sweeper/index.docbook
/usr/share/doc/HTML/de/sweeper/sweeper.png
/usr/share/doc/HTML/el/sweeper/index.cache.bz2
/usr/share/doc/HTML/el/sweeper/index.docbook
/usr/share/doc/HTML/el/sweeper/sweeper.png
/usr/share/doc/HTML/en/sweeper/index.cache.bz2
/usr/share/doc/HTML/en/sweeper/index.docbook
/usr/share/doc/HTML/en/sweeper/sweeper.png
/usr/share/doc/HTML/es/sweeper/index.cache.bz2
/usr/share/doc/HTML/es/sweeper/index.docbook
/usr/share/doc/HTML/et/sweeper/index.cache.bz2
/usr/share/doc/HTML/et/sweeper/index.docbook
/usr/share/doc/HTML/fr/sweeper/index.cache.bz2
/usr/share/doc/HTML/fr/sweeper/index.docbook
/usr/share/doc/HTML/it/sweeper/index.cache.bz2
/usr/share/doc/HTML/it/sweeper/index.docbook
/usr/share/doc/HTML/nl/sweeper/index.cache.bz2
/usr/share/doc/HTML/nl/sweeper/index.docbook
/usr/share/doc/HTML/pt/sweeper/index.cache.bz2
/usr/share/doc/HTML/pt/sweeper/index.docbook
/usr/share/doc/HTML/pt_BR/sweeper/index.cache.bz2
/usr/share/doc/HTML/pt_BR/sweeper/index.docbook
/usr/share/doc/HTML/pt_BR/sweeper/sweeper.png
/usr/share/doc/HTML/sv/sweeper/index.cache.bz2
/usr/share/doc/HTML/sv/sweeper/index.docbook
/usr/share/doc/HTML/uk/sweeper/index.cache.bz2
/usr/share/doc/HTML/uk/sweeper/index.docbook
/usr/share/doc/HTML/uk/sweeper/sweeper.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sweeper/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files locales -f sweeper.lang
%defattr(-,root,root,-)

