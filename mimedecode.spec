Summary:	Decodes transfer encoded text type mime messages
Name:		mimedecode
Version:	1.9
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://ftp.debian.org/debian/pool/main/m/mimedecode/%{name}_%{version}.orig.tar.gz
# Source0-md5:	c9df055e2f68d672390d877ab0a315d8
Patch0:		http://ftp.debian.org/debian/pool/main/m/mimedecode/%{name}_1.9-4.diff.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program performs the decoding of transfer encoded text type mime
messages. The message in its entirety is read from stdin. The decoded
message is written to stdout; hence, this program behaves as a filter
which may be placed wherever convenient. I particular like it in front
of my slocal command in my .forward file.

It is assumed that the message has reached its point of final delivery
and at that point 8-bit text types can be handled natively. Hence, the
need for transfer-encodings is not present any more.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -f debian/rules

%install
rm -rf $RPM_BUILD_ROOT

install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D debian/mimedecode.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man?/%{name}.*
%doc COPYING debian/README
