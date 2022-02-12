#!/bin/bash
CUTESV=/home/grads/gzpan2/apps/miniconda3/envs/cityu/bin/cuteSV
SNIFFILES=/home/grads/gzpan2/apps/Sniffles-master/bin/sniffles-core-1.0.12/sniffles
NANOSV=/home/grads/gzpan2/apps/miniconda3/envs/cityu/bin/NanoSV
bam=$1
ref=$2
out_dir=$3
threads=$4

if [ ! -d $out_dir/sniffiles ]; then
  mkdir $out_dir/sniffiles
fi
if [ ! -d $out_dir/cutesv ]; then
  mkdir $out_dir/cutesv
fi
# if [ ! -d $out_dir/gridss ]; then
#   mkdir $out_dir/gridss
# fi
if [ ! -d $out_dir/nanosv ]; then
  mkdir $out_dir/nanosv
fi

# sniffiles
$SNIFFILES -m $bam -v $out_dir/sniffiles/snif.vcf -s 2 --max_distance 300 -n -1

# cutesv
CUTESV $bam $ref $out_dir/cutesv/cute.vcf $out_dir/cutesv --max_cluster_bias_INS 100 --diff_ratio_merging_INS 0.3 --max_cluster_bias_DEL 200 --diff_ratio_merging_DEL 0.5 --report_readid --threads $threads