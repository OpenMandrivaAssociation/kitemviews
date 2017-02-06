%define major 5
%define libname %mklibname KF5ItemViews %{major}
%define devname %mklibname KF5ItemViews -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kitemviews
Version:	5.31.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 item view library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: cmake(Qt5LinguistTools)
Requires: %{libname} = %{EVRD}

%description
The ItemViews framework contains data views on top of
QAbstractItemView that help in common tasks, such as sorting, proxying
and filtering.

ItemViews contains useful classes such as a view for checkable or
selectable items, recursive filtering and breadcrumb selection.

%package -n %{libname}
Summary: The KDE Frameworks 5 item view library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
The ItemViews framework contains data views on top of
QAbstractItemView that help in common tasks, such as sorting, proxying
and filtering.

ItemViews contains useful classes such as a view for checkable or
selectable items, recursive filtering and breadcrumb selection.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

The ItemViews framework contains data views on top of
QAbstractItemView that help in common tasks, such as sorting, proxying
and filtering.

ItemViews contains useful classes such as a view for checkable or
selectable items, recursive filtering and breadcrumb selection.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

L="`pwd`/kitemviews%{major}_qt.lang"
cd %{buildroot}
for i in .%{_datadir}/locale/*/LC_MESSAGES/*.qm; do
	LNG=`echo $i |cut -d/ -f5`
	echo -n "%lang($LNG) " >>$L
	echo $i |cut -b2- >>$L
done

%files -f kitemviews%{major}_qt.lang

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5ItemViews
%{_libdir}/qt5/mkspecs/modules/*
