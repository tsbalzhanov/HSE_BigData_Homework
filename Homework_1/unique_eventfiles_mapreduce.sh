#! /bin/sh
cat data/star2002-sample.csv | python mr/unique_eventfiles_mapper.py | sort -t$'\t' -k1,1 | python mr/unique_eventfiles_reducer.py | tee unique_eventfiles.csv