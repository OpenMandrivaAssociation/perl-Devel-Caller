%define upstream_name    Devel-Caller
%define upstream_version 2.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    Meatier versions of caller()
License:    Artistic/GPL
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Devel/Devel-Caller-%{upstream_version}.tar.gz

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.50.0-5
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 2.50.0-4
+ Revision: 681395
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.50.0-3mdv2011.0
+ Revision: 555790
- rebuild for perl 5.12

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.50.0-2mdv2011.0
+ Revision: 555229
- rebuild

* Fri Apr 09 2010 Jérôme Quelin <jquelin@mandriva.org> 2.50.0-1mdv2010.1
+ Revision: 533384
- update to 2.05

* Wed Feb 17 2010 Jérôme Quelin <jquelin@mandriva.org> 2.40.0-1mdv2010.1
+ Revision: 506945
- update to 2.04

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 2.30.0-1mdv2010.0
+ Revision: 406979
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.03-3mdv2009.0
+ Revision: 256616
- rebuild

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.03-1mdv2008.1
+ Revision: 152831
- update to new version 2.03

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 2.02-2mdv2008.1
+ Revision: 152059
- rebuild

* Sat Dec 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.02-1mdv2008.1
+ Revision: 139199
- update to new version 2.02

* Fri Dec 28 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.01-1mdv2008.1
+ Revision: 138799
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-2mdv2008.0
+ Revision: 88427
- rebuild


* Wed Aug 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2007.0
- New version 0.11
- rpmbuildupdate aware
- fix directory ownership
- Module::Build-based build

* Sat Mar 25 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.09-2mdk
- Add BuildRequires

* Fri Mar 24 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.09-1mdk
- First Mandriva release


