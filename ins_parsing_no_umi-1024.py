import pickle
import sys
import pprint
import re

# with open('green_LT_insDict.pkl', 'rb') as pkl:
# 	insDict = pickle.load(pkl)

# insDict = {
	# insertion:{		
# 		"counts": {
#			"well" : int()
#		}
# 	}
# }
## sysargv[1] = "exp"_well_data_file.txt
def writestuff(file, numA, numC, numG, numT,combinations,combcount):
	file.write('\n')
	file.write(f"A: {numA}")
	file.write('\n')
	file.write(f"C: {numC}")
	file.write('\n')
	file.write(f"G: {numG}")
	file.write('\n')
	file.write(f"T: {numT}")
	file.write('\n')
	i = 0
	while i < len(combinations):
		file.write(f"{combinations[i]}: {combcount[i]}")
		file.write('\n')
		i += 1

insDict = {}
open('base_count_wells-1024.txt','w').close()
with open(sys.argv[1]) as samples:
	for line in samples:
		counter = 0
		c = 0
		count = 0
		insCount = 0
		line = line.strip().split(' ')
		withlengths = line[0]
		well_regex = re.search('(?<=_).*?(?=[.])', line[0]) ## finds well number between '_' and '.' of file name
		well = f"well_{str(int(well_regex.group())+1)}" 
		print(f"Working on {well}")

		with open(withlengths) as lengths:
			numA,numC,numG,numT = 0,0,0,0
			combinations = ["AAAAA","AAAAC","AAAAG","AAAAT","AAACA","AAACC","AAACG","AAACT","AAAGA","AAAGC","AAAGG","AAAGT","AAATA","AAATC","AAATG","AAATT","AACAA","AACAC","AACAG","AACAT","AACCA","AACCC","AACCG","AACCT","AACGA","AACGC","AACGG","AACGT","AACTA","AACTC","AACTG","AACTT","AAGAA","AAGAC","AAGAG","AAGAT","AAGCA","AAGCC","AAGCG","AAGCT","AAGGA","AAGGC","AAGGG","AAGGT","AAGTA","AAGTC","AAGTG","AAGTT","AATAA","AATAC","AATAG","AATAT","AATCA","AATCC","AATCG","AATCT","AATGA","AATGC","AATGG","AATGT","AATTA","AATTC","AATTG","AATTT","ACAAA","ACAAC","ACAAG","ACAAT","ACACA","ACACC","ACACG","ACACT","ACAGA","ACAGC","ACAGG","ACAGT","ACATA","ACATC","ACATG","ACATT","ACCAA","ACCAC","ACCAG","ACCAT","ACCCA","ACCCC","ACCCG","ACCCT","ACCGA","ACCGC","ACCGG","ACCGT","ACCTA","ACCTC","ACCTG","ACCTT","ACGAA","ACGAC","ACGAG","ACGAT","ACGCA","ACGCC","ACGCG","ACGCT","ACGGA","ACGGC","ACGGG","ACGGT","ACGTA","ACGTC","ACGTG","ACGTT","ACTAA","ACTAC","ACTAG","ACTAT","ACTCA","ACTCC","ACTCG","ACTCT","ACTGA","ACTGC","ACTGG","ACTGT","ACTTA","ACTTC","ACTTG","ACTTT","AGAAA","AGAAC","AGAAG","AGAAT","AGACA","AGACC","AGACG","AGACT","AGAGA","AGAGC","AGAGG","AGAGT","AGATA","AGATC","AGATG","AGATT","AGCAA","AGCAC","AGCAG","AGCAT","AGCCA","AGCCC","AGCCG","AGCCT","AGCGA","AGCGC","AGCGG","AGCGT","AGCTA","AGCTC","AGCTG","AGCTT","AGGAA","AGGAC","AGGAG","AGGAT","AGGCA","AGGCC","AGGCG","AGGCT","AGGGA","AGGGC","AGGGG","AGGGT","AGGTA","AGGTC","AGGTG","AGGTT","AGTAA","AGTAC","AGTAG","AGTAT","AGTCA","AGTCC","AGTCG","AGTCT","AGTGA","AGTGC","AGTGG","AGTGT","AGTTA","AGTTC","AGTTG","AGTTT","ATAAA","ATAAC","ATAAG","ATAAT","ATACA","ATACC","ATACG","ATACT","ATAGA","ATAGC","ATAGG","ATAGT","ATATA","ATATC","ATATG","ATATT","ATCAA","ATCAC","ATCAG","ATCAT","ATCCA","ATCCC","ATCCG","ATCCT","ATCGA","ATCGC","ATCGG","ATCGT","ATCTA","ATCTC","ATCTG","ATCTT","ATGAA","ATGAC","ATGAG","ATGAT","ATGCA","ATGCC","ATGCG","ATGCT","ATGGA","ATGGC","ATGGG","ATGGT","ATGTA","ATGTC","ATGTG","ATGTT","ATTAA","ATTAC","ATTAG","ATTAT","ATTCA","ATTCC","ATTCG","ATTCT","ATTGA","ATTGC","ATTGG","ATTGT","ATTTA","ATTTC","ATTTG","ATTTT","CAAAA","CAAAC","CAAAG","CAAAT","CAACA","CAACC","CAACG","CAACT","CAAGA","CAAGC","CAAGG","CAAGT","CAATA","CAATC","CAATG","CAATT","CACAA","CACAC","CACAG","CACAT","CACCA","CACCC","CACCG","CACCT","CACGA","CACGC","CACGG","CACGT","CACTA","CACTC","CACTG","CACTT","CAGAA","CAGAC","CAGAG","CAGAT","CAGCA","CAGCC","CAGCG","CAGCT","CAGGA","CAGGC","CAGGG","CAGGT","CAGTA","CAGTC","CAGTG","CAGTT","CATAA","CATAC","CATAG","CATAT","CATCA","CATCC","CATCG","CATCT","CATGA","CATGC","CATGG","CATGT","CATTA","CATTC","CATTG","CATTT","CCAAA","CCAAC","CCAAG","CCAAT","CCACA","CCACC","CCACG","CCACT","CCAGA","CCAGC","CCAGG","CCAGT","CCATA","CCATC","CCATG","CCATT","CCCAA","CCCAC","CCCAG","CCCAT","CCCCA","CCCCC","CCCCG","CCCCT","CCCGA","CCCGC","CCCGG","CCCGT","CCCTA","CCCTC","CCCTG","CCCTT","CCGAA","CCGAC","CCGAG","CCGAT","CCGCA","CCGCC","CCGCG","CCGCT","CCGGA","CCGGC","CCGGG","CCGGT","CCGTA","CCGTC","CCGTG","CCGTT","CCTAA","CCTAC","CCTAG","CCTAT","CCTCA","CCTCC","CCTCG","CCTCT","CCTGA","CCTGC","CCTGG","CCTGT","CCTTA","CCTTC","CCTTG","CCTTT","CGAAA","CGAAC","CGAAG","CGAAT","CGACA","CGACC","CGACG","CGACT","CGAGA","CGAGC","CGAGG","CGAGT","CGATA","CGATC","CGATG","CGATT","CGCAA","CGCAC","CGCAG","CGCAT","CGCCA","CGCCC","CGCCG","CGCCT","CGCGA","CGCGC","CGCGG","CGCGT","CGCTA","CGCTC","CGCTG","CGCTT","CGGAA","CGGAC","CGGAG","CGGAT","CGGCA","CGGCC","CGGCG","CGGCT","CGGGA","CGGGC","CGGGG","CGGGT","CGGTA","CGGTC","CGGTG","CGGTT","CGTAA","CGTAC","CGTAG","CGTAT","CGTCA","CGTCC","CGTCG","CGTCT","CGTGA","CGTGC","CGTGG","CGTGT","CGTTA","CGTTC","CGTTG","CGTTT","CTAAA","CTAAC","CTAAG","CTAAT","CTACA","CTACC","CTACG","CTACT","CTAGA","CTAGC","CTAGG","CTAGT","CTATA","CTATC","CTATG","CTATT","CTCAA","CTCAC","CTCAG","CTCAT","CTCCA","CTCCC","CTCCG","CTCCT","CTCGA","CTCGC","CTCGG","CTCGT","CTCTA","CTCTC","CTCTG","CTCTT","CTGAA","CTGAC","CTGAG","CTGAT","CTGCA","CTGCC","CTGCG","CTGCT","CTGGA","CTGGC","CTGGG","CTGGT","CTGTA","CTGTC","CTGTG","CTGTT","CTTAA","CTTAC","CTTAG","CTTAT","CTTCA","CTTCC","CTTCG","CTTCT","CTTGA","CTTGC","CTTGG","CTTGT","CTTTA","CTTTC","CTTTG","CTTTT","GAAAA","GAAAC","GAAAG","GAAAT","GAACA","GAACC","GAACG","GAACT","GAAGA","GAAGC","GAAGG","GAAGT","GAATA","GAATC","GAATG","GAATT","GACAA","GACAC","GACAG","GACAT","GACCA","GACCC","GACCG","GACCT","GACGA","GACGC","GACGG","GACGT","GACTA","GACTC","GACTG","GACTT","GAGAA","GAGAC","GAGAG","GAGAT","GAGCA","GAGCC","GAGCG","GAGCT","GAGGA","GAGGC","GAGGG","GAGGT","GAGTA","GAGTC","GAGTG","GAGTT","GATAA","GATAC","GATAG","GATAT","GATCA","GATCC","GATCG","GATCT","GATGA","GATGC","GATGG","GATGT","GATTA","GATTC","GATTG","GATTT","GCAAA","GCAAC","GCAAG","GCAAT","GCACA","GCACC","GCACG","GCACT","GCAGA","GCAGC","GCAGG","GCAGT","GCATA","GCATC","GCATG","GCATT","GCCAA","GCCAC","GCCAG","GCCAT","GCCCA","GCCCC","GCCCG","GCCCT","GCCGA","GCCGC","GCCGG","GCCGT","GCCTA","GCCTC","GCCTG","GCCTT","GCGAA","GCGAC","GCGAG","GCGAT","GCGCA","GCGCC","GCGCG","GCGCT","GCGGA","GCGGC","GCGGG","GCGGT","GCGTA","GCGTC","GCGTG","GCGTT","GCTAA","GCTAC","GCTAG","GCTAT","GCTCA","GCTCC","GCTCG","GCTCT","GCTGA","GCTGC","GCTGG","GCTGT","GCTTA","GCTTC","GCTTG","GCTTT","GGAAA","GGAAC","GGAAG","GGAAT","GGACA","GGACC","GGACG","GGACT","GGAGA","GGAGC","GGAGG","GGAGT","GGATA","GGATC","GGATG","GGATT","GGCAA","GGCAC","GGCAG","GGCAT","GGCCA","GGCCC","GGCCG","GGCCT","GGCGA","GGCGC","GGCGG","GGCGT","GGCTA","GGCTC","GGCTG","GGCTT","GGGAA","GGGAC","GGGAG","GGGAT","GGGCA","GGGCC","GGGCG","GGGCT","GGGGA","GGGGC","GGGGG","GGGGT","GGGTA","GGGTC","GGGTG","GGGTT","GGTAA","GGTAC","GGTAG","GGTAT","GGTCA","GGTCC","GGTCG","GGTCT","GGTGA","GGTGC","GGTGG","GGTGT","GGTTA","GGTTC","GGTTG","GGTTT","GTAAA","GTAAC","GTAAG","GTAAT","GTACA","GTACC","GTACG","GTACT","GTAGA","GTAGC","GTAGG","GTAGT","GTATA","GTATC","GTATG","GTATT","GTCAA","GTCAC","GTCAG","GTCAT","GTCCA","GTCCC","GTCCG","GTCCT","GTCGA","GTCGC","GTCGG","GTCGT","GTCTA","GTCTC","GTCTG","GTCTT","GTGAA","GTGAC","GTGAG","GTGAT","GTGCA","GTGCC","GTGCG","GTGCT","GTGGA","GTGGC","GTGGG","GTGGT","GTGTA","GTGTC","GTGTG","GTGTT","GTTAA","GTTAC","GTTAG","GTTAT","GTTCA","GTTCC","GTTCG","GTTCT","GTTGA","GTTGC","GTTGG","GTTGT","GTTTA","GTTTC","GTTTG","GTTTT","TAAAA","TAAAC","TAAAG","TAAAT","TAACA","TAACC","TAACG","TAACT","TAAGA","TAAGC","TAAGG","TAAGT","TAATA","TAATC","TAATG","TAATT","TACAA","TACAC","TACAG","TACAT","TACCA","TACCC","TACCG","TACCT","TACGA","TACGC","TACGG","TACGT","TACTA","TACTC","TACTG","TACTT","TAGAA","TAGAC","TAGAG","TAGAT","TAGCA","TAGCC","TAGCG","TAGCT","TAGGA","TAGGC","TAGGG","TAGGT","TAGTA","TAGTC","TAGTG","TAGTT","TATAA","TATAC","TATAG","TATAT","TATCA","TATCC","TATCG","TATCT","TATGA","TATGC","TATGG","TATGT","TATTA","TATTC","TATTG","TATTT","TCAAA","TCAAC","TCAAG","TCAAT","TCACA","TCACC","TCACG","TCACT","TCAGA","TCAGC","TCAGG","TCAGT","TCATA","TCATC","TCATG","TCATT","TCCAA","TCCAC","TCCAG","TCCAT","TCCCA","TCCCC","TCCCG","TCCCT","TCCGA","TCCGC","TCCGG","TCCGT","TCCTA","TCCTC","TCCTG","TCCTT","TCGAA","TCGAC","TCGAG","TCGAT","TCGCA","TCGCC","TCGCG","TCGCT","TCGGA","TCGGC","TCGGG","TCGGT","TCGTA","TCGTC","TCGTG","TCGTT","TCTAA","TCTAC","TCTAG","TCTAT","TCTCA","TCTCC","TCTCG","TCTCT","TCTGA","TCTGC","TCTGG","TCTGT","TCTTA","TCTTC","TCTTG","TCTTT","TGAAA","TGAAC","TGAAG","TGAAT","TGACA","TGACC","TGACG","TGACT","TGAGA","TGAGC","TGAGG","TGAGT","TGATA","TGATC","TGATG","TGATT","TGCAA","TGCAC","TGCAG","TGCAT","TGCCA","TGCCC","TGCCG","TGCCT","TGCGA","TGCGC","TGCGG","TGCGT","TGCTA","TGCTC","TGCTG","TGCTT","TGGAA","TGGAC","TGGAG","TGGAT","TGGCA","TGGCC","TGGCG","TGGCT","TGGGA","TGGGC","TGGGG","TGGGT","TGGTA","TGGTC","TGGTG","TGGTT","TGTAA","TGTAC","TGTAG","TGTAT","TGTCA","TGTCC","TGTCG","TGTCT","TGTGA","TGTGC","TGTGG","TGTGT","TGTTA","TGTTC","TGTTG","TGTTT","TTAAA","TTAAC","TTAAG","TTAAT","TTACA","TTACC","TTACG","TTACT","TTAGA","TTAGC","TTAGG","TTAGT","TTATA","TTATC","TTATG","TTATT","TTCAA","TTCAC","TTCAG","TTCAT","TTCCA","TTCCC","TTCCG","TTCCT","TTCGA","TTCGC","TTCGG","TTCGT","TTCTA","TTCTC","TTCTG","TTCTT","TTGAA","TTGAC","TTGAG","TTGAT","TTGCA","TTGCC","TTGCG","TTGCT","TTGGA","TTGGC","TTGGG","TTGGT","TTGTA","TTGTC","TTGTG","TTGTT","TTTAA","TTTAC","TTTAG","TTTAT","TTTCA","TTTCC","TTTCG","TTTCT","TTTGA","TTTGC","TTTGG","TTTGT","TTTTA","TTTTC","TTTTG","TTTTT",]
			combcount = [0] * 1024
			for line in lengths:
				insInfo = line.strip().split('\t')
				insertion = insInfo[1]
				insLen = insInfo[2]
				insCount = int(insInfo[3])
				insPerc = insInfo[4]
				numA += insertion.count('A')
				numC += insertion.count('C')
				numG += insertion.count('G')
				numT += insertion.count('T')
				i = 0
				while i < len(combcount):
					combcount[i] += insertion.count(combinations[i])
					i += 1
				#if insertion == 'ROOT':
					#print("found one")
				if insertion not in insDict: ## have we seen this insertion?
					insDict[insertion] = {"counts":{well:insCount}}
					c += 1
					continue
				if well in insDict[insertion]["counts"]: ## have we seen this insertion in this well?
					insDict[insertion]["counts"][well] += insCount
				else:
					insDict[insertion]["counts"][well] = insCount
			with open('base_count_wells-1024.txt','a') as base_count:
					base_count.write(f"{well}")
					writestuff(base_count, numA, numC, numG, numT,combinations,combcount) #create a new text file and put stuff in it
					#continue
			# print(f"{c} unique insertions in {well}")
			# print(f"{insCount} non-unique in {well}")

countDict = {}

for key in insDict:
	for w in insDict[key]["counts"]:
		if not w in countDict:
			countDict[w] = 1
		else:
			countDict[w] += 1


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(countDict)

with open('darkgreenLT_percinsDict.pkl', 'wb') as file:
	pickle.dump(insDict, file)
