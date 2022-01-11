#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : sweeper
Version  : 21.12.1
Release  : 34
URL      : https://download.kde.org/stable/release-service/21.12.1/src/sweeper-21.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.12.1/src/sweeper-21.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.12.1/src/sweeper-21.12.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: sweeper-bin = %{version}-%{release}
Requires: sweeper-data = %{version}-%{release}
Requires: sweeper-license = %{version}-%{release}
Requires: sweeper-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
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
%setup -q -n sweeper-21.12.1
cd %{_builddir}/sweeper-21.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641925207
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1641925207
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sweeper
cp %{_builddir}/sweeper-21.12.1/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/sweeper/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
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
/usr/share/qlogging-categories5/sweeper.categories

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
/usr/share/doc/HTML/ru/sweeper/index.cache.bz2
/usr/share/doc/HTML/ru/sweeper/index.docbook
/usr/share/doc/HTML/sv/sweeper/index.cache.bz2
/usr/share/doc/HTML/sv/sweeper/index.docbook
/usr/share/doc/HTML/uk/sweeper/index.cache.bz2
/usr/share/doc/HTML/uk/sweeper/index.docbook
/usr/share/doc/HTML/uk/sweeper/sweeper.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sweeper/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567

%files locales -f sweeper.lang
%defattr(-,root,root,-)

