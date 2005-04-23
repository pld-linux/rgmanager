Summary:	Open Source HA Resource Group Failover
Summary(pl):	Failover dla grupy zasobów o wysokiej dostêpno¶ci
Name:		rgmanager
Version:	1.9.30
Release:	1
License:	GPL/LGPL
Group:		Applications/System
Source0:	http://people.redhat.com/cfeist/cluster/tgz/%{name}-%{version}.tar.gz
# Source0-md5:	89d855b0159d03b4e03107d9678178aa
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
%setup -q

%{__perl} -pi -e 's/-g /%{rpmcflags} /' src/{clulib,daemons}/Makefile
%{__perl} -pi -e 's,-g ,%{rpmcflags} -I/usr/include/ncurses ,' src/utils/Makefile

%build
./configure
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO errors.txt
%attr(755,root,root) %{_sbindir}/*
#%attr(754,root,root) /etc/rc.d/init.d/rgmanager
%attr(755,root,root) %{_datadir}/cluster
%{_mandir}/man8/*
