# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

%define major 0
%define libname %mklibname cyaml %{major}
%define develname %mklibname cyaml -d

Name:		libcyaml
Version:	1.3.1
Release:	1
Summary:	LibCYAML is a C library for reading and writing structured YAML documents
License:	ISC
Group:		Development/Libraries/C and C++
URL:		https://github.com/tlsa/libcyaml
Source:		https://github.com/tlsa/libcyaml/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(yaml-0.1)

%description
LibCYAML is a C library for reading and writing structured YAML documents.

%package -n %{libname}
Summary:	LibCYAML is a C library for reading and writing structured YAML documents
Group:		System/Libraries

%description -n %{libname}
LibCYAML is a C library for reading and writing structured YAML documents.

%package -n %{develname}
Summary:	Development files for libcyaml
Group:		Development/Libraries/C and C++
Requires:	%{libname} = %{version}

%description -n %{develname}
This package holds the development files for libcyaml,
C library for reading and writing structured YAML documents.

%prep
%autosetup -n libcyaml-%{version} -p1

%build
%make_build

%install
%ifnarch %{ix86} %{arm}
%make_install PREFIX=%{_prefix} LIBDIR=lib64
%else
%make_install PREFIX=%{_prefix}
%endif
find %{buildroot} -type f -name "*.la" -delete -print


%files -n %{libname}
%{_libdir}/libcyaml.so.*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/libcyaml.a
%{_libdir}/pkgconfig/libcyaml.pc
%{_libdir}/libcyaml.so
