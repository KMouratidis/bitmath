# sitelib for noarch packages
%if 0%{?rhel} && 0%{?rhel} <= 5
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%endif

Name: python-bitmath
Summary: For manipulating file size/transfer rates/capacity in different prefix units
Version: 1.0.2
Release: 2%{?dist}

Group: Development/Libraries
License: BSD
Source0: https://github.com/tbielawa/bitmath/archive/%{name}-%{version}-%{release}.tar.gz
Url: https://github.com/tbielawa/bitmath

BuildArch: noarch
BuildRequires: python2-devel

%description
bitmath simplifies many facets of interacting with file sizes in
various units. Examples include: converting between SI and NIST prefix
units (GiB to kB), converting between units of the same type (SI to
SI, or NIST to NIST), basic arithmetic operations (subtracting 42KiB
from 50GiB), and rich comparison operations (1024 Bytes == 1KiB).

In addition to the conversion and math operations, bitmath provides
human readable representations of values which are suitable for use in
interactive shells as well as larger scripts and applications.


%prep
%setup -n bitmath-%{version} -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --root=$RPM_BUILD_ROOT --record=python-bitmath-files.txt

%files -f python-bitmath-files.txt
%doc README.md LICENSE

%changelog
* Thu Mar 13 2014 Tim Bielawa <tbielawa@redhat.com> - 1.0.2-2
- Bump spec for proper Source0 versioning

* Thu Mar 13 2014 Tim Bielawa <tbielawa@redhat.com> - 1.0.2-1
- First real solid release with full functionality and documentation

* Tue Mar 11 2014 Tim Bielawa <tbielawa@redhat.com> - 1.0.0-1
- First release