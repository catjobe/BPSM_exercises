#!/bin/bash

awk 'BEGIN{FS="\t";}
	{
		if ($1 != "name" && $1 != "" && $6 <= 1995)
			{print $0;}
	}' example_people_data.tsv | wc -l
