/*
# This file is in AT&T syntax - see http://www.imada.sdu.dk/Courses/DM18/Litteratur/IntelnATT.htm
# and http://en.wikipedia.org/wiki/X86_assembly_language#Syntax. Both gdb and objdump produce
# AT&T syntax by default.

MOV $27186,%ebx
MOV $21894,%eax
MOV $27429,%ecx
CMP %eax,%ebx
JL L1
JMP L2
L1:
IMUL %eax,%ebx
ADD %eax,%ebx
MOV %ebx,%eax
SUB %ecx,%eax
JMP L3
L2:
IMUL %eax,%ebx
SUB %eax,%ebx
MOV %ebx,%eax
ADD %ecx,%eax
L3:
NOP
*/

#include <stdio.h>

int main(void) {
	int ebx,eax,ecx;
	ebx = 27186;
	eax = 21894;
	ecx = 27429;
	
	if (ebx < eax) {
		ebx *= eax;
		ebx += eax;
		eax = ebx;
		eax -= ecx;
	} else {
		ebx *= eax;
		ebx -= eax;
		eax = ebx;
		eax += ecx;
	}

	printf("%d",eax);
	return 0;
}