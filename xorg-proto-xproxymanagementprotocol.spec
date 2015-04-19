Summary:	X Proxy Management Protocol headers
Summary(pl.UTF-8):	Pliki nagłówkowe protokołu X Proxy Management
Name:		xorg-proto-xproxymanagementprotocol
Version:	1.0.3
Release:	2
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/xproxymanagementprotocol-%{version}.tar.bz2
# Source0-md5:	9de22ca1522008c28fb03dfc41ba2d30
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Proxy Management Protocol headers.

The Proxy Management Protocol is an ICE based protocol that provides a
way for application servers to easily locate proxy services available
to them.

%description -l pl.UTF-8
Pliki nagłówkowe protokołu X Proxy Management.

Proxy Management Protocol to oparty na ICE protokół pozwalający
serwerom aplikacji lokalizować w prosty sposób dostępne dla nich
usługi proxy.

%package devel
Summary:	X Proxy Management Protocol headers
Summary(pl.UTF-8):	Pliki nagłówkowe protokołu X Proxy Management
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
X Proxy Management Protocol headers.

The Proxy Management Protocol is an ICE based protocol that provides a
way for application servers to easily locate proxy services available
to them.

%description devel -l pl.UTF-8
Pliki nagłówkowe protokołu X Proxy Management.

Proxy Management Protocol to oparty na ICE protokół pozwalający
serwerom aplikacji lokalizować w prosty sposób dostępne dla nich
usługi proxy.

%prep
%setup -q -n xproxymanagementprotocol-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog PM_spec README
%dir %{_includedir}/X11/PM
%{_includedir}/X11/PM/PM*.h
%{_pkgconfigdir}/xproxymngproto.pc
