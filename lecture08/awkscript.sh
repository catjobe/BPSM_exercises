#!/bin/bash

cat mock_NCBI.fasta | awk 'BEGIN{count=0;}{
if(substr($1,1,1)==">")
	{
		count++;
		if(count==1)
			{
				printf $1"\n";
			}
	else {
		printf "\n"$1"\n";
	}
}
else {
	printf $1;
}
}
END {
printf "\n";
}' > singleline_NCBIseqs.fasta
