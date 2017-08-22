%{!?__build_pkg_version: %define __build_pkg_version 0.1.0}
%{!?__build_pkg_release: %define __build_pkg_release 1}
#@BugURL        https://sourceforge.net/p/xmlstar/bugs/
#@CVEURL        https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=xmlstarlet
Name: xmlstarlet
Summary: Command Line XML Toolkit
Version: %{__build_pkg_version}
Release: %{__build_pkg_release}%{?dist}
License: MIT
Group: Text Tools
Source0: http://xmlstar.sourceforge.net/downloads/xmlstarlet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: libxml2-devel >= 2.6.27
BuildRequires: libxslt-devel >= 1.1.9
URL: http://xmlstar.sourceforge.net/
Prefix: %{_prefix}
Docdir: %{_docdir}

%description
XMLStarlet is a set of command line utilities which can be used
to transform, query, validate, and edit XML documents and files
using simple set of shell commands in similar way it is done for
plain text files using UNIX grep, sed, awk, diff, patch, join, etc
commands.

%prep
%setup -q

%build
%configure
make

%install
rm -fr %{buildroot}

%makeinstall

%clean
rm -fr %{buildroot}

%post

%postun

%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog NEWS README Copyright TODO doc/xmlstarlet.txt doc/xmlstarlet.pdf
%doc %{_mandir}/man1/xmlstarlet.1*

%{prefix}/bin/xml
%changelog

