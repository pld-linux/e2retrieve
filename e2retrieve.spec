Summary:	e2retrieve - a data recovery tool for ext2 filesystem
Summary(pl.UTF-8):	e2retrieve - narzędzie do odzyskiwania danych z systemu plików ext2
Name:		e2retrieve
Version:	20070415
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://www.guzu.net/files/%{name}_%{version}.tar.gz
# Source0-md5:	aa1ab6ff535980fc936fe6c3252e0be9
Patch0:		%{name}-lvmblkmajor.patch
Patch1:		%{name}-reg_eip.patch
URL:		http://www.guzu.net/linux/e2retrieve.php
BuildRequires:	e2fsprogs-devel
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

%description -l pl.UTF-8
e2retrieve to narzędzie do odzyskiwania danych z systemu plików ext2.
Oznacza to, że e2retrieve nie próbuje naprawić systemu plików, ale
wyciągnąć dane, żeby skopiować je w inne miejsce (inny dysk, NFS,
Samba...).

e2retrieve:
- może odzyskać dane z obciętego lub podzielonego systemu plików ext2
  (np. w przypadku LVM z uszkodzonym dyskiem),
- nie zapisuje na system plików ext2, który analizuje, więc nie
  zwiększy rozmiaru uszkodzeń,
- odzyskuje katalogi, drzewa katalogów, pliki, dowiązania symboliczne
  oraz pliki specjalne z ich prawami dostępu, właścicielem i datą
  modyfikacji,
- jest napisane całkowicie od początku w C,
- nie wymaga żadnej biblioteki,
- może łatwo zmieścić się na dyskietce ratunkowej (w przypadku, kiedy
  brak odpowiedniej liczby portów IDE),
- nie jest narzędziem do odkasowywania.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

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
