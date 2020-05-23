# insertion-entropy-calc
This folder contains all the raw data and scripts needed to perform the calculation shown in Figure S5a.

681c5LT_0.newinfo.withlengths.sorted.txt contains all of the insertions from our lineage tracing dataset (Figure 5)
above the cutoff abundance of 0.0139%. The other files are just there so that the code runs, and as a sanity check.
Other than deleting the low-abundance insertions and ROOT sequence, and combining all the files into 
681c5LT_0.newinfo.withlengths.sorted.txt, these "withlengths.sorted.txt" files are just as they came off the 
CHYRON-NGS pipeline.

These scripts were all run on macOS HighSierra with Anaconda3 and Python2.7 installed.

To calculate the proportions of all possible 4-nt sequences, for example, type the following into the terminal:

python3 ins-parsing-no-umi-256.py well_data.txt

When prompted, type "16" to include all sequences.

The script outputs a file called "base_count_wells-256.txt". (Included in this repository as an example.) All of the
data can be found under "well 1." (This is harvested from "681c5LT_0.newinfo.withlengths.sorted.txt.") 

To calculate the proportion of all possible 5-nt sequences, use ins-parsing-no-umi-1024.py, etc.

"summary and entropy calc.xlsx" is included in this repository as an example of how to use the outputs of the scripts
to calculate Shannon entropy.
