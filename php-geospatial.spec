#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v3
# autospec commit: c1050fe
#
Name     : php-geospatial
Version  : 0.3.2
Release  : 51
URL      : https://pecl.php.net/get/geospatial-0.3.2.tgz
Source0  : https://pecl.php.net/get/geospatial-0.3.2.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-geospatial-lib = %{version}-%{release}
Requires: php-geospatial-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : perl(Getopt::Long)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package lib
Summary: lib components for the php-geospatial package.
Group: Libraries
Requires: php-geospatial-license = %{version}-%{release}

%description lib
lib components for the php-geospatial package.


%package license
Summary: license components for the php-geospatial package.
Group: Default

%description license
license components for the php-geospatial package.


%prep
%setup -q -n geospatial-0.3.2
cd %{_builddir}/geospatial-0.3.2
pushd ..
cp -a geospatial-0.3.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-geospatial
cp %{_builddir}/geospatial-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-geospatial/1979963df4747a96d74e8044f0046cf58a2a21a3 || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20230831/geospatial.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-geospatial/1979963df4747a96d74e8044f0046cf58a2a21a3
