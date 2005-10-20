Summary:	PM protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u PM i pomocnicze
Name:		xorg-proto-xproxymanagementprotocol
Version:	1.0.1
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/proto/xproxymanagementprotocol-%{version}.tar.bz2
# Source0-md5:	2951543a1d5687d54db825bac2bffaed
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PM protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u PM i pomocnicze.

%package devel
Summary:	PM protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u PM i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
PM protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u PM i pomocnicze.

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
%{_includedir}/X11/PM/*.h
%{_pkgconfigdir}/xproxymngproto.pc
