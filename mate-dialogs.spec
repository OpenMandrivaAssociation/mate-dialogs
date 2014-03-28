%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Call GNOME dialog boxes from the command line
Name:		mate-dialogs
Version:	1.8.0
Release:	1
License:	LGPLv2+
Group:		Development/Other
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libnotify)

%description
Mate-dialogs allows you to display dialog boxes from the commandline and shell
scripts.

%prep
%setup -q
NOCONFIGURE=yes ./autogen.sh

%build
%configure2_5x

%make
										
%install
%makeinstall_std

%find_lang matedialog --with-gnome 
%find_lang %{name}
cat matedialog.lang >> %{name}.lang

%files -f %{name}.lang
%doc AUTHORS COPYING HACKING NEWS README THANKS TODO
%{_bindir}/matedialog
%dir %{_datadir}/matedialog
%{_datadir}/matedialog/*
%{_mandir}/man1/*

