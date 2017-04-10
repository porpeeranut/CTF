open with Wireshark and export HTTP object from menu 
File > Export objects > HTTP
will got a flag.zip
then bruteforce with dictionary in Kali
fcrackzip -u -D -p "./dict.txt" ./Desktop/flag.zip

and unzip to get flag
unzip ./Desktop/flag.zip