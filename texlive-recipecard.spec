# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/recipecard
# catalog-date 2008-08-24 10:50:19 +0200
# catalog-license lppl
# catalog-version 2.0
Name:		texlive-recipecard
Version:	2.0
Release:	1
Summary:	Typeset recipes in note-card-sized boxes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/recipecard
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/recipecard.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/recipecard.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/recipecard.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The recipecard class typesets recipes into note card sized
boxes that can then be cut out and pasted on to note cards. The
recipe then looks elegant and fits in the box of recipes.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
