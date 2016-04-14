Name:           gnome-flashback
Version:        3.20.0
Release:        1%{?dist}
Summary:        Classic GNOME session

License:        GPLv3+
URL:            https://wiki.gnome.org/Projects/GnomeFlashback
Source0:        http://download.gnome.org/sources/%{name}/3.20/%{name}-%{version}.tar.xz

BuildRequires:  gnome-common
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.19.5
BuildRequires:  pkgconfig(gnome-bluetooth-1.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.12.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.12.0
BuildRequires:  pkgconfig(ibus-1.0) >= 1.5.2
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.13
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(polkit-agent-1) >= 0.97
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.97
BuildRequires:  pkgconfig(upower-glib) >= 0.99.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(xrandr)
Requires:       gnome-panel
Requires:       gnome-applets
Requires:       metacity
Requires:       notification-daemon
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
* Thu Apr 14 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 3.20.0-1
- new version for GNOME Flashback 3.20.

* Thu Oct 15 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Fri Oct 02 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.18.0-1
- Update for GNOME Flashback 3.18.

* Mon Aug 24 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.17.2-2
- Fix crash in display-config (BGO#753927)

* Wed Jul 15 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.17.2-1
- Unstable version bump

* Wed Jul 15 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.16.1-3
- Add polkit-gnome autostart

* Wed Jul 15 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.16.1-2
- Add upstream fix for BGO#738562

* Wed Jul 15 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.16.1-1
- Update for GNOME 3.16.

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
