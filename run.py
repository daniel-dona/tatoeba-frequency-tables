#!/usr/bin/env python3

sentences_file = "sentences.csv"

output_path = "output/"

list_size = 10000

skip_lang = ["cmn", "kor", "\\N", "jpn"]

gen_list = ["spa", "eng", "ita"]

remove_symb = [".", ",", "?", "!", "¿", "¡"]

lang_list = []

if len(gen_list) != 0:
	
	lang_list = gen_list
	
else:

	with open(sentences_file) as sentences:

		for sentence in sentences:
		
			col = sentence.split("\t")
			
			if not col[1] in lang_list and not col[1] in skip_lang:
			
				lang_list.append(col[1])
	
print("Language list:", lang_list, flush=True)
	

			
for lang in lang_list:
	
	print("Processing language:", lang, flush=True)
	
	freq_list = {}
	
	with open(sentences_file) as sentences:
		
		with open(output_path+lang+".txt", "w+") as output_file:

			for sentence in sentences:
			
				col = sentence.split("\t")
				
				if col[1] == lang:
					
					words = col[2].replace("\n", "").split(" ")
					
					for word in words:
						
						for symb in remove_symb:
							
							word = word.replace(symb, "")
						
						if word in freq_list:
							
							freq_list[word] += 1
							
						else:
						
							freq_list[word] = 1
							
			ordered_list = { k:v for k, v in sorted(freq_list.items(), key=lambda item: item[1], reverse=True) }
				
			for item in list(ordered_list.keys())[:list_size]:
					
				print(item, ordered_list[item], file=output_file)
				
		
