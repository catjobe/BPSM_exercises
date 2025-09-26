#!/bin/bash

country=$(cut -f7 example_people_data.tsv | awk '($1 != "country" && $1 != "")' | sort | uniq -c | sort -k1n | tail -1 | awk '{FS="\t";}{print $2;}')

echo "The most common country is $country"

over50s=$(grep "$country" example_people_data.tsv | awk 'BEGIN{FS="\t";}{
	if ($6 <= 1975)
		{print $0;}
	}' | wc -l)


echo "There is $over50s individual over the age of 50 from $country"

