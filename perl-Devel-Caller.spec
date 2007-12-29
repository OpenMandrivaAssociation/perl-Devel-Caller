%define module  Devel-Caller
%define name    perl-%{module}
%define version 2.02
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Meatier versions of caller()
License:        Artistic/GPL
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Devel/%{module}-%{version}.tar.bz2
BuildRequires:  perl(PadWalker)
BuildRequires:  perl-devel
Buildroot:      %{_tmppath}/%{name}-%{version}

%description
This module provides various improvements over the built-in caller()
primitive.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/*/*
%{perl_vendorarch}/Devel
%{perl_vendorarch}/auto/Devel

