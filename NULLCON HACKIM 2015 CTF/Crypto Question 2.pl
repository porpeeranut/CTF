#!/usr/bin/perl

# NULLCON HACKIM 2015 CTF
# http://ctf.nullcon.net/challenge.php?c=0202
# Crypto Question 2 100 pts

my $crypto = "11313221111241132131614122141231311261112124131111132131623212141221322111131312141321222141621211124114212162114241131222211121623122211112211112133162321214121211135321221412121112112113221221111221416231242121613111131222211121124163221214216352123221111241132212211121621322141311322111216241121322214163111113221221112163113211422111216213222111131321623212141221322111231131721142123213221142312262131221112222221111222212411222322132221221322111123222311221112211421322312211423122111112312231222143212221322221135111211111321142411213221112132221126111215112123211211232122111";
my $bin = "";

@crypto = split("", $crypto);

#	Run Length Encoding
my $start = '0';
for (my $i=0; $i <= length($crypto); $i++) {
	#print "$crypto[$i]";
	if ($start == '0') {
		$bin .= '0'x$crypto[$i];
		$start = '1';
	} else {
		$bin .= '1'x$crypto[$i];
		$start = '0';
	}
}

#	Binary string to ASCII
$chars = length($bin);
@decrypt = pack("B$chars",$bin);
print "@decrypt\n";

# flag is "4674107e353af23dec1e471415bbd923"