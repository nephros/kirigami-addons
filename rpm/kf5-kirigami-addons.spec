Name: opt-kf5-kirigami2-addons
Version:        0.7.2
Release:        1%{?dist}
Epoch:          1
License:        LGPLv3
Summary:        Convergent visual components ("widgets") for Kirigami-based applications
Url:            https://invent.kde.org/libraries/kirigami-addons
Source0: %{name}-%{version}.tar.bz2

%{?opt_kf5_default_filter}

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: opt-kf5-rpm-macros
BuildRequires: opt-kf5-ki18n-devel
BuildRequires: opt-kf5-kirigami2-devel

BuildRequires:  opt-qt5-qtbase-devel
BuildRequires:  opt-qt5-qtdeclarative-devel
BuildRequires:  opt-qt5-qtquickcontrols2-devel

%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires: opt-qt5-qtdeclarative
Requires: opt-qt5-qtquickcontrols2
Requires: opt-kf5-kirigami2

%description
A set of "widgets" i.e visual end user components along with a
code to support them. Components are usable by both touch and
desktop experiences providing a native experience on both, and
look native with any QQC2 style (qqc2-desktop-theme, Material
or Plasma).

%package dateandtime
Summary:        Date and time add-on for the Kirigami framework
%{?opt_kf5_default_filter}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description dateandtime
Date and time Kirigami addons, which complements other
software like Kclock.

%package treeview
Summary:         Tree view add-on for the Kirigami framework
%{?opt_kf5_default_filter}
Requires:        %{name}%{?_isa} = %{version}-%{release}
%description treeview
Tree view Kirigami addon, which is useful for listing files.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../
%make_build

popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%find_lang %{orig_name} --all-name

%files -f %{orig_name}.lang
%doc README.md
%license LICENSES/
%dir %{_opt_kf5_qmldir}/org/kde
%dir %{_opt_kf5_qmldir}/org/kde/kirigamiaddons
%{_opt_kf5_libdir}/qt5/qml/org/kde/kirigamiaddons/*
%{_opt_kf5_libdir}/cmake/KF5KirigamiAddons/*


%files dateandtime
%{_opt_kf5_qmldir}/org/kde/kirigamiaddons/dateandtime/

%files treeview
%{_opt_kf5_qmldir}/org/kde/kirigamiaddons/treeview/
