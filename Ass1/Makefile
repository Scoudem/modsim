UVAID1=10551832
UVAID2=10617558
UVAID=$(UVAID1)-$(UVAID2)
PROGNAME=modsim1

MKDIR=mkdir
PACK=tar -jcvf
CC=gcc
CFLAGS=-Wall -Wextra -O1 -pedantic -std=c99
LDFLAGS=-lm
CP=cp
RM=rm -rf

all: floatrep numdif root2 newrap

floatrep:
	$(CC) $(CFLAGS) floatrep.c $(LDLAGS)

numdif:
	$(CC) $(CFLAGS) numdif.c $(LDLAGS)

root2:
	$(CC) $(CFLAGS) root2.c $(LDLAGS)

newrap:
	$(CC) $(CFLAGS) newrap.c $(LDLAGS)

clean:
	$(RM) *.o  $(PROGNAME)-$(UVAID).tbz

tarball: $(PROGNAME)
	$(MAKE) clean
	$(MKDIR) $(PROGNAME)-$(UVAID)
	$(CP) * $(PROGNAME)-$(UVAID) || true
	$(PACK) $(PROGNAME)-$(UVAID).tbz $(PROGNAME)-$(UVAID)/*
	$(RM) $(PROGNAME)-$(UVAID)