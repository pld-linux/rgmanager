# NOTE: obsoleted by -rgmanager subpackage from cluster.spec (3.x)
Summary:	Open Source HA Resource Group Failover
Summary(pl.UTF-8):	Failover dla grupy zasobów o wysokiej dostępności
Name:		rgmanager
Version:	2.03.11
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	ftp://sources.redhat.com/pub/cluster/releases/cluster-%{version}.tar.gz
# Source0-md5:	712b9f583472d1de614641bc0f4a0aaf
Patch0:		cluster-kernel.patch
URL:		http://sources.redhat.com/cluster/
BuildRequires:	ccs-devel >= 2.03.11
BuildRequires:	cman-devel >= 2.03.11
BuildRequires:	dlm-devel >= 2.03.11
BuildRequires:	libxml2-devel >= 2
BuildRequires:	ncurses-devel
BuildRequires:	perl-base
BuildRequires:	slang-devel
Requires:	/sbin/findfs
Requires:	awk
Requires:	bash
Requires:	ccs >= 2.03.11
Requires:	cman-libs >= 2.03.11
Requires:	dlm-libs >= 2.03.11
Requires:	grep
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
%patch -P0 -p1

# there are some unused variables
%{__perl} -pi -e 's/-Werror //' %{name}/src/clulib/Makefile
%{__perl} -pi -e 's/-Werror //' %{name}/src/daemons/Makefile
%{__perl} -pi -e 's/-Werror //' %{name}/src/utils/Makefile
%{__perl} -pi -e 's/-lncurses/-lncurses -ltinfo/' %{name}/src/utils/Makefile

%build
./configure \
	--cc="%{__cc}" \
	--cflags="%{rpmcflags} -Wall" \
	--ldflags="%{rpmldflags}" \
	--incdir=%{_includedir} \
	--ncursesincdir=%{_includedir}/ncurses \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--mandir=%{_mandir} \
	--prefix=%{_prefix} \
	--sbindir=%{_sbindir} \
	--without_gfs \
	--without_gfs2 \
	--without_gnbd \
	--without_kernel_modules
# -j1 because of missing dependency in clulib
%{__make} -C %{name} -j1 \
	NCURSES_LDFLAGS="-lncurses -ltinfo"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C %{name} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}/{ChangeLog,README,errors.txt}
%attr(755,root,root) %{_sbindir}/clubufflush
%attr(755,root,root) %{_sbindir}/clufindhostname
%attr(755,root,root) %{_sbindir}/clulog
%attr(755,root,root) %{_sbindir}/clunfslock
%attr(755,root,root) %{_sbindir}/clurgmgrd
%attr(755,root,root) %{_sbindir}/clurmtabd
%attr(755,root,root) %{_sbindir}/clustat
%attr(755,root,root) %{_sbindir}/clusvcadm
%attr(755,root,root) %{_sbindir}/rg_test
#%attr(754,root,root) /etc/rc.d/init.d/rgmanager
%attr(755,root,root) %{_datadir}/cluster
%{_mandir}/man8/clubufflush.8*
%{_mandir}/man8/clufindhostname.8*
%{_mandir}/man8/clulog.8*
%{_mandir}/man8/clurgmgrd.8*
%{_mandir}/man8/clurmtabd.8*
%{_mandir}/man8/clustat.8*
%{_mandir}/man8/clusvcadm.8*
