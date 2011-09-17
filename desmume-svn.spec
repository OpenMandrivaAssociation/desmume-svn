Name:			desmume-svn
%define longname	DeSmuME-SVN
%define stablename	desmume
%define stablelongname	DeSmuME
%define revision 	r4092
Version:		0.9.8.%{revision}
Release:		%mkrel 0

Summary:	A Nintendo DS emulator
License:	GPLv2+
Group:		Emulators
URL:		http://desmume.sourceforge.net/
Source0:	%{name}-%{revision}-1.tar.bz2
#Source1:	%{name}-%{version}-wx-headers.tar.bz2
Source10:	%{name}-48.png

# Modified .desktop files for svn build
Source20:	%{name}.desktop
Source21:	%{name}-glade.desktop
Source22:	wx%{name}.desktop

# Local patches to rename package
Patch0:		%{name}_name.patch
Patch1:		%{name}_cli_makefile.patch
Patch2:		%{name}_gtkglade_makefile.patch
Patch3:		%{name}_gtk_makefile.patch
Patch4:		%{name}_wx_makefile.patch

BuildRequires:	automake
BuildRequires:	autogen
BuildRequires:	autoconf
BuildRequires:	gtk2-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	gtkglext-devel
BuildRequires:	wxGTK2.8-devel
BuildRequires:	agg-devel
BuildRequires:	pcap-devel
BuildRequires:	desktop-file-utils
BuildRequires:	recode
BuildRequires:	intltool
BuildRequires:	libSDL-devel
BuildRequires:	libz-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-Revision

%package -n %{name}-glade
Summary:	A Nintendo DS emulator (Glade GUI version)
Group:		Emulators
License:	GPLv2+

%package -n %{name}-cli
Summary:	A Nintendo DS emulator (CLI version)
Group:		Emulators
License:	GPLv2+

%package -n wx%{name}
Summary:	A Nintendo DS emulator (wxWidgets GUI version)
Group:		Emulators
License:	GPLv2+

%description
DeSmuME is a Nintendo DS emulator running homebrew demos and commercial 
games... For the latter ones, you should own the games corresponding the 
roms you play with.

You can find a compatibility list here : http://desmume.org/?page_id=15

In this package is the GTK GUI version. 

It is a SVN build.

Warning:
If you use a 3d desktop, forget the GUI for now or disable AIGLX.
You can do this by setting Option "AIGLX" "off" in ServerFlags section.

This package is in PLF because of Mandriva policy regarding emulators.

%description -n %{name}-glade
DeSmuME is a Nintendo DS emulator running homebrew demos and commercial 
games... For the latter ones, you should own the games corresponding the 
roms you play with.

You can find a compatibility list here : http://desmume.org/?page_id=15

In this package is the GTK/Glade version, which includes a translation.

It is a SVN build.

Warning:
If you use a 3d desktop, forget the GUI for now or disable AIGLX.
You can do this by setting Option "AIGLX" "off" in ServerFlags section.

This package is in PLF because of Mandriva policy regarding emulators.

%description -n %{name}-cli
DeSmuME is a Nintendo DS emulator running homebrew demos and commercial 
games... For the latter ones, you should own the games corresponding the 
roms you play with.

You can find a compatibility list here : http://desmume.org/?page_id=15

In this package is the CLI version (without a GUI).

It is a SVN build.

This package is in PLF because of Mandriva policy regarding emulators.

%description -n wx%{name}
DeSmuME is a Nintendo DS emulator running homebrew demos and commercial
games... For the latter ones, you should own the games corresponding the
roms you play with.

You can find a compatibility list here : http://desmume.org/?page_id=15

In this package is the wxWidgets version.

It is a SVN build.

This package is in PLF because of Mandriva policy regarding emulators.


%prep
%setup -q -n desmume
#recode l1..u8 AUTHORS ChangeLog
#perl -pi -e 's|\r\n|\n|g' AUTHORS ChangeLog
#find src -name *.[ch]* -exec chmod 644 {} +
%patch0
%patch1
%patch2
%patch3
%patch4


%build
./autogen.sh
%configure2_5x --enable-wifi --enable-wxwidgets --enable-gdb-stub --enable-openal
#--enable-osmesa
%make

%install
rm -rf %{buildroot}
%makeinstall

#glade files
install -d -m 755 %{buildroot}/%{_datadir}/%{name}
install -m 644 src/gtk-glade/glade/* %{buildroot}/%{_datadir}/%{name}

# remove invalid glade file directory created by make install
rm -rf %{buildroot}/%{_datadir}/%{stablename}

# fix glade file names
mv %{buildroot}/%{_datadir}/%{name}/DeSmuMe.glade %{buildroot}/%{_datadir}/%{name}/%{longname}.glade
mv %{buildroot}/%{_datadir}/%{name}/DeSmuMe_Dtools.glade %{buildroot}/%{_datadir}/%{name}/%{longname}_Dtools.glade
mv %{buildroot}/%{_datadir}/%{name}/%{stablelongname}.xpm %{buildroot}/%{_datadir}/%{name}/%{longname}.xpm

#icons
install -d -m 755 %{buildroot}/%{_iconsdir}
install -m 644 %{SOURCE10} %{buildroot}/%{_iconsdir}/%{name}.png
install -m 644 %{SOURCE10} %{buildroot}/%{_iconsdir}/%{name}-glade.png
install -m 644 %{SOURCE10} %{buildroot}/%{_iconsdir}/wx%{name}.png

#rm -rf %{buildroot}/%{_datadir}/pixmaps

# Remove Desktop files and install new ones
rm %{buildroot}%{_datadir}/applications/%{stablename}.desktop 
rm %{buildroot}%{_datadir}/applications/%{stablename}-glade.desktop
rm %{buildroot}%{_datadir}/applications/wx%{stablename}.desktop
install -m 644 %{SOURCE20} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -m 644 %{SOURCE21} %{buildroot}%{_datadir}/applications/%{name}-glade.desktop
install -m 644 %{SOURCE22} %{buildroot}%{_datadir}/applications/wx%{name}.desktop

# fix the man pages file names
mv %{buildroot}/%{_mandir}/man1/%{stablename}.1 %{buildroot}/%{_mandir}/man1/%{name}.1
mv %{buildroot}/%{_mandir}/man1/%{stablename}-glade.1 %{buildroot}/%{_mandir}/man1/%{name}-glade.1
mv %{buildroot}/%{_mandir}/man1/%{stablename}-cli.1 %{buildroot}/%{_mandir}/man1/%{name}-cli.1

# and the .xpm file name
mv %{buildroot}/%{_datadir}/pixmaps/%{stablelongname}.xpm %{buildroot}/%{_datadir}/pixmaps/%{longname}.xpm

#xdg menus
desktop-file-install --vendor="" \
 --dir=%{buildroot}%{_datadir}/applications \
 %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install --vendor="" \
 --dir=%{buildroot}%{_datadir}/applications \
 %{buildroot}%{_datadir}/applications/%{name}-glade.desktop

desktop-file-install --vendor="" \
 --dir=%{buildroot}%{_datadir}/applications \
 %{buildroot}%{_datadir}/applications/wx%{name}.desktop

%find_lang %{name}

%if %mdkversion<200900
%post
%{update_menus}

%post -n %{name}-glade
%{update_menus}

%post -n wx%{name}
%{update_menus}

%postun
%{clean_menus}

%postun -n %{name}-glade
%{clean_menus}

%postun -n wx%{name}
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README README.LIN
%attr(0755,root,root) %{_bindir}/%{name}
%{_iconsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/desmume-svn.1.lzma
%{_datadir}/pixmaps/%{longname}.xpm

%files -n %{name}-glade -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README README.LIN
%attr(0755,root,root) %{_bindir}/%{name}-glade
%{_datadir}/%{name}
%{_iconsdir}/%{name}-glade.png
%{_datadir}/applications/%{name}-glade.desktop
%{_mandir}/man1/desmume-svn-glade.1.lzma

%files -n %{name}-cli
%defattr(-,root,root)
%doc AUTHORS ChangeLog README README.LIN
%attr(0755,root,root) %{_bindir}/%{name}-cli
%{_mandir}/man1/desmume-svn-cli.1.lzma

%files -n wx%{name}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README README.LIN
%attr(0755,root,root) %{_bindir}/wx%{name}
%{_iconsdir}/wx%{name}.png
%{_datadir}/applications/wx%{name}.desktop


%clean
rm -rf %{buildroot}

