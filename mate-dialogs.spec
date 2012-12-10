Summary:	Call GNOME dialog boxes from the command line
Name:		mate-dialogs
Version:	1.4.0
Release:	1
License:	LGPLv2+
Group:		Development/Other
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires:	docbook-dtd412-xml
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libmatenotify)
BuildRequires:	pkgconfig(mate-doc-utils)

%description
Mate-dialogs allows you to display dialog boxes from the commandline and shell
scripts.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-scrollkeeper
%make
										
%install
%makeinstall_std

# MD this file conflicts with zenity
rm -f %{buildroot}%{_bindir}/gdialog

%find_lang matedialog --with-gnome
%find_lang %{name}
cat matedialog.lang >> %{name}.lang

%files -f %{name}.lang
%doc AUTHORS COPYING HACKING NEWS README THANKS TODO
%{_bindir}/matedialog
%dir %{_datadir}/matedialog
%{_datadir}/matedialog/*
%{_mandir}/man1/*

# this is a new help dir for mate and should be removed once 
# properly found with find-lang.sh
%{_datadir}/mate/help/*



%changelog
* Thu Aug 02 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.4.0-1
+ Revision: 811578
- new version 1.4.0

* Tue Jun 12 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-3
+ Revision: 805260
- rebuild really deleting gdialog now

* Mon Jun 11 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-2
+ Revision: 804434
- rebuild removing conflicting file gdialog with zenity

* Fri Jun 01 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-1
+ Revision: 801805
- imported package mate-dialogs

