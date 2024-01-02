Name:		texlive-tagpdf
Version:	69165
Release:	1
Summary:	Tools for experimenting with tagging using pdfLaTeX and LuaLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tagpdf
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tagpdf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tagpdf.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tagpdf.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers tools to experiment with tagging and
accessibility using pdfLaTeX and LuaTeX. It isn't meant for
production but allows the user to try out how difficult it is
to tag some structures; to try out how much tagging is really
needed; to test what else is needed so that a pdf works e.g.
with a screen reader. Its goal is to get a feeling for what has
to be done, which kernel changes are needed, how packages
should be adapted.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/tagpdf
%{_texmfdistdir}/tex/latex/tagpdf
%doc %{_texmfdistdir}/doc/latex/tagpdf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
