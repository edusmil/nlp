SELECT * FROM edusmil_bdd.nlp_autor_obra;

insert into nlp_autor_obra values (31,'FARDA_FARDAO_CAMISOLA_DORMIR',4,now())

select lower(nlp_corpus_sngram) collate utf8_bin ,count(*) 
from nlp_corpus_sngram
where nlp_corpus_sngram not like '%.%' and nlp_corpus_sngram not like '%-%'  and nlp_corpus_sngram not like '%\'%' and  
nlp_corpus_sngram not like '%?%' and nlp_corpus_sngram not like '%`%' and nlp_corpus_sngram not like '%,%' 
and nlp_corpus_sngram not like '%\%' and nlp_corpus_sngram not like '%!%' and nlp_corpus_sngram not like '%:%' 
group by lower(nlp_corpus_sngram) collate utf8_bin 
order by 2 desc limit 0, 1000


show PROCESSLIST