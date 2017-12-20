#! /bin/sh
cat data/star2002-sample.csv | python mr/average_pt_mapper.py | sort -t$'\t' -k1,1 | python mr/average_pt_reducer.py | tee average_pt.csv
