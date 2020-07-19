#
# spec file for package libcyaml
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           libcyaml
Version:        1.1.0
Release:        0
Summary:        LibCYAML is a C library for reading and writing structured YAML documents
License:        ISC
Group:          Development/Libraries/C and C++
URL:            https://pyyaml.org/wiki/LibYAML
Source:         libcyaml-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  libyaml-devel

%description
LibCYAML is a C library for reading and writing structured YAML documents

%define lib_name libcyaml1

%package -n %{lib_name}
Summary:        LibCYAML is a C library for reading and writing structured YAML documents
Group:          System/Libraries

%description -n %{lib_name}
LibCYAML is a C library for reading and writing structured YAML documents.

%package devel
Summary:        Development files for libcyaml
Group:          Development/Libraries/C and C++
Requires:       %{lib_name} = %{version}

%description devel
This package holds the development files for libcyaml,
C library for reading and writing structured YAML documents.

%prep
%setup -q -n libcyaml-%{version}

%build
%make_build

%install
%make_install PREFIX=%{_prefix} LIBDIR=lib64
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%post   -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%{_libdir}/libcyaml.so.*

%files devel
%{_includedir}/*
%{_libdir}/libcyaml.a
%{_libdir}/pkgconfig/libcyaml.pc
%{_libdir}/libcyaml.so

%changelog
