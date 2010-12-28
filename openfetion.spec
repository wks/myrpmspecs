%define libname libofetion
%define cliprog cliofetion

Name:			openfetion
Version:		2.1.0
Release:		1%{?dist}
Summary:		A Fetion client written using GTK2+
Group:			Applications/Internet
License:		GPLv2+
URL:			http://basiccoder.com/openfetion
Source0:		http://ofetion.googlecode.com/files/%{name}-all-%{version}.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	libxml2-devel, gtk2-devel, gstreamer-devel, libnotify-devel
BuildRequires:	libXScrnSaver-devel, intltool, openssl-devel, sqlite-devel
BuildRequires:	gettext, NetworkManager-glib-devel, desktop-file-utils
BuildRequires:	cmake

%description
Openfetion is a Fetion client written using GTK2+,
based on Fetion v4 protocol.

%package -n %{name}-cli
Summary:		A command line Fetion client using libfetion
Group:			Applications/Internet

%description -n %{name}-cli
This is a command line Fetion client.  It can send
messages via the Fetion protocol.  It is based on the
libfetion library.

%package -n %{libname}
Summary:		Library files of Openfetion
Group:			Development/Libraries

%description -n %{libname}
This package contains the dynamic library of Openfetion,
which handles the network protocol and can be reused to 
create Fetion clients.

%package -n %{libname}-devel
Summary:		Development files for openfetion-lib
Group:			Development/Libraries
Requires:		%{libname} = %{version}-%{release}

%description -n %{libname}-devel
This package contains header files needed for developing 
software which uses %{libname}.


%prep
%setup -q -n %{name}-all-%{version}

%build
%cmake .

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/libofetion.a

desktop-file-install --delete-original \
  --dir ${RPM_BUILD_ROOT}/%{_datadir}/applications \
  ${RPM_BUILD_ROOT}/%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun
update-desktop-database %{_datadir}/applications &>/dev/null || :

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING LICENSE README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/resource/newmessage.wav
%{_datadir}/%{name}/skin/*
%{_datadir}/pixmaps/fetion.svg

%files -n %{name}-cli
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING LICENSE README
%{_bindir}/%{cliprog}

%files -n %{libname}
%defattr(-,root,root,-)
%{_datadir}/%{name}/resource/city.xml
%{_datadir}/%{name}/resource/province.xml
%{_libdir}/libofetion.so*

%files -n %{libname}-devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/pkgconfig/*

%changelog
* Tue Dec 28 2010 Kunshan Wang <wks1986@gmail.com> - 2.1.0-1
- Upgrade to 2.1.0
- Fixed some building commands since OpenFetion has switched to cmake
- Removed rpath removal code since it is already removed by cmake

* Tue Nov 16 2010 Liang Suilong <liangsuilong@gmail.com> - 2.0.2-2
- Clean up spec file
- Add BR: NetworkManager-glib-devel and desktop-file-utils

* Tue Nov 16 2010 Liang Suilong <liangsuilong@gmail.com> - 2.0.2-1
- Upgrade to 2.0.2

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

