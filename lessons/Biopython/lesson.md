---
layout: page
title: 'Biopython'
visible: true
---

# Biopython 10-minute demo

 - **Author**: Madeleine Bonsma
 - **Research field**: Microbial ecology - prokaryote-phage interactions
 - **Lesson topic**: Biopython - examples
 - **Lesson content URL**: <https://github.com/UofTCoders/studyGroup/tree/gh-pages/lessons/Biopython>

## Intro ##

Biopython is a package designed for working with genetic sequence data in Python. 

THE MOST HELPFUL resource for Biopython: http://biopython.org/DIST/docs/tutorial/Tutorial.html

## Some Biopython features ##
  
  * The Seq object:
```
from Bio.Seq import Seq # sequence tools to do stuff like reverse complement
from Bio.Alphabet import generic_dna # more sequence tools

my_DNA = "GTTTTTGTACTCTCAAGATTTAAGTAACTGTACAAC"
my_DNA = Seq(my_DNA,generic_dna) # convert string to Seq object
my_DNA_reverse_complement = str(my_DNA.reverse_complement()) # reverse complement
```

There are also options for searching, transcription, and translation

  * parsing BLAST output: 

This is an example function that extracts pretty much everything from the blast records object. To see all options, use `dir(NCBIXML.parse)`, or check the help: `help(NCBIXML.parse)`

```
def parse_blast(resultfile):
    from Bio.Blast import NCBIXML
    result_handle = open(resultfile)
    blast_records = NCBIXML.parse(result_handle)

    count = 0
    for blast_record in blast_records:
        print "printing header stuff"
        print "blast_record.query", blast_record.query
        print "blast_record.query_letters", blast_record.query_letters
        print "printing descriptions"        
        print "printing descriptions"
        for description in blast_record.descriptions:
            print "description.title", description.title
            print "description.score", description.score #I think this is the best score
            print "description.e", description.e #I think this is the best e-value
            print "num_alignments", description.num_alignments #number of alignments per query
        print "printing alignments"
        for alignment in blast_record.alignments:
            print "alignment.title", alignment.title
            print "alignment.length", alignment.length
            print "printing hsps"
            for hsp in alignment.hsps: #Multiple hits means multiple hsps 
                print "hsp.align_length", hsp.align_length
        
                print "hsp.score", hsp.score
                print "hsp.bits", hsp.bits
                print "hsp.expect", hsp.expect
                print "hsp.num_alignments", hsp.num_alignments
                print "hsp.identities", hsp.identities
                print "hsp.positives", hsp.positives
                print "hsp.gaps", hsp.gaps
                print "hsp.strand", hsp.strand
                print "hsp.frame", hsp.frame
                print "hsp.query", hsp.query
                print "hsp.query_start", hsp.query_start
                print "hsp.query_end", hsp.query_end
                print "hsp.match", hsp.match
                print "hsp.sbjct", hsp.sbjct
                print "hsp.sbjct_start", hsp.sbjct_start
                print "hsp.sbjct_end", hsp.sbjct_end
        print "-----------------------------------"      

    result_handle.close()
    return

fn = "data/BLAST_output.xml"
# Here's what the output looks like: https://github.com/mbonsma/studyGroup/blob/gh-pages/lessons/Biopython/example_data/BLAST_output.xml

parse_blast(fn)
```

  * Running BLAST locally (on your machine as opposed to over the web)

Note: this won't work unless you install [blast+](http://www.ncbi.nlm.nih.gov/guide/howto/run-blast-local/) and then add the blast+ directory to your PATH. 

```
from Bio.Blast.Applications import NcbiblastnCommandline
#help(NcbiblastnCommandline)
import os

my_query = "data/spacers.fasta"

database = "DB_June29"

outfile = "data/BLAST_output.xml"

# these parameters should be changed to meet your needs
blastn_obj = NcbiblastnCommandline(query=my_query, db=database, evalue=1, num_alignments = 100, dust = "no", task = "blastn",reward = 1, penalty = -3, outfmt=5, out = outfile)

stdout, stderr = blastn_obj()
```