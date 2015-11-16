## Some cool things you can do with Biopython
## MB - August 20, 2015

## Biopython is a package designed for working with genetic sequence data in Python. 

## THE MOST HELPFUL resource for Biopython: http://biopython.org/DIST/docs/tutorial/Tutorial.html

# Two useful commands:

# help(some_thing) - prints the help stuff
# dir(some_thing) - list the attributes of the class to which some_thing belongs

# ---------------------------- The Seq object ----------------------------

from Bio.Seq import Seq # sequence tools to do stuff like reverse complement
from Bio.Alphabet import generic_dna # more sequence tools

my_DNA = "GTTTTTGTACTCTCAAGATTTAAGTAACTGTACAAC"

my_DNA = Seq(my_DNA,generic_dna) # convert string to Seq object

my_DNA_reverse_complement = str(my_DNA.reverse_complement()) # reverse complement

# Options for searching, transcription, and translation

# ------------------------- parse BLAST output ------------------------------

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

fn = "example_data/BLAST_output.xml"

parse_blast(fn)

"""
# ------------------------- Local BLAST -------------------------------------

from Bio.Blast.Applications import NcbiblastnCommandline
#help(NcbiblastnCommandline)
import os

my_query = "example_data/spacers.fasta"

database = "DB_June29"

outfile = "example_data/BLAST_output.xml"

# these parameters should be changed to meet your needs
blastn_obj = NcbiblastnCommandline(query=my_query, db=database, evalue=1, num_alignments = 100, dust = "no", task = "blastn",reward = 1, penalty = -3, outfmt=5, out = outfile)

stdout, stderr = blastn_obj()

"""