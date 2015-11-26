UVAID1=10551832
UVAID2=10617558
UVAID=$(UVAID1)-$(UVAID2)
PROGNAME=modsim2
FILES=$(wildcard *.py) Makefile

MKDIR=mkdir
PACK=tar -jcvf
CP=cp
RM=rm -rf

clean:
	$(RM) *.pyc $(PROGNAME)-$(UVAID).tbz

tarball:
	$(MAKE) clean
	$(MKDIR) $(PROGNAME)-$(UVAID)
	$(CP) $(FILES) $(PROGNAME)-$(UVAID) || true
	$(PACK) $(PROGNAME)-$(UVAID).tbz $(PROGNAME)-$(UVAID)/*
	$(RM) $(PROGNAME)-$(UVAID)