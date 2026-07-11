%global tl_name recipecard
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Typeset recipes in note-card-sized boxes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/recipecard
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/recipecard.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/recipecard.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/recipecard.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The recipecard class typesets recipes into note card sized boxes that
can then be cut out and pasted on to note cards. The recipe then looks
elegant and fits in the box of recipes.

