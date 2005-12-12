Summary:	Open Source HA Resource Group Failover
Summary(pl):	Failover dla grupy zasobów o wysokiej dostêpno¶ci
Name:		rgmanager
Version:	1.01.00
Release:	1
License:	GPL/LGPL
Group:		Applications/System
Source0:	ftp://sources.redhat.com/pub/cluster/releases/cluster-%{version}.tar.gz
# Source0-md5:	e98551b02ee8ed46ae0ab8fca193d751
URL:		http://sources.redhat.com/cluster/
BuildRequires:	ccs-devel
BuildRequires:	magma-devel
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRequires:	perl-base
Requires:	awk
Requires:	bash
Requires:	grep
Requires:	sed
Requires:	ccs
Requires:	magma
Requires:	net-tools
Requires:	mount
Requires:	/sbin/findfs
Obsoletes:	clumanager
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Resource Group Manager provides high availability of critical server
applications in the event of planned or unplanned system downtime.

%description
Resource Group Manager daje wysok± dostêpno¶æ krytycznych aplikacji
serwerowych w przypadku planowanych lub nieplanowanych wy³±czeñ
serwera.

%prep
%setup -q -n cluster-%{version}
cd %{name}
%{__perl} -pi -e 's/-g /%{rpmcflags} /' src/{clulib,daemons}/Makefile
%{__perl} -pi -e 's,-g ,%{rpmcflags} -I%{_includedir}/ncurses ,' src/utils/Makefile

%build
cd %{name}
./configure
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}/{AUTHORS,ChangeLog,README,TODO,errors.txt}
%attr(755,root,root) %{_sbindir}/*
#%attr(754,root,root) /etc/rc.d/init.d/rgmanager
%attr(755,root,root) %{_datadir}/cluster
%{_mandir}/man8/*
