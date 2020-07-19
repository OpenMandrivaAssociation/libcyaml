%global debug_package %{nil}

%define oname libcyaml

Name:           cyaml
Version:        1.1.0
Release:        1
Summary:        LibCYAML is a C library for reading and writing structured YAML documents
License:        ISC
Group:          Development/Libraries/C and C++
URL:            https://github.com/tlsa/libcyaml
Source:         https://github.com/tlsa/libcyaml/archive/v%{version}/%{oname}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(yaml-0.1)

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


%files -n %{lib_name}
%{_libdir}/libcyaml.so.*

%files devel
%{_includedir}/*
%{_libdir}/libcyaml.a
%{_libdir}/pkgconfig/libcyaml.pc
%{_libdir}/libcyaml.so
