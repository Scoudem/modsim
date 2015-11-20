UVAID1=10551832
UVAID2=10617558
UVAID=$(UVAID1)-$(UVAID2)
PROGNAME=modsim1
FILES=floatrep.c numdif.c root2.c newrap.c add.c add.h Makefile

MKDIR=mkdir
PACK=tar -jcvf
CC=gcc
CFLAGS=-Wall -Wextra -O1 -pedantic -std=c99 -Wunused-parameter
LDFLAGS=-lm
CP=cp
RM=rm -rf

all: floatrep numdif root2 newrap

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

floatrep: floatrep.o add.o
	$(CC) $(CFLAGS) -o floatrep floatrep.o add.o $(LDFLAGS)

numdif: numdif.c
	$(CC) $(CFLAGS) -o numdif  numdif.c $(LDFLAGS)

root2: root2.c
	$(CC) $(CFLAGS) -o root2  root2.c $(LDFLAGS)

newrap: newrap.c
	$(CC) $(CFLAGS) -o newrap  newrap.c $(LDFLAGS)

clean:
	$(RM) *.o  $(PROGNAME)-$(UVAID).tbz
	$(RM) floatrep numdif root2 newrap

tarball: all
	$(MAKE) clean
	$(MKDIR) $(PROGNAME)-$(UVAID)
	$(CP) $(FILES) $(PROGNAME)-$(UVAID) || true
	$(PACK) $(PROGNAME)-$(UVAID).tbz $(PROGNAME)-$(UVAID)/*
	$(RM) $(PROGNAME)-$(UVAID)
