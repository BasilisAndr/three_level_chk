LANG1 = ckt
TARGETS = $(LANG1).mor.hfstol  $(LANG1).surf_split.hfstol $(LANG1).mor.hfst $(LANG1).surf_split.hfst
DATA = $(chkchn_DATA)
chkchn_DATA = $(TARGETS)

all: all-am

all-am: Makefile $(DATA)

$(LANG1).twol.hfst: $(LANG1).twol
	hfst-twolc $(LANG1).twol -o $(LANG1).twol.hfst

$(LANG1).lexctwol.hfst: $(LANG1).twol.hfst
	cp ../glossing/$(LANG1).lexc.hfst ./$(LANG1).lexc.hfst
	hfst-compose-intersect -1 $(LANG1).lexc.hfst -2 $(LANG1).twol.hfst -o $(LANG1).lexctwol.hfst


$(LANG1).lexctwol.mor.hfst: $(LANG1).lexctwol.hfst
	hfst-invert $(LANG1).lexctwol.hfst -o $(LANG1).lexctwol.mor.hfst



$(LANG1).mor.hfst: $(LANG1).lexctwol.mor.hfst
	cp ../glossing/$(LANG1).twoc.hfst ./$(LANG1).twoc.hfst
	hfst-compose-intersect -1 $(LANG1).lexctwol.mor.hfst -2 $(LANG1).twoc.hfst -o $(LANG1).mor.hfst

$(LANG1).mor.hfstol: $(LANG1).mor.hfst
	hfst-fst2fst --format=optimized-lookup-weighted -i $(LANG1).mor.hfst -o $(LANG1).mor.hfstol

$(LANG1).surf_split.hfst: $(LANG1).mor.hfst
	hfst-invert $(LANG1).mor.hfst -o $(LANG1).surf_split.hfst

$(LANG1).surf_split.hfstol: $(LANG1).surf_split.hfst
	hfst-fst2fst --format=optimized-lookup-weighted -i $(LANG1).surf_split.hfst -o $(LANG1).surf_split.hfstol

clear:
	rm $(TARGETS) $(LANG1).lexctwol.hfst $(LANG1).lexctwol.mor.hfst
