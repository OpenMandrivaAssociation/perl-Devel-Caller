%define module  Devel-Caller
%define name    perl-%{module}
%define version 0.11
%define release %mkrel 2

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Meatier versions of caller()
License:        Artistic/GPL
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Devel/%{module}-%{version}.tar.bz2
BuildRequires:  perl(Module::Build)
Buildroot:      %{_tmppath}/%{name}-%{version}

%description
This module provides various improvements over the built-in caller()
primitive.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"
%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_mandir}/*/*
%{perl_vendorarch}/Devel
%{perl_vendorarch}/auto/Devel

