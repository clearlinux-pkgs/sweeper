#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v27
# autospec commit: 65cf152
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : sweeper
Version  : 25.04.2
Release  : 80
URL      : https://download.kde.org/stable/release-service/25.04.2/src/sweeper-25.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/25.04.2/src/sweeper-25.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/25.04.2/src/sweeper-25.04.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
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
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : ki18n-dev
BuildRequires : plasma-activities-stats-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n sweeper-25.04.2
cd %{_builddir}/sweeper-25.04.2
pushd ..
cp -a sweeper-25.04.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1749479370
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1749479370
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sweeper
cp %{_builddir}/sweeper-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/sweeper/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang sweeper
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/sweeper
/usr/bin/sweeper

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.sweeper.desktop
/usr/share/dbus-1/interfaces/org.kde.sweeper.xml
/usr/share/icons/hicolor/scalable/apps/sweeper.svg
/usr/share/metainfo/org.kde.sweeper.appdata.xml
/usr/share/qlogging-categories6/sweeper.categories

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
/usr/share/doc/HTML/sl/sweeper/index.cache.bz2
/usr/share/doc/HTML/sl/sweeper/index.docbook
/usr/share/doc/HTML/sv/sweeper/index.cache.bz2
/usr/share/doc/HTML/sv/sweeper/index.docbook
/usr/share/doc/HTML/tr/sweeper/index.cache.bz2
/usr/share/doc/HTML/tr/sweeper/index.docbook
/usr/share/doc/HTML/tr/sweeper/sweeper.png
/usr/share/doc/HTML/uk/sweeper/index.cache.bz2
/usr/share/doc/HTML/uk/sweeper/index.docbook
/usr/share/doc/HTML/uk/sweeper/sweeper.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sweeper/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567

%files locales -f sweeper.lang
%defattr(-,root,root,-)

