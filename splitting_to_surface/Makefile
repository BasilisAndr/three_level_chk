LANG1 = ckt
TARGETS = $(LANG1).mor.hfstol  $(LANG1).surf_split.hfstol $(LANG1).mor.hfst $(LANG1).surf_split.hfst
DATA = $(chkchn_DATA)
chkchn_DATA = $(TARGETS)

all: all-am

all-am: Makefile $(DATA)

# twol file with morpheme boundaries in
$(LANG1).twol.hfst: $(LANG1).twol
	hfst-twolc $(LANG1).twol -o $(LANG1).twol.hfst

# results of lexc and twol (surface transducer with boundaries)
#   нытэминӈыӄин.adj<3pl><part>:тэминӈыӄин-ӄинэт-э
$(LANG1).lexctwol.hfst: $(LANG1).twol.hfst ../glossing/$(LANG1).lexc.hfst
	hfst-compose-intersect -1 ../glossing/$(LANG1).lexc.hfst -2 $(LANG1).twol.hfst -o $(LANG1).lexctwol.hfst

# surface forms with morpheme boundaries + morphotactic constraints
#   э-тэминӈыӄин-кинэн-ӈэ:нытэминӈыӄин.adj<3pl><part>
$(LANG1).mor.hfst: $(LANG1).lexctwol.mor.hfst  ../glossing/$(LANG1).twoc.hfst
	hfst-compose-intersect -1 $(LANG1).lexctwol.mor.hfst -2 ../glossing/$(LANG1).twoc.hfst -o $(LANG1).mor.hfst

# analyses to segmented surface forms 
#   нытэминӈыӄин.adj<3pl><part>:тэминӈыӄин-ӄинэт-э
$(LANG1).surf_split.hfst: $(LANG1).mor.hfst
	hfst-invert $(LANG1).mor.hfst -o $(LANG1).surf_split.hfst

# optimised version of ckt.surf_split.hfst
$(LANG1).surf_split.hfstol: $(LANG1).surf_split.hfst
	hfst-fst2fst --format=optimized-lookup-weighted -i $(LANG1).surf_split.hfst -o $(LANG1).surf_split.hfstol


	# for debugging
	$(LANG1).lexctwol.mor.hfst: $(LANG1).lexctwol.hfst
		hfst-invert $(LANG1).lexctwol.hfst -o $(LANG1).lexctwol.mor.hfst


	# for debugging
	$(LANG1).mor.hfstol: $(LANG1).mor.hfst
		hfst-fst2fst --format=optimized-lookup-weighted -i $(LANG1).mor.hfst -o $(LANG1).mor.hfstol


clear:
	rm $(TARGETS) $(LANG1).lexctwol.hfst $(LANG1).lexctwol.mor.hfst
