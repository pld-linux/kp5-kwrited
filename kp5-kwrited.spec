#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.27.11
%define		qtver		5.15.2
%define		kpname		kwrited
Summary:	kwrited
Name:		kp5-%{kpname}
Version:	5.27.11
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		Base
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	bc6fc49d2d2e0d1eee6fbbd276f795de
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-kpty-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Plasma daemon listening for wall and write messages.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/qt5/plugins/kf5/kded/kwrited.so
%{_datadir}/knotifications5/kwrited.notifyrc
