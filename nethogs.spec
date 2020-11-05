%define debug_package %{nil}

Name:           nethogs
Version:        0.8.6
Release:        1
Summary:        Nethogs is a small 'net top' tool
License:        GPLv2+
URL:            https://github.com/raboof/nethogs/
Source0:        https://github.com/raboof/nethogs/archive/v%{version}.tar.gz

BuildRequires:  gcc-c++ libpcap-devel ncurses-devel

%description
NetHogs is a small 'net top' tool. Instead of breaking the traffic down per protocol or per subnet, like most tools do, it groups bandwidth by process.
NetHogs does not rely on a special kernel module to be loaded. If there's suddenly a lot of network traffic, you can fire up 
NetHogs and immediately see which PID is causing this. This makes it easy to identify programs that have gone wild and are su
ddenly taking up your bandwidth.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%make_build

%install
%make_install

%check
%make_build test

%files
%license COPYING
%doc README.md
%{_sbindir}/../local/sbin/nethogs
%{_mandir}/../../local/share/man/man8/nethogs.8*

%changelog
* Wed Nov 4 2020 zengwefeng<zwfeng@huawei.com> - 0.8.6-1
- Package init
