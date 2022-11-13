Name:		texlive-recipecard
Version:	15878
Release:	1
Summary:	Typeset recipes in note-card-sized boxes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/recipecard
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/recipecard.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/recipecard.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/recipecard.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The recipecard class typesets recipes into note card sized
boxes that can then be cut out and pasted on to note cards. The
recipe then looks elegant and fits in the box of recipes.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/recipecard/recipecard.cls
%doc %{_texmfdistdir}/doc/latex/recipecard/README
%doc %{_texmfdistdir}/doc/latex/recipecard/recipecard.pdf
%doc %{_texmfdistdir}/doc/latex/recipecard/test2.pdf
%doc %{_texmfdistdir}/doc/latex/recipecard/test2.tex
#- source
%doc %{_texmfdistdir}/source/latex/recipecard/recipecard.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
