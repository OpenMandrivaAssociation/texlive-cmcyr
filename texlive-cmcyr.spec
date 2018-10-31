# revision 16696
# category Package
# catalog-ctan /fonts/cyrillic/cmcyr
# catalog-date 2007-09-16 18:06:50 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-cmcyr
Version:	20180303
Release:	2
Summary:	Computer Modern fonts with cyrillic extensions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/cyrillic/cmcyr
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmcyr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmcyr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
These are the Computer Modern fonts extended with Russian
letters, in MetaFont sources and ATM Compatible Type 1 format.
The fonts are provided in KOI-7, but virtual fonts are
available to recode them to three other Russian 8-bit
encodings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/cmcyr/cmcyr.map
%{_texmfdistdir}/fonts/source/public/cmcyr/ccsc.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/citall.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcb10.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcbx10.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcbx12.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcbx5.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcbx6.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcbx7.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcbx8.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcbx9.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcbxsl1.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcbxti1.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmccsc10.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmccsc8.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmccsc9.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcinch.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcitt10.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcsc11.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcsc12.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcsc14.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcsc18.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcsc24.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcsc36.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcscsl1.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcsl10.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcsl12.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcsl8.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcsl9.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcsltt1.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcss10.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcss12.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcss17.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcss8.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcss9.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcssbx1.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcssdc1.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcssi10.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcssi12.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcssi17.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcssi8.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcssi9.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcssq8.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcssqi8.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcti10.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcti12.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcti7.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcti8.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcti9.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmctitle.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmctt10.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmctt12.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmctt8.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmctt9.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcu10.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcyr10.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcyr12.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcyr17.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcyr5.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcyr6.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcyr7.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcyr8.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cmcyr9.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/coding.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cyrillic.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cyrl.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cyrlc.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cyrsymb.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cyrt.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cyru.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cytextit.mf
%{_texmfdistdir}/fonts/source/public/cmcyr/cytitle.mf
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcb10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcbx5.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcbxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcbxti10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmccsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmccsc8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmccsc9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcinch.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcitt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcsltt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcss10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcss12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcss17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcss8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcss9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcssbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcssdc10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcssi10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcssi12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcssi17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcssi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcssi9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcssq8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcssqi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcti10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcti12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcti7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcti8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcti9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmctt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmctt12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmctt8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmctt9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcu10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcyr10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcyr12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcyr17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcyr5.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcyr6.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcyr7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcyr8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/cmcyr9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmb10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmbx5.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmbxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmbxti10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmcsc8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmcsc9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcminch.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmitt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmmi10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmmi12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmmi6.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmmi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmmi9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmmib10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmr10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmr12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmr17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmr5.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmr6.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmr7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmr8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmr9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmsltt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmss10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmss12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmss17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmss8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmss9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmssbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmssdc10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmssi10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmssi12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmssi17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmssi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmssi9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmssq8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmssqi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmti10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmti12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmti7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmti8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmti9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmtt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmtt12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmtt8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmtt9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/kcmu10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmb10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmbx5.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmbxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmbxti10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmcsc8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmcsc9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcminch.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmitt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmmi10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmmi12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmmi6.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmmi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmmi9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmmib10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmr10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmr12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmr17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmr5.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmr6.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmr7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmr8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmr9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmsltt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmss10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmss12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmss17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmss8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmss9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmssbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmssdc10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmssi10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmssi12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmssi17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmssi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmssi9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmssq8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmssqi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmti10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmti12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmti7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmti8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmti9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmtt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmtt12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmtt8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmtt9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/wcmu10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmb10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmbx5.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmbxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmbxti10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmcsc8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmcsc9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcminch.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmitt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmmi10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmmi12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmmi6.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmmi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmmi9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmmib10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmr10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmr12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmr17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmr5.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmr6.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmr7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmr8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmr9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmsltt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmss10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmss12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmss17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmss8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmss9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmssbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmssdc10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmssi10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmssi12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmssi17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmssi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmssi9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmssq8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmssqi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmti10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmti12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmti7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmti8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmti9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmtt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmtt12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmtt8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmtt9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/xcmu10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmb10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmbx5.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmbxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmbxti10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmcsc8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmcsc9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycminch.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmitt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmmi10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmmi12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmmi6.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmmi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmmi9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmmib10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmr10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmr12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmr17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmr5.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmr6.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmr7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmr8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmr9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmsltt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmss10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmss12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmss17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmss8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmss9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmssbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmssdc10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmssi10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmssi12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmssi17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmssi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmssi9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmssq8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmssqi8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmti10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmti12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmti7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmti8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmti9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmtt10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmtt12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmtt8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmtt9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmcyr/ycmu10.tfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcb10.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcb10.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcbx10.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcbx10.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcbx12.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcbx12.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcbx5.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcbx5.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcbx6.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcbx6.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcbx7.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcbx7.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcbx8.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcbx8.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcbx9.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcbx9.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcbxsl1.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcbxsl1.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcbxti1.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcbxti1.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmccsc10.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmccsc10.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmccsc8.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmccsc8.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmccsc9.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmccsc9.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcinch7.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcinch7.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcitt10.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcitt10.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcsl10.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcsl10.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcsl12.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcsl12.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcsl8.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcsl8.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcsl9.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcsl9.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcsltt1.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcsltt1.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcss10.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcss10.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcss12.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcss12.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcss17.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcss17.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcss8.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcss8.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcss9.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcss9.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcssbx1.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcssbx1.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcssdc1.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcssdc1.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcssi10.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcssi10.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcssi12.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcssi12.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcssi17.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcssi17.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcssi8.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcssi8.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcssi9.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcssi9.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcssq8.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcssq8.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcssqi8.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcssqi8.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcti10.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcti10.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcti12.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcti12.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcti7.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcti7.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcti8.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcti8.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcti9.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcti9.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmctt10.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmctt10.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmctt12.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmctt12.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmctt8.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmctt8.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmctt9.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmctt9.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcu10.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcu10.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcyr10.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcyr10.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcyr12.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcyr12.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcyr17.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcyr17.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcyr5.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcyr5.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcyr6.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcyr6.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcyr7.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcyr7.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcyr8.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcyr8.pfm
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcyr9.pfb
%{_texmfdistdir}/fonts/type1/public/cmcyr/cmcyr9.pfm
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmb10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmbx10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmbx12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmbx5.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmbx6.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmbx7.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmbx8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmbx9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmbxsl10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmbxti10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmcsc10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmcsc8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmcsc9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcminch.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmitt10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmmi10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmmi12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmmi5.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmmi6.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmmi7.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmmi8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmmi9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmmib10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmr10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmr12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmr17.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmr5.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmr6.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmr7.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmr8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmr9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmsl10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmsl12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmsl8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmsl9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmsltt10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmss10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmss12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmss17.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmss8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmss9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmssbx10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmssdc10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmssi10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmssi12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmssi17.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmssi8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmssi9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmssq8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmssqi8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmti10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmti12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmti7.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmti8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmti9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmtt10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmtt12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmtt8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmtt9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/kcmu10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmb10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmbx10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmbx12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmbx5.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmbx6.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmbx7.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmbx8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmbx9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmbxsl10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmbxti10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmcsc10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmcsc8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmcsc9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcminch.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmitt10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmmi10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmmi12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmmi5.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmmi6.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmmi7.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmmi8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmmi9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmmib10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmr10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmr12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmr17.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmr5.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmr6.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmr7.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmr8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmr9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmsl10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmsl12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmsl8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmsl9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmsltt10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmss10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmss12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmss17.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmss8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmss9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmssbx10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmssdc10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmssi10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmssi12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmssi17.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmssi8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmssi9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmssq8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmssqi8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmti10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmti12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmti7.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmti8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmti9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmtt10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmtt12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmtt8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmtt9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/wcmu10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmb10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmbx10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmbx12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmbx5.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmbx6.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmbx7.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmbx8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmbx9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmbxsl10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmbxti10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmcsc10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmcsc8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmcsc9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcminch.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmitt10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmmi10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmmi12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmmi5.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmmi6.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmmi7.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmmi8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmmi9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmmib10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmr10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmr12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmr17.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmr5.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmr6.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmr7.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmr8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmr9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmsl10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmsl12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmsl8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmsl9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmsltt10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmss10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmss12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmss17.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmss8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmss9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmssbx10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmssdc10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmssi10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmssi12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmssi17.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmssi8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmssi9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmssq8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmssqi8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmti10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmti12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmti7.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmti8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmti9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmtt10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmtt12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmtt8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmtt9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/xcmu10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmb10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmbx10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmbx12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmbx5.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmbx6.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmbx7.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmbx8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmbx9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmbxsl10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmbxti10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmcsc10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmcsc8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmcsc9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycminch.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmitt10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmmi10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmmi12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmmi5.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmmi6.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmmi7.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmmi8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmmi9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmmib10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmr10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmr12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmr17.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmr5.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmr6.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmr7.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmr8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmr9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmsl10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmsl12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmsl8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmsl9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmsltt10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmss10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmss12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmss17.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmss8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmss9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmssbx10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmssdc10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmssi10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmssi12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmssi17.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmssi8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmssi9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmssq8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmssqi8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmti10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmti12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmti7.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmti8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmti9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmtt10.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmtt12.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmtt8.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmtt9.vf
%{_texmfdistdir}/fonts/vf/public/cmcyr/ycmu10.vf
%doc %{_texmfdistdir}/doc/fonts/cmcyr/README
%doc %{_texmfdistdir}/doc/fonts/cmcyr/cmalt
%doc %{_texmfdistdir}/doc/fonts/cmcyr/cmalte
%doc %{_texmfdistdir}/doc/fonts/cmcyr/cmiso
%doc %{_texmfdistdir}/doc/fonts/cmcyr/cmisoe
%doc %{_texmfdistdir}/doc/fonts/cmcyr/cmkde
%doc %{_texmfdistdir}/doc/fonts/cmcyr/cmkdee
%doc %{_texmfdistdir}/doc/fonts/cmcyr/cmkoi8
%doc %{_texmfdistdir}/doc/fonts/cmcyr/cmkoi8e
%doc %{_texmfdistdir}/doc/fonts/cmcyr/cmwin
%doc %{_texmfdistdir}/doc/fonts/cmcyr/cmwine
%doc %{_texmfdistdir}/doc/fonts/cmcyr/cyralt
%doc %{_texmfdistdir}/doc/fonts/cmcyr/cyralte
%doc %{_texmfdistdir}/doc/fonts/cmcyr/cyriso
%doc %{_texmfdistdir}/doc/fonts/cmcyr/cyrisoe
%doc %{_texmfdistdir}/doc/fonts/cmcyr/cyrkde
%doc %{_texmfdistdir}/doc/fonts/cmcyr/cyrkdee
%doc %{_texmfdistdir}/doc/fonts/cmcyr/cyrkoi8
%doc %{_texmfdistdir}/doc/fonts/cmcyr/cyrkoi8e
%doc %{_texmfdistdir}/doc/fonts/cmcyr/cyrwin
%doc %{_texmfdistdir}/doc/fonts/cmcyr/cyrwine
%doc %{_texmfdistdir}/doc/fonts/cmcyr/merge.6i
%doc %{_texmfdistdir}/doc/fonts/cmcyr/merge.6k
%doc %{_texmfdistdir}/doc/fonts/cmcyr/merge.6w
%doc %{_texmfdistdir}/doc/fonts/cmcyr/merge.alt
%doc %{_texmfdistdir}/doc/fonts/cmcyr/merge.bat
%doc %{_texmfdistdir}/doc/fonts/cmcyr/merge.iso
%doc %{_texmfdistdir}/doc/fonts/cmcyr/merge.koi
%doc %{_texmfdistdir}/doc/fonts/cmcyr/merge.o6w
%doc %{_texmfdistdir}/doc/fonts/cmcyr/merge.win
%doc %{_texmfdistdir}/doc/fonts/cmcyr/vf/cmcyr6i/merge.bat
%doc %{_texmfdistdir}/doc/fonts/cmcyr/vf/cmcyr6k/merge.bat
%doc %{_texmfdistdir}/doc/fonts/cmcyr/vf/cmcyr6w/merge.bat
%doc %{_texmfdistdir}/doc/fonts/cmcyr/wncalt
%doc %{_texmfdistdir}/doc/fonts/cmcyr/wncalte
%doc %{_texmfdistdir}/doc/fonts/cmcyr/wnciso
%doc %{_texmfdistdir}/doc/fonts/cmcyr/wncisoe
%doc %{_texmfdistdir}/doc/fonts/cmcyr/wnckoi8
%doc %{_texmfdistdir}/doc/fonts/cmcyr/wnckoi8e

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070916-2
+ Revision: 750260
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070916-1
+ Revision: 718077
- texlive-cmcyr
- texlive-cmcyr
- texlive-cmcyr
- texlive-cmcyr
- texlive-cmcyr

