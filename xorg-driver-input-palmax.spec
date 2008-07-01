Summary:	X.org input driver for Palmax (TR88L803) touchscreen devices
Summary(pl.UTF-8):	Sterownik wejściowy X.org dla ekranów dotykowych Palmax (TR88L803)
Name:		xorg-driver-input-palmax
Version:	1.2.0
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-palmax-%{version}.tar.bz2
# Source0-md5:	9655d2235569c5a6ac321c6fb89a6f3b
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
BuildRequires:  rpmbuild(macros) >= 1.389
%requires_xorg_xserver_xinput
Requires:	xorg-xserver-server >= 1.0.99.901
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for Palmax (TR88L803) touchscreen devices. It
supports Palmax PD1000, Palmax PD1100 and in theory any other system
using a TR88L803 wired to a serial port.

%description -l pl.UTF-8
Sterownik wejściowy X.org dla ekranów dotykowych Palmax (TR88L803).
Obsługuje ekrany Palmax PD1000, Palmax PD1100 i teoretycznie dowolny
inny używający układu TR88L803 podłączonego do portu szeregowego.

%prep
%setup -q -n xf86-input-palmax-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/input/palmax_drv.so
%{_mandir}/man4/palmax.4*
