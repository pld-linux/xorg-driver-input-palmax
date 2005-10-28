Summary:	X.org input driver for Palmax (TR88L803) touchscreen devices
Summary(pl):	Sterownik wej¶ciowy X.org dla ekranów dotykowych Palmax (TR88L803)
Name:		xorg-driver-input-palmax
Version:	1.0.0.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-input-palmax-%{version}.tar.bz2
# Source0-md5:	16c33f3fa271d4d79a0063dedce188c4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for Palmax (TR88L803) touchscreen devices. It
supports Palmax PD1000, Palmax PD1100 and in theory any other system
using a TR88L803 wired to a serial port.

%description -l pl
Sterownik wej¶ciowy X.org dla ekranów dotykowych Palmax (TR88L803).
Obs³uguje ekrany Palmax PD1000, Palmax PD1100 i teoretycznie dowolny
inny u¿ywaj±cy uk³adu TR88L803 pod³±czonego do portu szeregowego.

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
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/input/palmax_drv.so
%{_mandir}/man4/palmax.4x*
