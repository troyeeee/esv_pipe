import vcf
from chr_cfg import *
from ordered_set import OrderedSet

vcf_reader = vcf.Reader(filename=r'/Users/troye/Documents/SVAS/combined.genotyped.sort.vcf')



pos_map = {}
ins_segs = {}
pos_rec_map = {}
pos_to_seg = {}
dup_points = {}

for chrom in CHROMS:
    pos_map[chrom]=OrderedSet()
    ins_segs[chrom]={}
    pos_rec_map[chrom]={}
    pos_to_seg[chrom]={}
    dup_points[chrom]=OrderedSet()


# pre_chr = ''
for record in vcf_reader:
    if record.CHROM == record.INFO['CHR2'] == "chr1":
        if record.var_subtype=="INV":
            print(record.ID)
        pos_map[record.CHROM].add(record.POS)
        pos_rec_map[record.CHROM] = record
        if record.var_subtype=="DUP":
            if record.POS < record.INFO['END']:
                dup_points[record.CHROM].add(record.POS+1)
                dup_points[record.CHROM].add(record.INFO['END'])
        if record.var_subtype=="INS":
            ins_segs[record.CHROM][record.POS] = str(record.POS) + "_INS"
        

# write segment
for k, v in pos_map.items():
    with open(k+".lh", "w") as lh:
        pre_pos = 0
        for i in v:
            seg_name = str(pre_pos)+"_"+str(i)
            pos_to_seg[k][pre_pos] = seg_name
            pos_to_seg[k][i] = seg_name
            if pre_pos in dup_points[k]:
                lh.write("SEG "+seg_name+ " 2 0 0 0\n")
            else:
                lh.write("SEG "+seg_name+ " 1 0 0 0\n")
            if i in ins_segs[k]:
                lh.write("SEG "+ins_segs[k][i]+ " 1 0 0 0\n")   
            pre_pos = i+1

# write junction
# for chrom, recs in pos_rec_map.items():
#     with open(chrom+".lh", "a") as lh:
#         for pos, rec in recs.items():
#             if rec.var_subtype=="DEL":
#                 lh.write("JUNC "+ pos_to_seg[CHROM][pos]+ " + " + pos_to_seg[CHROM][pos] + " + 1")
#             if rec.var_subtype=="DUP":
                












# pos_to_seg = {}
# for k, v in pos_map.items():
#     with open(k+".lh", "a") as lh:
#         pre_pos = 0
#         for i in v:
#             seg_name = str(pre_pos)+"_"+str(i)
#             pre_pos = i
#             lh.write("SEG "+seg_name+ " 1 0 0 0\n")
#             if i in ins_segs[k]:
#                lh.write("SEG "+ins_segs[k][i]+ " 1 0 0 0\n")



# for record in vcf_reader:
#     # if record.POS ==3576514:
#     #     continue
#     # print(record)
#     # print(record.ALT[0)
#     if record.var_subtype=="TRA":
#         print(record.CHROM, record.INFO['CHR2'])