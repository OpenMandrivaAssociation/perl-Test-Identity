%define upstream_name    Test-Identity
%define upstream_version 0.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Assert the referential identity of a reference
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Builder::Tester)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a single testing function, 'identical'. It asserts
that a given reference is as expected; that is, it either refers to the
same object or is 'undef'. It is similar to 'Test::More::is' except that it
uses 'refaddr', ensuring that it behaves correctly even if the references
under test are objects that overload stringification or numification.

It also provides better diagnostics if the test fails:

 $ perl -MTest::More=tests,1 -MTest::Identity -e'identical [], {}'
 1..1
 not ok 1
 #   Failed test at -e line 1.
 # Expected an anonymous HASH ref, got an anonymous ARRAY ref
 # Looks like you failed 1 test of 1.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


