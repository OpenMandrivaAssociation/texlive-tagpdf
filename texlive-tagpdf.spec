%global tl_name tagpdf
%global tl_revision 79038

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0c
Release:	%{tl_revision}.1
Summary:	Code for PDF tagging using pdfLaTeX and LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tagpdf
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tagpdf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tagpdf.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tagpdf.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package contains the core code for tagging and accessibility used by
the LaTeX kernel in the Tagged PDF project. See
https://github.com/latex3/tagging-project for more information.

