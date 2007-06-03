# TODO: optflags or noarch?
Summary:	Decodes transfer encoded text type MIME messages
Summary(pl.UTF-8):	Narzędzie do dekodowania wiadomości tekstowych MIME
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
This program performs the decoding of transfer encoded text type MIME
messages. The message in its entirety is read from stdin. The decoded
message is written to stdout; hence, this program behaves as a filter
which may be placed wherever convenient. I particular like it in front
of my slocal command in my .forward file.

It is assumed that the message has reached its point of final delivery
and at that point 8-bit text types can be handled natively. Hence, the
need for transfer-encodings is not present any more.

%description -l pl.UTF-8
Ten program przeprowadza dekodowanie wiadomości tekstowych MIME.
Wiadomość jest czytana w całości ze standardowego wejścia. Zdekodowana
wiadomość jest wypisywana na stadardowe wyjście; w ten sposób problem
zachowuje się jak filtr, który można umieścić tam, gdzie wygodnie. W
szczególności na przykład na początku polecenia slocal w pliku
.forward.

Zakłada się, że wiadomość osiągnęła miejsce przeznaczenia na tym
etapie 8-bitowe typy tekstowe mogą być obsługiwane natywnie. W ten
sposób nie ma już potrzeby kodowania wiadomości na potrzeby
przesyłania.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -f debian/rules \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D debian/mimedecode.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING debian/README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man?/%{name}.*
