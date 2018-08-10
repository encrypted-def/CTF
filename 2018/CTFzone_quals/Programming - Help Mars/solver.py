import hashlib
import sys
msg = "10532,111808,9066,64465,34874,89064,137,4547,25145,10824,122193,6169,10895,40896,187356,4721,1732,46101,39262,103437,8324,9661,61254,17561,17562,635,183688,24275,24285,172470,54159,90283,812,145888,26216,67897,24483,60020,8749,7176,7233,225944"
print(hashlib.md5(msg.encode()).hexdigest().upper())
print(hashlib.md5(msg.encode()).hexdigest())

vaccine_raw1 = '''1 acgcgtcgac atggagaaaa tagtgcttct'''
vaccine_raw2 = ''' ataaggcggc cgcttaaatg caaattctgc attg'''
vaccine_raw3 = '''atggagaaaa tagtrcttct tcttgcaata gtcagtcttg ttaaaagtga tcagatttgc
       61 attggttacc atgcaaacaa ttcaacagag caggttgaca caatcatgga aaagaacgtt
      121 actgttacac atgcccaaga catactggaa aagacacaca acgggaagct ctgcgatcta
      181 gatggagtga agcctctaat tttaagagat tgtagtgtag ctggatggct cctcgggaac
      241 ccaatgtgtg acgaattcat caatgtaccg gaatggtctt acatagtgga gaaggccaat
      301 ccaaccaatg acctctgtta cccagggagt ttcaacgact atgaagaact gaaacatcta
      361 ttgagcagaa taaaccattt tgagaaaatt caaatcatcc ccaaaagttc ttggtccgat
      421 catgaagcct catcaggagt gagctcagca tgtccatacc tgggaagtcc ctcctttttt
      481 agaaatgtgg tatggcttat caaaaagaac agtacatacc caacaataaa gaaaagctac
      541 aataatacca accaagaaga tcttttggta ctgtggggaa ttcaccatcc taatgatgcg
      601 gcagagcaga caaggctata tcaaaaccca accacctata tttccattgg gacatcaaca
      661 ctaaaccaga gattggtacc aaaaatagct actagatcca aagtaaacgg gcaaagtgga
      721 aggatggagt tcttctgggc aattttaaaa cctaatgatg caatcaactt cgagagtaat
      781 ggaaatttca ttgctccaga atatgcatac aaaattgtca agaaagggga ctcagcaatt
      841 atgaaaagtg aattggaata tggtaactgc aacaccaagt gtcaaactcc aatgggggcg
      901 ataaactcta gtatgccatt ccacaacata caccctctca ccatcgggga atgccccaaa
      961 tatgtgaaat caaacagatt agtccttgca acagggctca gaaatagccc tcaaagagag
     1021 agcagaagaa aaaagagagg actatttgga gctatagcag gttttataga gggaggatgg
     1081 cagggaatgg tagatggctg gtatgggtac caccatagca atgagcaggg gagtgggtac
     1141 gctgcagaca aagaatccac tcaaaaggca atagatggag tcaccaataa ggtcaactca
     1201 attattgaca aaatgaacac tcagtttgag gctgttggaa gggaatttaa taacttagaa
     1261 aggagaatag agaatttaaa caagaagatg gaagacgggt ttctagatgt ttggacttat
     1321 aatgccgaac ttctggttct catggaaaat gagagaactc tagactttca tgactcaaat
     1381 gttaagaacc tctacgacaa ggtccgacta cagcttaggg ataatgcaaa agagctgggt
     1441 aacggttgtt tcgagttcta tcacaaatgt gataatgaat gtatggaaag tataagaaac
     1501 ggaacgtaca actatccgca gtattcagaa gaagcaagat taaaaagaga ggaaataagt
     1561 ggggtaaaat tggaatcaat aggaacttac caaatactgt caatttattc aacagtagcg
     1621 agttccctag cactggcaat catgatagct ggtctatctt tatggatgtg ctccaatgga
     1681 tcgttacaat gcagaatttg catttaa
//'''
vaccine_raw4 = '''atggagaaaa tagtgcttct ttttgcaata gtcagtcttg ttaaaagtga tcagatttgc
       61 attggttacc atgcaaacaa ctcgacagag caggttgaca caataatgga aaagaacgtt
      121 actgttacac atgcccaaga catactggaa aagaaacaca acgggaagct ctgcgatcta
      181 gatggagtga agcctctaat tttgagagat tgtagcgtag ctggatggct cctcggaaac
      241 ccaatgtgtg acgaattcat caatgtgccg gaatggtctt acatagtgga gaaggccaat
      301 ccagtcaatg acctctgtta cccaggggat ttcaatgact atgaagaatt gaaacaccta
      361 ttgagcagaa taaaccattt tgagaaaatt cagatcatcc ccaaaagttc ttggtccagt
      421 catgaagcct cattaggggt gagctcagca tgcccatacc agggaaagtc ctcctttttc
      481 agaaatgtgg tatggcttat caacaagaac agtacatacc caacaataaa gaggagctac
      541 aataatacca accaagaaga tcttttggta ctgtggggga ttcaccatcc taatgatgcg
      601 gcagagcaga caaagctcta tcaaaaccca accacctata tttccgttgg gacatcaaca
      661 ctaaaccaga gattggtacc aagaatagct actagatcca aagtaaacgg gcaaagtgga
      721 aggatggagt tcttctggac aattttaaag ccgaatgatg caatcaactt cgagagtaat
      781 ggaaatttca ttgctccaga atatgcatac aaaattgtca agaaagggga ctcaacaatt
      841 atgaaaagtg aattggaata tggtaactgc aacaccaagt gtcaaactcc aatgggggcg
      901 ataaactcta gcatgccatt ccacaatata caccctctca ccattgggga atgccccaaa
      961 tatgtgaaat caaacagatt agtccttgcg actgggctca gaaatagccc tcaacgagag
     1021 acgcgaggat tatttggagc tatagcaggt tttatagagg gaggatggca gggaatggta
     1081 gatggttggt atgggtacca ccatagcaat gagcagggga gtgggtacgc tgcagacaaa
     1141 gaatccactc aaaaggcaat agatggagtc accaataagg tcaactcgat cattgacaaa
     1201 atgaacactc agtttgaggc cgttggaagg gaatttaaca acttagaaag gagaatagag
     1261 aatttaaaca agaagatgga agacgggttc ctagatgtct ggacttataa tgctgaactt
     1321 ctggttctca tggaaaatga gagaactcta gactttcatg actcaaatgt caagaacctt
     1381 tacgacaagg tccgactaca gcttagggat aatgcaaagg agctgggtaa cggttgtttc
     1441 gagttctatc ataaatgtga taatgaatgt atggaaagtg taagaaatgg aacgtatgac
     1501 tacccgcagt attcagaaga agcgagacta aaaagagagg aaataagtgg agtaaaattg
     1561 gaatcaatag gaatttacca aatactgtca atttattcta cagtggcgag ttccctagca
     1621 ctggcaatca tggtagctgg tctatcctta tggatgtgct ccaatggatc gttacaatgc
     1681 agaatttgca tttaa'''
vaccine_raw5 = '''atggagaaaa tagtgcttct tcttgcaata gtcagccttg ttaaaagtga tcagatttgc
       61 attggttacc atgcaaacaa ctcgacagag caggttgaca caataatgga aaagaacgtt
      121 actgttacac atgcccaaga catactggaa aagacacaca acgggaagct ctgcgatcta
      181 gatggagtga agcctctgat tttaagagat tgtagtgtag ctggatggct cctcggaaac
      241 ccaatgtgtg acgaattcat caatgtgccg gaatggtctt acatagtgga gaaggccaac
      301 ccagccaatg acctctgtta cccagggaat ttcaacgact atgaagaact gaaacaccta
      361 ttgagcagaa taaaccattt tgagaaaatt cagatcatcc ccaaaagttc ttggtccgat
      421 catgaagcct catcaggggt gagctcagca tgtccatacc agggaacgcc ctcctttttc
      481 agaaatgtgg tatggcttat caaaaagaac aatacatacc caacaataaa gagaagctac
      541 aataatacca accaggaaga tcttttgata ctgtggggga ttcatcattc taatgatgcg
      601 gcagagcaga caaagctcta tcaaaaccca accacctata tttccgttgg gacatcaaca
      661 ctaaaccaga gattggtacc aaaaatagct actagatcca aagtaaacgg gcaaagtgga
      721 aggatggatt tcttctggac aattttaaaa ccgaatgatg caatcaactt cgagagtaat
      781 ggaaatttca ttgctccaga atatgcatac aaaattgtca agaaagggga ctcagcaatt
      841 gttaaaagtg aagtggaata tggtaactgc aacacaaagt gtcaaactcc aataggggcg
      901 ataaactcta gtatgccatt ccacaacata caccctctca ccatcgggga atgccccaaa
      961 tatgtgaaat caaacaaatt agtccttgcg actgggctca gaaatagtcc tctaagagaa
     1021 agaagaagaa aaagaggact atttggagct atagcagggt ttatagaggg aggatggcag
     1081 ggaatggtag atggttggta tgggtaccac catagcaatg agcaggggag tgggtacgct
     1141 gcagacaaag aatccactca aaaggcaata gatggagtca ccaataaggt caactcgatc
     1201 attgacaaaa tgaacactca gtttgaggcc gttggaaggg aatttaataa cttagaaagg
     1261 agaatagaga atttaaacaa gaaaatggaa gacggattcc tagatgtctg gacttataat
     1321 gctgaacttc tggttctcat ggaaaatgag agaactctag acttccatga ttcaaatgtc
     1381 aagaaccttt acgacaaggt ccgactacag cttagggata atgcaaagga gctgggtaac
     1441 ggttgtttcg agttctatca caaatgtgat aatgaatgta tggaaagtgt aagaaacgga
     1501 acgtatgact acccgcagta ttcagaagaa gcaagattaa aaagagagga aataagtgga
     1561 gtaaaattgg aatcaatagg aacttaccaa atactgtcaa tttattcaac agttgcgagt
     1621 tctctagcac tggcaatcat ggtggctggt ctatctttgt ggatgtgctc caatgggtcg
     1681 ttacaatgca gaatttgcat ttaa'''
#vaccine_raw = vaccine_raw1+vaccine_raw2+vaccine_raw3+vaccine_raw4+vaccine_raw5
vaccine_raw = vaccine_raw3
vaccine = "" # len 1706

def cmp(S1,S2):
  L1 = S1.split(',')
  L2 = S2.split(',')
  if len(L1) > len(L2): return S2
  if len(L2) > len(L1): return S1
  idx = 0
  while True:
    if leninfo[int(L1[idx])] < leninfo[int(L2[idx])]:
      return S2
    elif leninfo[int(L1[idx])] > leninfo[int(L2[idx])]:
      return S1
    idx += 1


for c in vaccine_raw:
  if c in 'atcgr':    
    vaccine += c.upper()
  #if c == 'a': vaccine += 'T'
  #if c == 't': vaccine += 'A'
  #if c == 'g': vaccine += 'C'
  #if c == 'c': vaccine += 'G'

print(len(vaccine))
for i in range(0,len(vaccine),10):
  print(i,vaccine[i:i+10])
#vaccine = vaccine[::-1]
D1 = [['']*6000 for i in range(6000)]
D2 = ['']*6000
leninfo = [0]*250000
seqq = ['']*250000
f = open("mars_dna_samples.txt")
for line in f.readlines():
  line = line.strip()
  num,seq=line.split(',')
  #if seq == 'TTCT': print(num)
  leninfo[int(num)] = len(seq)
  seqq[int(num)] = seq
  idx = -1
  while True:
    idx = vaccine.find(seq,idx+1)
    if idx == -1: break
    D1[idx][idx+len(seq)] = num

for last in range(1,len(vaccine)+1):
  if D1[0][last]:
    D2[last] = D1[0][last]
  for st in range(1,last):
    if D2[st] and D1[st][last]:
      if not D2[last]:
        D2[last]=D2[st]+','+D1[st][last]
      else:
        D2[last] = cmp(D2[last],D2[st]+','+D1[st][last])


print(D2[len(vaccine)])
chunk = list(map(int,D2[len(vaccine)].split(',')))
S=""
for c in chunk:
#  if seqq[c] in ["AAACCA","GGAAG","GGGA","TTCT"]:
#    print(c,seqq[c])
  #print(seqq[c], c)
  S += seqq[c]

"""
Collision
AAACCA
GGAAG
GGGA
TTCT
"""
