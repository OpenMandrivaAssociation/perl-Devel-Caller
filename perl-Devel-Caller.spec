%define upstream_name    Devel-Caller
%define upstream_version 2.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Meatier versions of caller()
License:    Artistic/GPL
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(PadWalker)
BuildRequires:  perl-devel

Buildroot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides various improvements over the built-in caller()
primitive.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%make test

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
