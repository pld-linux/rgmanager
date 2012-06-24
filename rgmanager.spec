Summary:	Open Source HA Resource Group Failover
Summary(pl.UTF-8):   Failover dla grupy zasobów o wysokiej dostępności
Name:		rgmanager
Version:	1.03.00
Release:	1
License:	GPL/LGPL
Group:		Applications/System
Source0:	ftp://sources.redhat.com/pub/cluster/releases/cluster-%{version}.tar.gz
# Source0-md5:	8eea23df70d2007c4fb8c234cfea49cf
URL:		http://sources.redhat.com/cluster/
BuildRequires:	ccs-devel
BuildRequires:	libxml2-devel
BuildRequires:	magma-devel >= 0:1.02.00
BuildRequires:	ncurses-devel
BuildRequires:	perl-base
Requires:	/sbin/findfs
Requires:	awk
Requires:	bash
Requires:	ccs
Requires:	grep
Requires:	magma
Requires:	mount
Requires:	net-tools
Requires:	sed
Obsoletes:	clumanager
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Resource Group Manager provides high availability of critical server
applications in the event of planned or unplanned system downtime.

%description -l pl.UTF-8
Resource Group Manager daje wysoką dostępność krytycznych aplikacji
serwerowych w przypadku planowanych lub nieplanowanych wyłączeń
serwera.

%prep
%setup -q -n cluster-%{version}
cd %{name}
%{__perl} -pi -e 's/-g /%{rpmcflags} /' src/{clulib,daemons}/Makefile
%{__perl} -pi -e 's,-g ,%{rpmcflags} -I/usr/include/ncurses ,' src/utils/Makefile

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
