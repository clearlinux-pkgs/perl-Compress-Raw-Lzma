#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Compress-Raw-Lzma
Version  : 2.082
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/P/PM/PMQS/Compress-Raw-Lzma-2.082.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PM/PMQS/Compress-Raw-Lzma-2.082.tar.gz
Summary  : 'Low-Level Interface to lzma compression library'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Compress-Raw-Lzma-lib = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : xz-dev

%description
Compress-Raw-Lzma
Version 2.082
15 April 2018
This program is free software; you can redistribute it
and/or modify it under the same terms as Perl itself.

%package dev
Summary: dev components for the perl-Compress-Raw-Lzma package.
Group: Development
Requires: perl-Compress-Raw-Lzma-lib = %{version}-%{release}
Provides: perl-Compress-Raw-Lzma-devel = %{version}-%{release}

%description dev
dev components for the perl-Compress-Raw-Lzma package.


%package lib
Summary: lib components for the perl-Compress-Raw-Lzma package.
Group: Libraries

%description lib
lib components for the perl-Compress-Raw-Lzma package.


%prep
%setup -q -n Compress-Raw-Lzma-2.082

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
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

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/Compress/Raw/Lzma.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/auto/Compress/Raw/Lzma/autosplit.ix

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Compress::Raw::Lzma.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/auto/Compress/Raw/Lzma/Lzma.so
