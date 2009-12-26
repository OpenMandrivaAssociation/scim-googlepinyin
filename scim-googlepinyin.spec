%define snapdate 20091225

Summary: An SCIM port of android Google Pinyin IME
Name: scim-googlepinyin
Version: 0.1
Release: %mkrel -c %snapdate 1
License: ASL 2.0
Group: System/Internationalization
URL: http://code.google.com/p/scim-googlepinyin/
Source: %{name}-%{snapdate}.tar.bz2
Patch0: scim-googlepinyin-fix-werror.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: scim-devel >= 1.4.8
Requires: scim-client

%description
scim-googlepinyin is an SCIM port of google-pinyin on android platform.
It's basically a translation from its original java code to C++ counterpart.
Android google pinyin's core is not changed in porting, but this user
interface is slightly modified to simulate the bevaviour of GooglePinyin
on Windows.

%prep
%setup -qn %{name}
%patch0 -p0

%build
./autogen.sh
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -fr %buildroot/%{scim_plugins_dir}/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/scim/googlepinyin
%{_datadir}/scim/icons/google-pinyin_icon.png
%{scim_plugins_dir}/*/*.so
