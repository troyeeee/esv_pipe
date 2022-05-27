import vcf

vcf_reader = vcf.Reader(filename=r'/Users/troye/Documents/SVAS/combined.genotyped.sort.vcf')
vcf_writer = vcf.Writer(open('/Users/troye/Documents/SVAS/combined.genotyped.sort.true.vcf', 'w'), vcf_reader)
for record in vcf_reader:
    if record.CHROM != record.INFO['CHR2']:
        continue
    if abs(record.POS-record.INFO['END'])<1000000:
        vcf_writer.write_record(record)
    else:
        print(record.POS, record.INFO['END'])
