Summary:	e2retrieve - a data recovery tool for ext2 filesystem
Summary(pl):	e2retrieve - narz�dzie do odzyskiwania danych z systemu plik�w ext2
Name:		e2retrieve
Version:	20031216
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://coredump.free.fr/linux/%{name}_%{version}.tar.gz
# Source0-md5:	628de3e4c1e0c0f55b74ee5c5bd1cb67
Patch0:		%{name}-lvmblkmajor.patch
URL:		http://coredump.free.fr/linux/e2retrieve.php
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
e2retrieve is a data recovery tool for ext2 filesystem. This means
that e2retrieve will not try to repair the filesystem but will extract
data to "copy" it to another place (another disk, NFS, Samba, ...).

e2retrieve:
- can recover data from a truncated or split ext2 filesystem (in the
  case of a LVM with a disk that has crashed, for example), 
- will not write onto the ext2 filesystem it is analysing, therefore
  it will never increase damages previously caused,
- recovers directories, directories tree, files, symbolic links and
  special files with their access rights, owner and modification date,
- is fully written in C from scratch,
- does not need any library,
- can easily fit in a rescue floppy disk (in the case where you do not
  have enough IDE slots),
- is not an undeleting tool.

%description -l pl
e2retrieve to narz�dzie do odzyskiwania danych z systemu plik�w ext2.
Oznacza to, �e e2retrieve nie pr�buje naprawi� systemu plik�w, ale
wyci�gn�� dane, �eby skopiowa� je w inne miejsce (inny dysk, NFS,
Samba...).

e2retrieve:
- mo�e odzyska� dane z obci�tego lub podzielonego systemu plik�w ext2
  (np. w przypadku LVM z uszkodzonym dyskiem),
- nie zapisuje na system plik�w ext2, kt�ry analizuje, wi�c nie
  zwi�kszy rozmiaru uszkodze�,
- odzyskuje katalogi, drzewa katalog�w, pliki, dowi�zania symboliczne
  oraz pliki specjalne z ich prawami dost�pu, w�a�cicielem i dat�
  modyfikacji,
- jest napisane ca�kowicie od pocz�tku w C,
- nie wymaga �adnej biblioteki,
- mo�e �atwo zmie�ci� si� na dyskietce ratunkowej (w przypadku, kiedy
  brak odpowiedniej liczby port�w IDE),
- nie jest narz�dziem do odkasowywania.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS_DIST="%{rpmcflags} -Wall" \
	STRIP=true

%install
rm -rf $RPM_BUILD_ROOT

install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README TODO
%attr(755,root,root) %{_bindir}/*
