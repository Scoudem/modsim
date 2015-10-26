UVAID1=10551832
UVAID2=10617558
UVAID=$(UVAID1)-$(UVAID2)
PROGNAME=modsim_1

MKDIR=mkdir
PACK=tar -jcvf
CC=gcc
CFLAGS=-Wall -Wextra -O1 -pedantic -std=c99
LDFLAGS=-lm
CP=cp
RM=rm -rf
OFILES=$(subst .c,.o,$(wildcard *.c))

$(PROGNAME): $(OFILES)
	$(CC) $(CFLAGS) $(OFILES) -o $(PROGNAME) $(LDFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

run: $(PROGNAME)
	./$(PROGNAME)

clean:
	$(RM) *.o $(PROGNAME) $(PROGNAME)-$(UVAID).tbz

tarball: $(PROGNAME)
	$(MAKE) clean
	$(MKDIR) $(PROGNAME)-$(UVAID)
	$(CP) * $(PROGNAME)-$(UVAID) || true
	$(PACK) $(PROGNAME)-$(UVAID).tbz $(PROGNAME)-$(UVAID)/*
	$(RM) $(PROGNAME)-$(UVAID)