SELECT * FROM edusmil_bdd.nlp_autor_obra
order by 3

insert into nlp_autor_obra values (31,'FARDA_FARDAO_CAMISOLA_DORMIR',4,now())

select lower(nlp_corpus_ngram) collate utf8_bin ,count(*) 
from nlp_corpus_ngram
where nlp_corpus_ngram not like '%.%' and nlp_corpus_ngram not like '%-%'  and nlp_corpus_ngram not like '%\'%' and  
nlp_corpus_ngram not like '%?%' and nlp_corpus_ngram not like '%`%' and nlp_corpus_ngram not like '%,%' 
and nlp_corpus_ngram not like '%\%' and nlp_corpus_ngram not like '%!%' and nlp_corpus_ngram not like '%:%' and 
nlp_corpus_ngram not like '%—%' and nlp_corpus_ngram not like '%;%' 
and nlp_n_gram=2
group by lower(nlp_corpus_ngram) collate utf8_bin 
order by 2 desc limit 0, 400


show PROCESSLIST