Summary:	GTK-Webcore Javascript Core library
Summary(pl.UTF-8):	Główna biblioteka Javascriptu dla GTK-Webcore
Name:		osb-jscore
Version:	0.5.0
Release:	0.1
License:	LGPL v2+
Group:		Libraries
Source0:	http://dl.sourceforge.net/gtk-webcore/%{name}-%{version}.tar.gz
# Source0-md5:	969cda923c419e35a319911b30b1d4b8
URL:		http://gtk-webcore.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK Webcore Javascript Core library.

%description -l pl.UTF-8
Główna biblioteka Javascriptu dla GTK-Webcore.

%package devel
Summary:	Header files for osb-jscore library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki osb-jscore
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This is the package containing the header files for osb-jscore.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki osb-jscore.

%package static
Summary:	Static osb-jscore library
Summary(pl.UTF-8):	Statyczna biblioteka osb-jscore
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static osb-jscore library.

%description static -l pl.UTF-8
Statyczna biblioteka osb-jscore.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README THANKS
%attr(755,root,root) %{_libdir}/libjscore.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjscore.so
%{_libdir}/libjscore.la
%dir %{_includedir}/osb
%{_includedir}/osb/JavaScriptCore
%{_pkgconfigdir}/osb-jscore.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libjscore.a
