Name:           gnome-flashback
Version:        3.22.1
Release:        1%{?dist}
Summary:        Classic GNOME session

License:        GPLv3+
URL:            https://wiki.gnome.org/Projects/GnomeFlashback
Source0:        http://download.gnome.org/sources/%{name}/3.22/%{name}-%{version}.tar.xz
Patch1:         0001-ibus-input-purpose-undefined.patch

BuildRequires:  gnome-common
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.3
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.10
BuildRequires:  pkgconfig(gnome-bluetooth-1.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.22.2
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.22.0
BuildRequires:  pkgconfig(ibus-1.0) >= 1.5.3
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.30
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(polkit-agent-1) >= 0.112
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.112
BuildRequires:  pkgconfig(upower-glib) >= 0.99.4
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi) >= 1.7.9
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(xrandr)
Requires:       gnome-panel
Requires:       gnome-applets
Requires:       metacity
Requires:       gnome-keyring
Requires:       gnome-screensaver
Requires:       gnome-settings-daemon
Requires:       gnome-session
Requires:       network-manager-applet

%description
GNOME Flashback is a session for GNOME 3 which was initially called
"GNOME Fallback". It provides a similar user experience to the GNOME 2.x
series sessions. The differences to the MATE project is that GNOME
Flashback uses Gtk+3 and tries to follow the current GNOME development
by integrating recent changes of the GNOME libraries.


%prep
%setup -q
%patch1 -p1


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}


%postun
if [ $1 -eq 0 ] ; then
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files -f %{name}.lang
%doc COPYING NEWS
%{_sysconfdir}/xdg/autostart/gnome-flashback-nm-applet.desktop
%{_sysconfdir}/xdg/autostart/gnome-flashback-screensaver.desktop
%{_sysconfdir}/xdg/menus/gnome-flashback-applications.menu
%{_bindir}/gnome-flashback
%{_libexecdir}/gnome-flashback-compiz
%{_libexecdir}/gnome-flashback-metacity
%{_datadir}/applications/gnome-flashback-init.desktop
%{_datadir}/applications/gnome-flashback.desktop
%{_datadir}/desktop-directories/X-GNOME-Flashback-Settings.directory
%{_datadir}/desktop-directories/X-GNOME-Flashback-Settings-System.directory
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-flashback.gschema.xml
%{_datadir}/gnome-session/sessions/gnome-flashback-compiz.session
%{_datadir}/gnome-session/sessions/gnome-flashback-metacity.session
%{_datadir}/xsessions/gnome-flashback-compiz.desktop
%{_datadir}/xsessions/gnome-flashback-metacity.desktop


%changelog
* Tue Aug 29 2017 Timothy Lusk <tlusk@carbonblack.com> - 3.22.1-1
- Version bump for GNOME Flashback 3.22.

* Thu Dec 17 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.14.0-7
- Add autostart for gnome-screensaver and nm-applet

* Tue Jul 14 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.14.0-6
- Add polkit-gnome autostart

* Sun Jul 12 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.14.0-5
- Backport upstream fix for BGO#738562

* Fri Feb 27 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.14.0-4
- Fix for BGO#738562

* Mon Feb 23 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.14.0-3
- Requires: gnome-screensaver

* Tue Feb 10 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.14.0-2
- Fix deps

* Mon Feb 02 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.14.0-1
- Update for GNOME 3.14.

* Mon Jan 12 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.10.0-1
- Initial release.
