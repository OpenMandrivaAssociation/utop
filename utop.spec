Name:           utop
Version:        1.5
Release:        1
Summary:        An improved toplevel for OCaml
License:        BSD-3-clause
Group:          Development/Other
URL:            http://forge.ocamlcore.org/projects/utop/
Source0:        http://forge.ocamlcore.org/frs/download.php/1169/utop-%{version}.tar.gz
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-lambda-term-devel
BuildRequires:  camlp4

%description
Utop is a universal toplevel for OCaml which can run in a terminal or
in emacs. It supports completion, colors, parenthesis matching, ...

%package        devel
Summary:        Development files for %{name}
Group:          Development/OCaml
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n utop-%{version}

%build
sh configure \
    --prefix %{_prefix} \
    --libdir %{_libdir} \
    --libexecdir %{_libexecdir} \
    --exec-prefix %{_exec_prefix} \
    --bindir %{_bindir} \
    --sbindir %{_sbindir} \
    --mandir %{_mandir} \
    --datadir %{_datadir} \
    --localstatedir %{_localstatedir} \
    --sharedstatedir %{_sharedstatedir} \
    --destdir %{buildroot}

make
make doc
mv _build/utop-api.docdir/ doc

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR/utop
make install

%files
%doc README.md LICENSE CHANGES.md
%dir %{_libdir}/ocaml/utop
%{_bindir}/utop
%{_bindir}/utop-full
%{_datadir}/emacs/site-lisp/utop.el
%{_libdir}/ocaml/utop/META
%{_libdir}/ocaml/utop/*.cmi
%{_libdir}/ocaml/utop/*.cma
%{_libdir}/ocaml/utop/*.cmxs
%{_mandir}/man1/*
%{_mandir}/man5/*

%files devel
%doc doc/
%doc examples/
%{_libdir}/ocaml/utop/*.a
%{_libdir}/ocaml/utop/*.cmxa
%{_libdir}/ocaml/utop/*.cmx
%{_libdir}/ocaml/utop/*.mli
