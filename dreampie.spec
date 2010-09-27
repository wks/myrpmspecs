# Turn off the brp-python-bytecompile script for manual bytecode compile.
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile!true!g')

Name:		dreampie
Version:	1.1
Release:	1%{?dist}
Summary:	An interactive Python shell written in Python with PyGTK

Group:		Development/Libraries
License:	GPLv3
URL:		http://dreampie.sourceforge.net/
Source0:	http://launchpad.net/dreampie/trunk/%{version}/+download/%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:	noarch
Requires:	pygtk2
BuildRequires:	python2-devel
BuildRequires:	python3-devel
BuildRequires:	pygtk2-devel

%description
DreamPie is a Python shell which is designed to be reliable and fun.

DreamPie was designed from the ground up to bring you a great interactive Python experience:

    * DreamPie features a new concept for an interactive shell: the window is divided into the history box, which lets you view previous commands and their output, and the code box, where you write your code. This allows you to edit any amount of code, just like in your favorite editor, and execute it when it's ready. You can also copy code from anywhere, edit it and run it instantly.
    * The Copy code only command will copy the code you want to keep, so you can save it in a file. The code is already formatted nicely with a four-space indentation.
    * Features automatic completion of attributes and file names.
    * Automatically displays function arguments and documentation.
    * Keeps your recent results in the result history, for later user.
    * Can automatically fold long outputs, so you can concentrate on what's important.
    * Lets you save the history of the session as an HTML file, for future reference. You can then load the history file into DreamPie, and quickly redo previous commands.
    * Automatically adds parentheses and optionally quotes when you press space after functions and methods. For example, execfile<space>→execfile(""), sin<space>→sin().
    * Supports interactive plotting with matplotlib. (You have to set "interactive: True" in the matplotlibrc file for this to work.)
    * Supports Python 2.5, 2.6, 2.7, Jython 2.5, IronPython 2.6 and Python 3.1.
    * Works on Windows, Linux and Mac. (Mac support requires MacPorts.)
    * Extremely fast and responsive.
    * Free software licensed under GPL version 3.


%prep
%setup -q


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

# Dreampie yields code for both Python 2 and Python 3.  Byte compile should
# be handled manually.
# Manually invoke the python byte compile macro for each path that needs byte
# compilation.
%py_byte_compile %{__python}  %{buildroot}%{_datadir}/dreampie/subp-py2/dreampielib
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/dreampie/subp-py3/dreampielib
 

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING LICENSE-PSF PKG-INFO README 
%{python_sitelib}/*
%{_bindir}/dreampie
%{_datadir}/*

%changelog
* Tue Aug 24 2010 Kunshan Wang <wks1986@gmail.com> 1.1-1
- Rewritten to comform the Fedora packaging guidelines.

* Mon May 17 2010 Kunshan Wang <wks1986@gmail.com> 1.0.2-0.wks.1
- Initial RPM release

