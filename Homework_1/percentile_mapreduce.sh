#! /bin/sh
cat data/star2002-sample.csv | python mr/percentile_mapper.py | sort -t$'\t' -k1,1 | python mr/percentile_reducer.py | tee percentiles.csv