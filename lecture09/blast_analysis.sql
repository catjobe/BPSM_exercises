use s2901468_blast;

/* Question 1 */

select sqacc from blast_table where mismatch > 20; 

/* Question 2 */

select sqacc from blast_table where mismatch > 20 and alignment_length < 100;

/* Question 3 */

select sqacc from blast_table where mismatch > 20 limit 20; 

/* Question 4 */

select count(*) from blast_table where alignment_length < 100;

/* Question 5 */

select sqacc from blast_table order by bitscore desc limit 10; 

/* Question 6 */

select sqacc from blast_table where sqacc LIKE "%AEI%";

/* Question 7 */

select count(*) from (select sqacc from blast_table group by sqacc having count(*) > 1) as duplicates;

/* Question 8 */

select 100*mismatch/alignment_length from blast_table;

/* Question 9 */

select * from blast_table where bitscore < 200;

select * from blast_table where bitscore >= 200;
