#!/bin/bash
echo "enter sequence filename: "
read filename
echo "enter file containing patterns to match: "
read patterns
echo "enter output filename: "
read output
perl -pe '/^>/ ? print "\n" : chomp' $filename | grep -f $patterns -w -A1 | grep -v -- "^--$" > $output
