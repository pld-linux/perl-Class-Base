#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Base
Summary:	Class::Base - useful base class for deriving other modules
Summary(pl.UTF-8):	Class::Base - klasa bazowa przydatna do tworzenia innych modułów
Name:		perl-Class-Base
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	526cc491f2a02991fce061bcc13e2fa8
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a simple base class from which other modules
can be derived, thereby inheriting a number of useful methods such as
new(), init(), params(), clone(), error() and debug().

%description -l pl.UTF-8
Moduł ten zawiera implementację prostej klasy bazowej, która może
służyć do wywiedzenia z niej innych modułów, które tym samym
odziedziczą takie przydatne metody, jak new(), init(), params(),
clone(), error() i debug().

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes TODO
%{perl_vendorlib}/Class/*.pm
%{_mandir}/man3/*
