UVAID1=10551832
UVAID2=10617558
UVAID=$(UVAID1)-$(UVAID2)
PROGNAME=modsim1
FILES=floatrep.c numdif.c root2.c newrap.c Makefile

MKDIR=mkdir
PACK=tar -jcvf
CC=gcc
CFLAGS=-Wall -Wextra -O1 -pedantic -std=c99
LDFLAGS=-lm
CP=cp
RM=rm -rf

all: floatrep numdif root2 newrap

floatrep:
	$(CC) $(CFLAGS) -o floatrep floatrep.c $(LDLAGS)

numdif:
	$(CC) $(CFLAGS) -o numdif  numdif.c $(LDLAGS)

root2:
	$(CC) $(CFLAGS) -o root2  root2.c $(LDLAGS)

newrap:
	$(CC) $(CFLAGS) -o newrap  newrap.c $(LDLAGS)

clean:
	$(RM) *.o  $(PROGNAME)-$(UVAID).tbz

tarball: all
	$(MAKE) clean
	$(MKDIR) $(PROGNAME)-$(UVAID)
	$(CP) $(FILES) $(PROGNAME)-$(UVAID) || true
	$(PACK) $(PROGNAME)-$(UVAID).tbz $(PROGNAME)-$(UVAID)/*
	$(RM) $(PROGNAME)-$(UVAID)