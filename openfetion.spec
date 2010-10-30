Name:       openfetion
Version:    2.0
Release:    2%{?dist}
Summary:    A Fetion client written using GTK+ 2

Group:      Applications/Internet
License:    GPLv2+
URL:        http://basiccoder.com/openfetion
Source0:    openfetion-2.0.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  libxml2-devel, gtk2-devel, gstreamer-devel, libnotify-devel
BuildRequires:  libXScrnSaver-devel, intltool, NetworkManager-devel
BuildRequires:  gettext

Requires:   %{name}-lib = %{version}-%{release}

%package lib
Summary:    Library files of Openfetion
Group:      Development/Libraries
BuildRequires:  libxml2-devel, openssl-devel, sqlite-devel

%package lib-devel
Summary:    Development files for openfetion-lib
Group:      Development/Libraries
Requires:   %{name}-lib = %{version}-%{release}
Requires:   libxml2-devel, openssl-devel, sqlite-devel


%description
Openfetion is a Fetion client written using GTK+ 2, based on Fetion v4 protocol.

%description lib
This package contains the dynamic library of Openfetion, which handles the network
protocol and can be reused to create Fetion clients.

%description lib-devel
This package contains header files needed for developing software which uses
Openfetion.


%prep
%setup -q

%build
%configure --disable-static

# Remove bogus rpath
sed -i \
	-e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
	-e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -Dpm 644 skin/fetion.svg $RPM_BUILD_ROOT%{_datadir}/pixmaps/fetion.svg
rm $RPM_BUILD_ROOT%{_libdir}/libofetion.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post lib -p /sbin/ldconfig

%postun lib -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING LICENSE README
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/resource/newmessage.wav
%{_datadir}/%{name}/skin/*
%{_datadir}/pixmaps/fetion.svg

%files lib
%defattr(-,root,root,-)
%{_datadir}/%{name}/resource/city.xml
%{_datadir}/%{name}/resource/province.xml
%{_libdir}/libofetion.so*

%files lib-devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/pkgconfig/*

%changelog
* Mon Oct 25 2010 Kunshan Wang <wks1986@gmail.com> - 2.0-2
- Added the missing BuildDep NetworkManager-devel

* Mon Oct 25 2010 Kunshan Wang <wks1986@gmail.com> - 2.0-1
- Upgrade to 2.0

* Mon Sep 27 2010 Kunshan Wang <wks1986@gmail.com> - 1.9-1
- Upgrade to 1.9

* Thu Aug 28 2010 Kunshan Wang <wks1986@gmail.com> - 1.8-1.svnr55
- Upgrade to SVN revision 55 

* Sun Jun 13 2010 Robin Lee <robinlee.sysu@gmail.com> - 1.6.1-2
- Spec file massively renewed with reference to the one from Kunshan Wang
  <wks1986@gmail.com>

* Sat Jun 12 2010 Xuqing Kuang <xuqingkuang@gmail.com> - 1.6.1-1
- Initial build.

