we neeed to enter the number that bigger than 1337 and equal to 1337!!
but they just check the number in 32 bit
so we can overflow it to exploit.

they need solution of problem to 1337

1337 overflow in binary is..
1 0000 0000 0000 0000 0000 0101 0011 1001

then perform it with -4 and / 7
python -c "print (0b100000000000000000000010100111001-4)/7"
613566947

and send this value to solve the problem.