Name: s2geometry
Summary: S2 is a library for spherical geometry
Version: 0.11.1
Release: 1%{?dist}
License: Apache License 2.0
Group: Libraries/Geosciences
URL: https://s2geometry.io

Source: %{name}-%{version}.tar.gz

BuildRequires: gcc-c++ cmake
BuildRequires: openssl-devel
BuildRequires: gtest-devel
BuildRequires: pkgconfig(absl_algorithm)

%description
S2 library represents all data on a three-dimensional
sphere (similar to a globe). This makes it possible to build a
worldwide geographic database with no seams or singularities, using a
single coordinate system, and with low distortion everywhere compared
to the true shape of the Earth.

PackageName: S2 Geometry Library
Categories:
  - Science
  - Maps
  - Library
Custom:
  Repo: https://github.com/google/s2geometry
Screenshots:
  - http://s2geometry.io/devguide/img/s2hierarchy.gif

%package devel
Summary: s2geometry development headers
Group: Development/Libraries
Requires: %{name} = %{version}
Requires: openssl-devel
Requires: pkgconfig(absl_algorithm)


%description devel
This package provides headers for development

PackageName: S2 Geometry Library Development
Categories:
  - Science
  - Maps
  - Library
Custom:
  Repo: https://github.com/google/s2geometry

%prep
%setup -q -n %{name}-%{version}/upstream

%build

%cmake -DCMAKE_VERBOSE_MAKEFILE=ON -DBUILD_PYTHON=OFF -DBUILD_TESTS=OFF \
       -DBUILD_SHARED_LIBS=ON -DBUILD_EXAMPLES=OFF
make %{?_smp_mflags}

%install
%make_install

%pre

%post -n s2geometry -p /sbin/ldconfig

%postun -n s2geometry -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%{_libdir}/libs2.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/s2
%{_libdir}/libs2.so
%{_datadir}/s2

%changelog
* Sun Oct 20 2024 rinigus <rinigus.git@gmail.com> - 0.11.1-1
- update

* Sun Nov 15 2020 rinigus <rinigus.git@gmail.com> - 0.9.0-1
- initial packaging release for SFOS
