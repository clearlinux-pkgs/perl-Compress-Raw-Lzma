#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 5424026
#
Name     : perl-Compress-Raw-Lzma
Version  : 2.213
Release  : 54
URL      : https://cpan.metacpan.org/authors/id/P/PM/PMQS/Compress-Raw-Lzma-2.213.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PM/PMQS/Compress-Raw-Lzma-2.213.tar.gz
Summary  : 'Low-Level Perl Interface to lzma compression library'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Compress-Raw-Lzma-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Pod::Markdown)
BuildRequires : xz-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Compress-Raw-Lzma
Version 2.213
28 August 2024
This program is free software; you can redistribute it
and/or modify it under the same terms as Perl itself.

%package dev
Summary: dev components for the perl-Compress-Raw-Lzma package.
Group: Development
Provides: perl-Compress-Raw-Lzma-devel = %{version}-%{release}
Requires: perl-Compress-Raw-Lzma = %{version}-%{release}

%description dev
dev components for the perl-Compress-Raw-Lzma package.


%package perl
Summary: perl components for the perl-Compress-Raw-Lzma package.
Group: Default
Requires: perl-Compress-Raw-Lzma = %{version}-%{release}

%description perl
perl components for the perl-Compress-Raw-Lzma package.


%prep
%setup -q -n Compress-Raw-Lzma-2.213
cd %{_builddir}/Compress-Raw-Lzma-2.213
pushd ..
cp -a Compress-Raw-Lzma-2.213 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Compress::Raw::Lzma.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
