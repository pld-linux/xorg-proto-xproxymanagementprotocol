Summary:	PM protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu PM i pomocnicze
Name:		xorg-proto-xproxymanagementprotocol
Version:	1.0.2
Release:	2
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/xproxymanagementprotocol-%{version}.tar.bz2
# Source0-md5:	d28007a50976204960fc1fc07b4ca093
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PM protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu PM i pomocnicze.

%package devel
Summary:	PM protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu PM i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
PM protocol and ancillary headers.

%description devel -l pl.UTF-8
Nagłówki protokołu PM i pomocnicze.

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
%doc COPYING ChangeLog
%dir %{_includedir}/X11/PM
%{_includedir}/X11/PM/*.h
%{_pkgconfigdir}/xproxymngproto.pc
