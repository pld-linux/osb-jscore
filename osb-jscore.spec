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
%if %{with initscript}
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	/sbin/chkconfig
%endif
#BuildRequires:	-
#BuildRequires:	autoconf
#BuildRequires:	automake
#BuildRequires:	libtool
#Requires(postun):	-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires:	-
#Provides:	group(foo)
#Provides:	user(foo)
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
#BuildArch:	noarch
#ExclusiveArch:	%{ix86}
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
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__gettextize}
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
#cp -f /usr/share/automake/config.sub .
%configure
%{__make}

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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

%if 0
# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%endif

# initscript and its config
%if %{with initscript}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%endif

#%{_examplesdir}/%{name}-%{version}

%if %{with subpackage}
%files subpackage
%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
%endif
