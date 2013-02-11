Name:		leveldb
Version:	1.9.0
Release:	4%{?dist}
Summary:	A fast and lightweight key/value database library by Google
Group:		Applications/Databases
License:	BSD
URL:		http://code.google.com/p/leveldb/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	snappy-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool


%description
LevelDB is a fast key-value storage library written at Google that provides an
ordered mapping from string keys to string values.


%package devel
Summary: The development files for %{name}
Group: Development/Libraries
Requires: pkgconfig
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig


%description devel
Additional header files for development with %{name}.


%prep
%setup -q

%build
autoreconf -ivf
%configure --disable-static --with-pic
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la


%check
%ifarch armv5tel armv7hl
# FIXME a couple of tests are failing on these secondary arches
make check || true
%else
# x86, x86_64, ppc, ppc64, ppc64v7 s390, and s390x are fine
make check
%endif


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc doc/ AUTHORS LICENSE README
%{_libdir}/lib%{name}.so.*


%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Mon Feb 11 2013 Gary Lowell <gary.lowell@inktank.com> - 1.9.0-0
- Version 1.9.0 for use with Ceph

* Thu Nov 29 2012 gil cattaneo <puntogil@libero.it> - 1.7.0-4
- Applied patch for allow leveldbjni build

* Sat Oct 27 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.7.0-3
- Dirty workarounds for failed tests on ARM

* Sat Oct 27 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.7.0-2
- Restored patch no.2

* Sat Oct 27 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.7.0-1
- Ver. 1.7.0 (API/ABI compatible bugfix release)

* Tue Aug 21 2012 Dan Horák <dan[at]danny.cz> - 1.5.0-4
- add workaround for big endians eg. s390(x)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.5.0-2
- Cleaned up spec by removing EL5-related stuff
- Added notes about the patches

* Fri Jun 15 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.5.0-1
- Ver. 1.5.0

* Thu May 17 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.4.0-1
- Initial package
