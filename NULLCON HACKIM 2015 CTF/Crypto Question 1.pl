#!/usr/bin/perl

# NULLCON HACKIM 2015 CTF
# http://ctf.nullcon.net/challenge.php?c=0201
# Crypto Question 1 100 pts

my $crypto = "TaPoGeTaBiGePoHfTmGeYbAtPtHoPoTaAuPtGeAuYbGeBiHoTaTmPtHoTmGePoAuGeErTaBiHoAuRnTmPbGePoHfTmGeTmRaTaBiPoTmPtHoTmGeAuYbGeTbGeLuTmPtTmPbTbOsGePbTmTaLuPtGeAuYbGeAuPbErTmPbGeTaPtGePtTbPoAtPbTmGeTbPtErGePoAuGeYbTaPtErGePoHfTmGeHoTbAtBiTmBiGeLuAuRnTmPbPtTaPtLuGePoHfTaBiGeAuPbErTmPbPdGeTbPtErGePoHfTaBiGePbTmYbTmPbBiGeTaPtGeTmTlAtTbOsGeIrTmTbBiAtPbTmGePoAuGePoHfTmGePbTmOsTbPoTaAuPtBiGeAuYbGeIrTbPtGeRhGeBiAuHoTaTbOsGeTbPtErGeHgAuOsTaPoTaHoTbOsGeRhGeTbPtErGePoAuGePoHfTmGeTmPtPoTaPbTmGeAtPtTaRnTmPbBiTmGeTbBiGeTbGeFrHfAuOsTmPd";
$crypto =~ s/At/85/g;
$crypto =~ s/Au/79/g;
$crypto =~ s/Bi/83/g;
$crypto =~ s/Er/68/g;
$crypto =~ s/Fr/87/g;
$crypto =~ s/Ge/32/g;
$crypto =~ s/Hf/72/g;
$crypto =~ s/Hg/80/g;
$crypto =~ s/Ho/67/g;
$crypto =~ s/Ir/77/g;
$crypto =~ s/Lu/71/g;
$crypto =~ s/Os/76/g;
$crypto =~ s/Pb/82/g;
$crypto =~ s/Pd/46/g;
$crypto =~ s/Po/84/g;
$crypto =~ s/Pt/78/g;
$crypto =~ s/Ra/88/g;
$crypto =~ s/Rh/45/g;
$crypto =~ s/Rn/86/g;
$crypto =~ s/Ta/73/g;
$crypto =~ s/Tb/65/g;
$crypto =~ s/Tl/81/g;
$crypto =~ s/Tm/69/g;
$crypto =~ s/Yb/70/g;

#	ASCII number to String
$crypto =~ s/(..)/chr($1)/eg;

print $crypto."\r\n";

# flag is "Periodic table"