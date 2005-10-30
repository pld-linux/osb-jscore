#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	GTK-Webcore Javascript Core library
Name:		osb-jscore
Version:	0.5.0
Release:	0.1
License:	GPL?
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/gtk-webcore/%{name}-%{version}.tar.gz
# Source0-md5:	969cda923c419e35a319911b30b1d4b8
URL:		http://gtk-webcore.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK Webcore Core library

%package devel
Summary:	Development libraries and header files for osb-jscore library
Group:		Development/Libraries
#Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the development libraries and header
files for osb-jscore.

%package static
Summary:	Static osb-jscore library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static osb-jscore library.

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
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_libdir}/libjscore.so.*.*

%files devel
%{_includedir}/osb/JavaScriptCore
%{_libdir}/libjscore.so
%{_libdir}/libjscore.la
%{_libdir}/pkgconfig/osb-jscore.pc

%files static
%{_libdir}/libjscore.a
