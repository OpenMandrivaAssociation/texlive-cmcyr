%global tl_name cmcyr
%global tl_revision 68681

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Computer Modern fonts with cyrillic extensions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cyrillic/cmcyr
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmcyr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmcyr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
These are the Computer Modern fonts extended with Russian letters, in
Metafont sources and ATM Compatible Type 1 format. The fonts are
provided in KOI-7, but virtual fonts are available to recode them to
three other Russian 8-bit encodings.

