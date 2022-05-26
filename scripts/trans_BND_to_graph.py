import vcf
from chr_cfg import *
from ordered_set import OrderedSet

vcf_reader = vcf.Reader(filename=r'/Users/troye/Documents/SVAS/combined.genotyped.sort.vcf')



pos_map = {}
for chrom in CHROMS:
    pos_map[chrom]=OrderedSet()


# pre_chr = ''
for record in vcf_reader:
    if record.CHROM == record.INFO['CHR2']:
        pos_map[record.CHROM].add(record.POS)
        

# write segment
for k, v in pos_map.items():
    with open(k+".lh", "w") as lh:
        pre_pos = 0
        for i in v:
            seg_name = str(pre_pos)+"_"+str(i)
            pre_pos = i
            lh.write("SEG "+seg_name+ " 1 0 0 0\n")        




for record in vcf_reader:
#     # if record.POS ==3576514:
#     #     continue
#     # print(record)
#     # print(record.ALT[0)
#     if record.var_subtype=="TRA":
#         print(record.CHROM, record.INFO['CHR2'])